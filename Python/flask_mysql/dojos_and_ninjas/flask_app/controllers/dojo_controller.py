from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/dojo/<int:dojo_id>')
def show_dojos_ninjas(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }
    return render_template('/ninjas.html', dojo_info_w_user = Dojo.get_one_dojo(data))

# @app.route('/create_dojo', methods=['POST'])
# def create_dojo():
#     Dojo.save_dojo(request.form)
#     return redirect ('/dojos')

# @app.route('/dojo/<int:dojo_id>')
# def show_ninjas():
#     Dojo.get_dojo_with_ninjas(request.form)
#     return render_template('/ninjas.html', ninja=Ninja.show_ninjas())