import psycopg2
from sheepledb.dbconfig import pg_config
class PostDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    def getAllPosts(self):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply) full outer join Images as I on P.post_id = I.post_id order by post_id;"
        c.execute(query)
        result = []
        for row in c:
            result.append(row)
        return result
    def getPostById(self, post_id):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply) full outer join Images as I on P.post_id = I.post_id where P.post_id = %s order by post_id;"
        c.execute(query, (post_id,))
        result = c.fetchone()
        return result
    def getNumOfReactions(self, post_id, reaction_type):
        c = self.conn.cursor()
        query = "select count(*) from Reacts where post_id = %s and reaction_type = %s;"
        c.execute(query, (post_id, reaction_type, ))
        result = c.fetchone()
        return result

    def getPostsByGC(self, gc_id):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply) full outer join Images as I on P.post_id = I.post_id where P.gc_id = %s order by post_id;"
        c.execute(query, (gc_id,))
        result = []
        for row in c:
            result.append(row)
        return result
    def getPostsByDay(self):
        c = self.conn.cursor()
        query = "Select P.post_date, count(*) from Post as P group by P.post_date;"
        c.execute(query)
        result = []
        for row in c:
            result.append(row)
        return result

    def getUserWhoLikesPost(self, post_id):
        c = self.conn.cursor()
        query = "select post_id, username from users natural inner join reacts where post_id = %s and reaction_type = 'like';"
        c.execute(query, (post_id,))
        result = []
        for row in c:
            result.append(row)

        return result


