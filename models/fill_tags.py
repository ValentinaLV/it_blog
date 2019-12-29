from models.tag import Tag
from app import db


# -----Tag db insert-----
# tag = Tag(name='python')
# tag1 = Tag(name='flask')
# tag2 = Tag(name='django')
# tag3 = Tag(name='pip')
# db.session.add_all([tag2, tag3])
# db.session.commit()
# tag4 = Tag(name='skills')
# tag5 = Tag(name='job')
# tag6 = Tag(name='certification')
# db.session.add_all([tag4, tag5, tag6])
# db.session.commit()
tag7 = Tag(name='story')
tag8 = Tag(name='blog')
tag9 = Tag(name='work')
tag10 = Tag(name='personal')
db.session.add_all([tag7, tag8, tag9, tag10])
db.session.commit()
tags = Tag.query.all()
print(tags)
