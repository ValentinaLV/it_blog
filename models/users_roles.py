from app import db

users_role = db.Table("users_roles",
                      db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                      db.Column("role_id", db.Integer, db.ForeignKey("role.id"))
                      )
