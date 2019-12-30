from app import app, db
from flask import render_template, request, redirect, url_for, flash
from models.contact_us import ContactUs
from posts.forms import ContactUsForm


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
        except:
            flash('Your form wasn\'t send.')
        return redirect(url_for('contacts'))

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

