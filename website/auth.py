from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.wrappers.response import _clean_accept_ranges
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#Defines that this file is a blueprint of my application
auth=Blueprint('auth',__name__)

#Define login with its HTML template
@auth.route('/login', methods=['GET', 'POST'])                       #ability to accept GET and POST requests
def login():
    if request.method=='POST':                                       #work if login is submitted
        email=request.form.get('email')                              #get login information
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()             #filters all of the users that have that email and shows first result
        if user:                                                       #if there is a user
            if check_password_hash(user.password, password):           #check if password matches the one in the db
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)                      #remembers that user is logged in
                return redirect(url_for('views.home'))                 #redirect to home page
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)               #pass value to template

#Define logout with its HTML template
@auth.route('/logout')                                                 #ability to accept GET and POST requests
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#Define Sign up with its HTML template, save the information
#from the form in a database, and flash messages
@auth.route('/sign-up', methods=['GET', 'POST'])                     #ability to accept GET and POST requests
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        first_name=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user=User.query.filter_by(email=email).first()
        if user:                                                       #check if user already exists
            flash('Email already exists.', category='error')         
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user=User(email=email, first_name=first_name, 
                password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()                                #Update database
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))             #Redirect user to home page

    return render_template("sign_up.html", user=current_user)