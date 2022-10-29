from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data:dict):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# the view profile page wants the full name, creating a regular instance method to pull together the user's full name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for info in results:
            users.append(cls(info))
        return users

    @classmethod
    def new_user(cls, data:dict):
        query ="INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])



    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)


    # class method to delete user
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

