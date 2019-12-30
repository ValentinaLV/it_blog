from flask import render_template, request, redirect, url_for, flash
from passlib.handlers.sha2_crypt import sha512_crypt

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
    form = ContactUsForm()

    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        subject = request.form.get('subject', '')
        telephone = request.form.get('telephone', '')
        message = request.form.get('message', '')
        try:
            contact_us_msg = ContactUs(name=name, email=email,
                                       telephone=telephone,
                                       subject=subject,
                                       message=message)
            db.session.add(contact_us_msg)
            db.session.commit()
            flash('Your form was successfully send.')
        except Exception:
            flash('Your form wasn\'t send.')
        return redirect(url_for('contacts'))

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register_user():
    form = RegistrationForm()

    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        password = sha512_crypt.encrypt((str(request.form.get('password', ''))))
        try:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('User was successfully registered.')
        except Exception:
            flash('User wasn\'t registered.')
        return redirect(url_for('security.login'))

    elif request.method == 'GET':
        return render_template('register.html', form=form)
