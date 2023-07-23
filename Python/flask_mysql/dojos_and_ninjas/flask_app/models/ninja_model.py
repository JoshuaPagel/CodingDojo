from flask_app.config.mysqlconnection import connectToMySQL

import pprint

db = 'dojo_and_ninjas_schema'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def show_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        db_response = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in db_response:
            ninjas.append(cls(ninja))
        print(db_response)
        return ninjas
    

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result