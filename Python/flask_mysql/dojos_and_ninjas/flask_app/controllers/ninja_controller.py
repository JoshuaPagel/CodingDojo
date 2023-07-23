from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo
# from flask_app.models.dojo_model import Dojo

@app.route('/')
def home():
    return redirect ('/dojos')

@app.route('/dojos')
def show_dojos():
    return render_template('dojos.html', dojos=Dojo.show_dojos())

# @app.route('/dojos/{{dojo.id}}')
# def dojo_select():
#     return render_template('ninjas.html')

@app.route('/create_ninja')
def create_ninja():
    return render_template('/new_ninja.html', dojos=Dojo.show_dojos())

@app.route('/save_ninja', methods=['POST'])
def ninja():
    Ninja.save_ninja(request.form)
    return redirect('/')

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect ('/dojos')

# @app.route('/dojo/<int:dojo_id>')
# def ninjas_table():
#     dojo_id_in_a_dict = {
#         'id': dojo_id
#     }
#     return render_template('/ninjas.html', dojo_id_in_a_dict = Dojo.get_dojo_with_ninjas(dojo_id_in_a_dict))

# @app.route('/dojo/<int:dojo_id>')
# def ninja_table():
#     Dojo.get_dojo_with_ninjas(request.form)
#     return render_template('/ninjas.html')


# @app.route('/dojo/<int:dojo_id>')
# def show_ninjas():
#     Dojo.get_dojo_with_ninjas(request.form)
#     return render_template('/ninjas.html', ninja=Ninja.show_ninjas())

# @app.route('/dojo/<int:dojo_id>')
# def show_ninjas(dojo_id):

#     Dojo.get_dojo_with_ninjas(request.form)
#     return render_template('/ninjas.html', dojos=Dojo.get_dojo_with_ninjas)