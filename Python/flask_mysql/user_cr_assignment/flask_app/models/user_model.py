from flask_app.config.mysqlconnection import connectToMySQL

db = 'assignment_users'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.owner = data['user_id']


    @classmethod
    def select_all_users(cls):
        query = "SELECT * FROM users;"
        db_response = connectToMySQL(db).query_db(query)
        users = []
        for user in db_response:
            users.append( cls(user) )
        return users
    

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        # db_response = connectToMySQL('assignment_users').query_db(query, form_data)
        # print(db_response)
        result = connectToMySQL(db).query_db(query, data)
        return result
    
# I'm stumped on connecting the database