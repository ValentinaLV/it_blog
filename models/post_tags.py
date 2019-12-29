import re
from app import db


def slugify(string):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', string)


post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )

# class PostTags(db.Model):
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))



