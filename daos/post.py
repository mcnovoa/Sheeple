import psycopg2
from sheepledb.dbconfig import pg_config

class PostDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from Post;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPostById(self, post_id):
        cursor = self.conn.cursor()
        query = "select * from Post where post_id = %s;"
        cursor.execute(query, (post_id,))
        result = cursor.fetchone()
        return result

    def createPost(self, args):
        param1 = args.get('post_content')  # message, photo || both
        param2 = args.get('gc_id')
        param3 = args.get('user_id')
        param4 = args.get('post_date')



