from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.conf.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
    @classmethod
    def save(cls, data ):
        query = """INSERT INTO ninjas ( first_name , last_name , age , dojo_id)
        VALUES ( %(f_name)s , %(l_name)s , %(age)s , %(name)s)
        ;"""
        return connectToMySQL('dojo_ninja_schemas').query_db( query, data )
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL('dojo_ninja_schemas').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def edit(cls, data):
        query = """UPDATE ninjas 
        SET first_name=%(f_name)s,last_name=%(l_name)s, age=%(age)s, dojo_id=%(dojo_id)s
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL('dojo_ninja_schemas').query_db(query, data)
        print("results", results)
        return results
    
    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojo_ninja_schemas').query_db(query,data)