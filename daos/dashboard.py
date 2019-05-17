import psycopg2
from sheepledb.dbconfig import pg_config


class DashboardDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getPostById(self, post_id):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply)  where P.post_id = %s order by post_id;"
        c.execute(query, (post_id,))
        result = c.fetchone()
        return result

    def getPopularHashtags(self):
        cursor = self.conn.cursor()
        query = "select hashtag_content, count(*) as count from hashashtag natural inner join hashtag group by hashtag_content order by count desc;"
        result = []
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        return result

    def getPostsPerDay(self):
        c = self.conn.cursor()
        query = "Select P.post_date, count(*) from Post as P group by P.post_date order by post_date;"
        c.execute(query)
        result = []
        for row in c:
            result.append(row)
        return result

    def getRepliesPerDay(self):
        c = self.conn.cursor()
        query = "Select P.post_date, count(*) from Post as P natural inner join isReply where reply = P.post_id group by P.post_date order by post_date;"
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

    def getUserWhoDislikesPost(self, post_id):
        c = self.conn.cursor()
        query = "select post_id, username from users natural inner join reacts where post_id = %s and reaction_type = 'dislike';"
        c.execute(query, (post_id,))
        result = []
        for row in c:
            result.append(row)
        return result

    def getReactionsPerDay(self, reaction_type):
        c = self.conn.cursor()
        query = "Select post_date, count(*) from Reacts inner join Post on post.post_id = reacts.post_id where reaction_type = %s group by post_date order by post_date;"
        c.execute(query, (reaction_type,))
        result = []
        for row in c:
            result.append(row)
        return result

    def mostActiveUsersPerDay(self):
        c = self.conn.cursor()
        query = "Select number_of_post.post_date, max(number_of_post.c) from (Select users.user_id, count(*) as c, post_date from Users inner join Post on post.user_id = users.user_id group by users.user_id, post_date) as number_of_post inner join Users on number_of_post.user_id = users.user_id group by post_date order by post_date;"
        c.execute(query)
        result = []
        for row in c:
            result.append(row)
        return result

    def getnumPostsByUserPerDay(self, user_id):
        c = self.conn.cursor()
        query = "Select post_date, count(*) as c from Users inner join Post on post.user_id = users.user_id where users.user_id = %s group by post.post_date;"
        c.execute(query, (user_id,))
        result = []
        for row in c:
            result.append(row)
        return result

    def getnumRepliesOfPost(self, post_id):
        c = self.conn.cursor()
        query = "Select post_id, count(*) from Post inner join isReply on post.post_id = isreply.original where post_id = %s group by post_id;"
        c.execute(query, (post_id,))
        result = []
        for row in c:
            result.append(row)
        return result

    def getNumOfReactions(self, post_id, reaction_type):
        c = self.conn.cursor()
        query = "select post_id, count(*) from Reacts where post_id = %s and reaction_type = %s group by post_id;"
        c.execute(query, (post_id, reaction_type, ))
        result = []
        for row in c:
            result.append(row)
        return result
