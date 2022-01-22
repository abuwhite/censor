from app import db

import datetime
from werkzeug.security import generate_password_hash, \
     check_password_hash


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    datetime_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lines = db.relationship('Line', cascade="all,delete", backref=db.backref('song', lazy='joined'), lazy='dynamic')
    is_deleted = db.Column(db.Boolean, default=False)


class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
    spans_of_time = db.relationship('SpanOfTime', cascade="all,delete", backref=db.backref('line', lazy='joined'), lazy='dynamic')


class SpanOfTime(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    line_id = db.Column(db.Integer, db.ForeignKey('line.id'))
    starting_64th = db.Column(db.Integer)  # I'm assuming the highest-granularity desired will be a 1/64th note-length.
    length = db.Column(db.Integer)  # I guess this'll be in 1/64th notes, so a 1/16th note will be '4'.
    content = db.Column(db.String(80))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), primary_key=True, unique=True)
    display_name = db.Column(db.String(80), default="A Rhymecraft User")
    password_hash = db.Column(db.String(200))
    datetime_subscription_valid_until = db.Column(db.DateTime, default=datetime.datetime.utcnow() - datetime.timedelta(days=1))
    datetime_joined = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    songs = db.relationship('Song', cascade="all,delete", backref=db.backref('user', lazy='joined'), lazy='dynamic')

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)


def init_db():
    db.create_all()

    # Create a test user
    new_user = User('a@a.com', 'aaaaaaaa')
    new_user.display_name = 'Nathan'
    db.session.add(new_user)
    db.session.commit()

    new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
    db.session.commit()


if __name__ == '__main__':
    init_db()