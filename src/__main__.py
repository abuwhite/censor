"""Main module engine."""


from flask import Flask, render_template, request, redirect

from src.utils.bank import BankAccount
from babel import numbers

app = Flask(__name__)


def currency(num):
    """Return format number."""
    return numbers.format_currency(num, "KZT", locale="kk_KZ")


@app.route("/")
def index():
    """Generate start page."""
    return render_template("index.html")


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


@app.route("/info")
def info():
    """Generate info page."""
    return render_template(
        "info.html",
        balance=currency(user.balance),
        day=currency(user.balance_for_day),
        expenses=currency(user.expenses),
        capital=currency(user.capital),
        year=currency(user.capital_year),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
