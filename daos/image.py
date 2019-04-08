import psycopg2
from sheepledb.dbconfig import pg_config

class ImageDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        pg_config['user'], pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllImages(self):
        c = self.conn.cursor()
        query = "select * from Post as P, Images as I where P.post_id = I.post_id;"
        c.execute(query)
        result = []
        for row in c:
            result.append(row)
        return result

    def getImagesById(self, image_id):
        c = self.conn.cursor()
        query = "select * from Post as P, Images as I where P.post_id = I.post_id and I.image_id = %s;"
        c.execute(query, (image_id,))
        result = c.fetchone()
        return result
