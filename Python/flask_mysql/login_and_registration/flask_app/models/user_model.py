from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'login_and_reg'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def select_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users
    
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL(db).query_db(query, data)
        return result
    
    @staticmethod
    def validate_register(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user_data["email"]): 
            flash("Email format is invalid or already is being used.")
            is_valid = False
        if len(user_data["password"]) < 8:
            flash("Password must have more than 8 characters.")
            is_valid = False
        if user_data["password"] != user_data ['confirm_password']:
            flash("Passwords don't match")
            is_valid = False
        print("$$$$$$$$$$$$$$$$$$$")
        return is_valid

    # @staticmethod
    # def validate_login(user_data):
    #     is_valid = True
    #     query = "SELECT * FROM users WHERE email = %(email)s"
    #     results = connectToMySQL(User.db).query_db(query, user_data)
    #     return is_valid

    @classmethod
    def find_user_by_email(cls, email_dict):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query, email_dict)
        # print(results)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def find_user_by_id(cls, email_dict):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, email_dict)
        # print(results)
        return cls(results[0])