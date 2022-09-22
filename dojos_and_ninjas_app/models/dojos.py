from dojos_and_ninjas_app.models import ninjas
from dojos_and_ninjas_app.conf.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        schools = connectToMySQL('dojo_ninja_schemas').query_db(query)
        halls = []
        for classes in schools:
            halls.append( cls(classes) )
        return halls
    
    @classmethod
    def get_one_dojo(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninja_schemas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninjas_students = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id' : row['dojo_id']
            }
            dojo.ninjas.append( ninjas.Ninja(ninjas_students) )
        return dojo
    
    @classmethod
    def save(cls, data ):
        query = """INSERT INTO dojos ( name , created_at, updated_at )
        VALUES ( %(name)s, NOW() , NOW() )
        ;"""

        return connectToMySQL('dojo_ninja_schemas').query_db( query, data )

