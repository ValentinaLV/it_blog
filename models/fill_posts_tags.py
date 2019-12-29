from models.tag import Tag
from models.post import Post
from app import db

# -----Post-Tag db insert (many-to-many relation)-----
t5 = Tag.query.all()[4]
print(t5)
post_query = Post.query.filter(Post.id == 29)
print(post_query)
post29 = post_query.first()
print(post29)
print(post29.tags)
print()
# add tag(id=4/.first()) to post(id=29)
# post29.tags.append(t5)
# print(post29.tags)
# db.session.add(post29)
# db.session.commit()

t6 = Tag.query.filter(Tag.id == 6).first()
t8 = Tag.query.filter(Tag.id == 8).first()
t9 = Tag.query.filter(Tag.id == 9).first()
t10 = Tag.query.filter(Tag.id == 10).first()
t11 = Tag.query.filter(Tag.id == 11).first()
post29.tags.append(t6)
post29.tags.append(t8)
post29.tags.append(t9)
post29.tags.append(t10)
post29.tags.append(t11)
print(post29.tags)
db.session.add(post29)
db.session.commit()

# # delete references]
# t5 = Tag.query.all()[4]
# post29 = Post.query.filter(Post.id == 29)[0]
# print(post29)
# post29.tags.remove(t5)
# print(post29.tags)
# db.session.add(post29)
# db.session.commit()