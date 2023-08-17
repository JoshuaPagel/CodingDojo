from flask_app.config.mysqlconnection import connectToMySQL

db= 'recipes'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under30 = data['under30']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def show_recipes(cls):
        query = "SELECT * FROM recipes;"
        db_response = connectToMySQL(db).query_db(query)
        recipes = []
        for recipe in db_response:
            recipes.append(cls(recipe))
        print(db_response)
        return recipes  
    

    # @classmethod
    # def save_recipes(cls, data):
    #     query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
    #     result = connectToMySQL(db).query_db(query, data)
    #     return result