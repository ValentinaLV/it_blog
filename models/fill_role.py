from app import db
from models.role import Role

from app import user_datastore

# db.create_all()
# user_datastore.create_role(name='admin')
# db.session.commit()

role = Role.query.first()
print(role.name)
