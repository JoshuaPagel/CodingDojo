from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
db = 'dojo_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def show_dojos(cls):
        query = "SELECT * FROM dojos;"
        db_response = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in db_response:
            dojos.append(cls(dojo))
        # print(db_response)
        return dojos
    
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(db).query_db(query, data)
        # print(result)
        return result
    
    # @classmethod
    # def get_dojo_with_ninjas(cls, data):
    #     query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id VALUES %(id)s;"
    #     result = connectToMySQL(db).query_db(query, data)
    #     print(result)
    #     return(result)

    @classmethod
    def get_one_dojo(cls, ninja_id_in_dict):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL(db).query_db(query, ninja_id_in_dict)
        new_ninja = cls(results[0])
        for dojo_w_ninjas in results:
            ninja_data = {
                'id': dojo_w_ninjas['ninjas.id'],
                'dojo_id': dojo_w_ninjas['dojo_id'],
                'first_name': dojo_w_ninjas['first_name'],
                'last_name': dojo_w_ninjas['last_name'],
                'age': dojo_w_ninjas['age'],
                'created_at': dojo_w_ninjas['ninjas.created_at'],
                'updated_at': dojo_w_ninjas['ninjas.updated_at']
            }
            new_ninja.ninjas.append(ninja_model.Ninja(ninja_data))
        # print(results)
        return new_ninja