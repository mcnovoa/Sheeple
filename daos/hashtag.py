#from sheepledb.dbConfig import pg_config
from sheepledb.dbconfig import pg_config
import psycopg2


class hashtagDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtag;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagById(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select * from hashtag where hashtag_id=%s;"
        cursor.execute(query, (hashtag_id,))

        result = cursor.fetchone()
        return result;

    def getHashtagByContent(self, content):
        cursor = self.conn.cursor()
        query = "select * from hashtag where hashtag_content=%s;"
        result = []
        cursor.execute(query, (content,))
        for row in cursor:
            result.append(row)
        return result

    def postHashtag(self, hashtag_content):
        cursor = self.conn.cursor()
        query = "insert into hashtag(hashtag_content) values(%s) returning hashtag_id;"
        cursor.execute(query, (hashtag_content, ))
        hid = cursor.fetchone()[0]
        self.conn.commit()
        return hid

    def insertIntoHasHashtag(self, hashtag_id, post_id):
        cursor = self.conn.cursor()
        query = "insert into hashashtag(hashtag_id, post_id) values(%s, %s);"
        cursor.execute(query, (hashtag_id, post_id, ))
        self.conn.commit()

    def getHashtagIdByContent(self, hashtag_content):
        cursor = self.conn.cursor()
        query = "select hashtag_id from hashtag where hashtag_content=%s;"
        cursor.execute(query, (hashtag_content,))
        result = []
        for row in cursor:
            result.append(row)
        return result


