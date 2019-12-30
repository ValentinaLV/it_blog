from flask_security import UserMixin

from app import db
from .users_roles import users_role


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)
    roles = db.relationship("Role", secondary=users_role,
                            backref=db.backref('users'),
                            lazy='dynamic')

    def __repr__(self):
        return "<User email: {}, active: {}>".format(self.email, self.active)
