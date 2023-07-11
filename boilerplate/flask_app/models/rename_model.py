from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex

db = 'Your database name'

class Rename(ie user):
    def __init__(self, data):
        #follow database table fields plus any other attribute you want to create
        # EXAMPLE: self.id = data['id']
        # self.first_name = data['first_name']
        # ETC
        #self.TABLE(ie user) = []
        pass


    @classmethod
    def rename(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            new_user = cls(user)
            users.append(new_user)
            return users
        #Nice little head start
        #Rest of code here
        print(results[some_number]['some_key'(ie first_name)])
        return "Something here"