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

    def getAllHashtagContent(self):
        cursor = self.conn.cursor()
        query = "select hashtag_content from hashtag;"
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
        query = "select * from hashtag where content=%s;"
        result = []
        cursor.execute(query, (content,))

        for row in cursor:
            result.append(row)
        return result

    def getPopularHashtags(self):
        cursor = self.conn.cursor()
        query = "select hashtag_content, count(*) as count from hashashtag natural inner join hashtag group by hashtag_content order by count desc;"
        result = []
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        return result

    def postHashtag(self, content):
        cursor = self.conn.cursor()
        query = "insert into Hashtag(hashtag_content) values(%s)"
        cursor.execute(query, (content,))

        self.conn.commit()

