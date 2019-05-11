import psycopg2
from sheepledb.dbconfig import pg_config


class PostDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertPost(self, post_content, post_date, image_url, user_id, gc_id):
        cursor = self.conn.cursor()
        fq = "select * from groupchat natural inner join users natural inner join belongsto where gc_id = %s and user_id = %s;"
        cursor.execute(fq, (gc_id, user_id,))
        bool = cursor.fetchone()
        if bool is not None:
            query = "insert into Post(post_content, post_date, image_url, user_id, gc_id) values (%s, %s, %s, %s, %s) returning post_id;"
            cursor.execute(query, (post_content, post_date, image_url, user_id, gc_id,))
            post_id = cursor.fetchone()[0]
            self.conn.commit()
            return post_id
        else:
            return None

    def insertReply(self, post_content, post_date, image_url, user_id, gc_id, original_post):
        cursor = self.conn.cursor()
        fq = "select * from groupchat natural inner join users natural inner join belongsto where gc_id = %s and user_id = %s;"
        cursor.execute(fq, (gc_id, user_id,))
        bool = cursor.fetchone()
        if bool is not None:
            query = "insert into Post(post_content, post_date, image_url, user_id, gc_id) values (%s, %s, %s, %s, %s) returning post_id;"
            cursor.execute(query, (post_content, post_date, image_url, user_id, gc_id,))
            post_id = cursor.fetchone()[0]
            rq = 'insert into isReply(original, reply) values (%s, %s);'
            cursor.execute(rq, (original_post, post_id,))
            self.conn.commit()
            return post_id
        else:
            return None

    def reactPost(self, reaction_type, post_id, user_id, gc_id):
        cursor = self.conn.cursor()
        fq = "select * from groupchat natural inner join users natural inner join belongsto where gc_id = %s and user_id = %s;"
        cursor.execute(fq, (gc_id, user_id,))
        bool = cursor.fetchone()
        ff = "select * from post where post_id = %s and gc_id = %s;"
        cursor.execute(ff, (post_id, gc_id,))
        boolf = cursor.fetchone()
        if bool is not None and boolf is not None:
            rq = "select reaction_type from reacts where post_id = %s and (reaction_type = 'like' or reaction_type = 'dislike') and user_id = %s;"
            cursor.execute(rq, (post_id, user_id,))
            p = cursor.fetchone()[0]
            if p is None:
                query = "insert into Reacts(reaction_type, post_id, user_id) values (%s, %s, %s);"
                cursor.execute(query, (reaction_type, post_id, user_id,))
                self.conn.commit()
                return 1
            else:
                if(reaction_type == 'like' and  p == 'like') or (reaction_type == 'dislike' and p == 'dislike'):
                    dq = "delete from reacts where reaction_type = %s and post_id = %s and user_id = %s;"
                    cursor.execute(dq, (reaction_type, post_id, user_id,))
                    self.conn.commit()
                    return -1
                else:
                    lastq = 'Update reacts set reaction_type = %s where user_id = %s and post_id = %s;'
                    cursor.execute(lastq, (reaction_type, user_id, post_id,))
                    self.conn.commit()
                    return 1
        else:
            return None

    def getAllPosts(self):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply) order by post_id;"
        c.execute(query)
        result = []
        for row in c:
            result.append(row)
        return result

    def getPostById(self, post_id):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply)  where P.post_id = %s order by post_id;"
        c.execute(query, (post_id,))
        result = c.fetchone()
        return result

    def getPostsByGC(self, gc_id):
        c = self.conn.cursor()
        query = "Select P.post_id, post_content, post_date, image_url, user_id, gc_id, original from (Post as P full outer join isReply as R on P.post_id = R.reply) where P.gc_id = %s order by post_id;"
        c.execute(query, (gc_id,))
        result = []
        for row in c:
            result.append(row)
        return result

    # def getPostsPerDay(self):
    #     c = self.conn.cursor()
    #     query = "Select P.post_date, count(*) from Post as P group by P.post_date order by post_date;"
    #     c.execute(query)
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getRepliesPerDay(self):
    #     c = self.conn.cursor()
    #     query = "Select P.post_date, count(*) from Post as P natural inner join isReply where reply = P.post_id group by P.post_date order by post_date;"
    #     c.execute(query)
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getUserWhoLikesPost(self, post_id):
    #     c = self.conn.cursor()
    #     query = "select post_id, username from users natural inner join reacts where post_id = %s and reaction_type = 'like';"
    #     c.execute(query, (post_id,))
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getUserWhoDislikesPost(self, post_id):
    #     c = self.conn.cursor()
    #     query = "select post_id, username from users natural inner join reacts where post_id = %s and reaction_type = 'dislike';"
    #     c.execute(query, (post_id,))
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getReactionsPerDay(self, reaction_type):
    #     c = self.conn.cursor()
    #     query = "Select post_date, count(*) from Reacts inner join Post on post.post_id = reacts.post_id where reaction_type = %s group by post_date order by post_date;"
    #     c.execute(query, (reaction_type,))
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def mostActiveUsersPerDay(self):
    #     c = self.conn.cursor()
    #     query = "Select number_of_post.post_date, max(number_of_post.c) from (Select users.user_id, count(*) as c, post_date from Users inner join Post on post.user_id = users.user_id group by users.user_id, post_date) as number_of_post inner join Users on number_of_post.user_id = users.user_id group by post_date order by post_date;"
    #     c.execute(query)
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getnumPostsByUserPerDay(self, user_id):
    #     c = self.conn.cursor()
    #     query = "Select post_date, count(*) as c from Users inner join Post on post.user_id = users.user_id where users.user_id = %s group by post.post_date;"
    #     c.execute(query, (user_id,))
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getnumRepliesOfPost(self, post_id):
    #     c = self.conn.cursor()
    #     query = "Select post_id, count(*) from Post inner join isReply on post.post_id = isreply.original where post_id = 5 group by post_id;"
    #     c.execute(query, (post_id,))
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
    #
    # def getNumOfReactions(self, post_id, reaction_type):
    #     c = self.conn.cursor()
    #     query = "select post_id, count(*) from Reacts where post_id = %s and reaction_type = %s group by post_id;"
    #     c.execute(query, (post_id, reaction_type, ))
    #     result = []
    #     for row in c:
    #         result.append(row)
    #     return result
