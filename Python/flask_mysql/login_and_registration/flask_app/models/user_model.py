from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'login_and_reg'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.first_name = data['last_name']
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
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters and letters only.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters and letters only.")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]): 
            flash("Email format is invalid or already is being used.")
            is_valid = False
        if len(user["password"]) < 8:
            flash("Password must have more than 8 characters.")
            is_valid = False
        if len(user["confirm_password"]) < 8:
            flash("Passwords don't match")
            is_valid = False
        print("$$$$$$$$$$$$$$$$$$$")
        return is_valid