from app import db
from models.user import User

from app import user_datastore

# db.create_all()
# user_datastore.create_user(email="tina.lysenok@gmail.com",
#                            password="Admin")
# db.session.commit()

user = User.query.first()
print(user)
print(user.id)
