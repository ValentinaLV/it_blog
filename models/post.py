from datetime import datetime

from app import db
from models.post_tags import post_tags, slugify


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    tags = db.relationship('Tag',
                           secondary=post_tags,
                           backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = self.generate_slug()

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

    def generate_slug(self):
        if self.title:
            return slugify(self.title)
