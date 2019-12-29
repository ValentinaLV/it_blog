from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/about')
def disabled():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

