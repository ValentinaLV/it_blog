from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError

from app import app, db
from models.contact_us import ContactUs
from models.user import User
from posts.forms import ContactUsForm, RegistrationForm


@app.route('/')
def index():
    return render_template('base.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/about')
def disabled():
    return render_template('about.html')


@app.route('/contacts', methods=['POST', 'GET'])
def contacts():
    form = ContactUsForm(request.form)
    if request.method == 'POST':
        if form.validate():
            contact_us_msg = ContactUs(name=form.name.data,
                                       email=form.email.data,
                                       telephone=form.telephone.data,
                                       subject=form.subject.data,
                                       message=form.message.data)
            db.session.add(contact_us_msg)
            db.session.commit()
            flash('Your form was successfully send.')
        elif not form.validate():
            flash('Your form wasn\'t send.')

    return render_template('contact.html', form=form)


@app.route('/sign-up', methods=["GET", "POST"])
def register_user():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('User was successfully registered.')
        except IntegrityError:
            flash('User wasn\'t registered. Username or email isn\'t unique. Try again.')
        return redirect(url_for('security.login'))

    return render_template('sign_up.html', form=form)
