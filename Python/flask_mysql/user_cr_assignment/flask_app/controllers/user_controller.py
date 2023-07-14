from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User


@app.route('/')
def home():
    return redirect('/table')

@app.route('/table')
def table():
    return render_template ("table.html", users=User.select_all_users())

@app.route('/table/create')
def add():
    return render_template('sign_up.html')

@app.route('/table/save', methods=['POST'])
def save():
    User.save_user(request.form)
    return redirect('/table')