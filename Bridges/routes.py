from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from Bridges import db, LoginManager
from flask import Flask
import os
import calendar
from Bridges.forms import LoginForm, RegisterForm
from Bridges.models import User

#import Database
#from flask_login import UserMixin
#from app import login
from flask_login import current_user, login_user
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy  import SQLAlchemy
#from app import db


 


@app.route('/')
def home():
    return render_template('home.html')
    print (calendar.weekheader(3))  

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('login.html'))

        return '<h1>Invalid username  or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    
    if form.validate_on_submit():
        #form.error
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
    
    #    return 'Never goes into the if statement'

        #return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.email.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

#from app import routes, models

