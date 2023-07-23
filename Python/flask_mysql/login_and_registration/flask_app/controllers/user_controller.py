from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#You will also need a bycrypt import (we will introduce this week 5)


@app.route('/')
def home():
    return render_template('login_and_reg.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    User.save_user(request.form)
    print(request.form)
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print (pw_hash)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    return redirect("/users")

@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard html page here!')