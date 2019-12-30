from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from config import Configuration
from models.admin import AdminView, HomeAdminIndexView

app = Flask(__name__)
Bootstrap(app)

# beneath debug=True
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ADMIN #
from models.post import Post
from models.tag import Tag

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminIndexView(name='Home'))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Tag, db.session))

# Flask user-security #
from models.user import User
from models.role import Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

