from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

# @app.route('')
# def get_all_recipes_w_users

@app.route('/dashboard/<int:recipe_id>')

@app.route('/dashboard/new')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/dashboard/create', methods=['POST'])
def create_recipe():
    data = {
        'name' : request.form['recipe_name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'under30' : request.form['under30'],
        'date_made' : request.form['date_made'],
        'user_id' : request.form['user_id']
    }