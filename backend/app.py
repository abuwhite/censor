"""Views module."""
import os

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required

from flask import render_template, request, redirect, Flask, url_for

from main.bank import BankAccount
from babel import numbers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique=True, index=True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def currency(num):
    """Return format number."""
    return numbers.format_currency(num, "KZT", locale="kk_KZ")


@app.route('/home')
def home():
    return render_template('main/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('home'))
        flash('Invalid email address or Password.')
    return render_template('main/login-new.html', form=form)


@login_required
def protected():
    return redirect(url_for('forbidden.html'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('main/registration.html', form=form)


@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/")
def index():
    """Generate start page."""
    return render_template("main/registration_old.html")


@app.route("/", methods=["POST"])
def index_post():
    """POST Form function."""
    global user
    user = BankAccount(
        _income=int(request.form["amount"]),
        _expenses=int(request.form["loan"]),
        _percent=int(request.form["capital"]),
    )

    return redirect("/info")


# @app.route("/", methods=["POST"])
# def index_post():
#     """POST Form function."""
#     global user
#     user = BankAccount(
#         _income=int(request.form["amount"]),
#         _expenses=int(request.form["loan"]),
#         _percent=int(request.form["capital"]),
#     )
#
#     return redirect("/info")


@app.route("/info")
def info():
    """Generate info page."""
    return render_template(
        "main/info.html",
        balance=currency(user.balance),
        day=currency(user.balance_for_day),
        expenses=currency(user.expenses),
        capital=currency(user.capital),
        year=currency(user.capital_year),
    )
