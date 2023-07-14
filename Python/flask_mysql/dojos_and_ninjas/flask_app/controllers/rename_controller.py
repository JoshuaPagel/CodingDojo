from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.rename_model import Rename #importing the class here

@app.route('/')
def home():
    return redirect ('/dojo')

@app.route('/dojo')
def rename1():
    return render_template('dojos.html')

@app.route('/dashboard')
def rename2():
    return render_template('Dashboard html page here!')