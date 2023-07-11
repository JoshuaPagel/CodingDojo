from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User


@app.route('/')
def home():
    return redirect('/table')

@app.route('/table')
def table():
    # user_id = users.create_user(request.form)
    # session['user_id'] = user_id
    # session['first_name'] = request.form['first_name']
    # session['last_name'] = request.form['last_name']
    # session['email'] = request.form['email']
    # session['created_at'] = request.form['email']
    return render_template ("table.html")

@app.route('/table/create')
def add():
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # email = request.form['email']
    # created_at = request.form['created_at']
    # user_id = users.create_user(request.form)
    # session['user_id'] = request.form ['user_id']
    # session['first_name'] = request.form['first_name']
    # session['last_name'] = request.form['last_name']
    # session['email'] = request.form['email']
    # session['created_at'] = request.form['email']
    return render_template('sign_up.html')

@app.route('/table/save', methods=['POST'])
def save():
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # email = request.form['email']
    # created_at = request.form['created_at']
    print(request.form)
    User(request.form)
    return redirect('/table')
    # first_name=first_name, last_name=last_name, email=email, created_at=created_at)