from app import db


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(100))
    telephone = db.Column(db.String(20))
    subject = db.Column(db.String(100))
    message = db.Column(db.Text)

    def __repr__(self):
        return "<ContactUs form name: {}, email: {}, subject: {}>".format(self.name, self.email, self.subject)
