from wtforms import Form, StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import ValidationError


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired(message="Enter title of the post please.")])
    body = TextAreaField('Body', validators=[DataRequired(message="Enter text of the post please.")])


class ContactUsForm(Form):
    name = StringField('Name', validators=[DataRequired(message="Enter your name please.")])
    email = StringField('Email', validators=[DataRequired(message="Enter your email please."), Email()])
    telephone = StringField('Telephone', validators=[DataRequired(message="Enter your telephone please."),
                                                     Length(min=10, max=13)])
    subject = StringField('Subject', validators=[DataRequired(message="Enter the subject please.")])
    message = TextAreaField('Message')
    submit = SubmitField("Send")


class RegistrationForm(Form):
    username = StringField('Username', [DataRequired(message="Enter your username please."),
                                        Length(min=4, max=100)])
    email = StringField('Email Address', [DataRequired(message="Enter your email please."),
                                          Length(min=6, max=100), Email()])
    password = PasswordField('New Password', [
        DataRequired(message="Enter your password please."), Length(min=6, max=20),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2020)',
                              [DataRequired(DataRequired(message="Accept the terms."))])
    submit = SubmitField("Send")
