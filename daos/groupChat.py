from sheepledb.dbconfig import pg_config
import psycopg2


class groupChatDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)



    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = "select * from groupchat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllGroupChatByNames(self, gc_name):
        cursor = self.conn.cursor()
        query = "select * " \
                "from groupchat " \
                "where gc_name = %s;"
        cursor.execute(query, (gc_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupChatById(self, gc_id):
        cursor = self.conn.cursor()
        query = "select * from groupchat where gc_id = %s;"
        cursor.execute(query, (gc_id,))
        result = cursor.fetchone()
        return result

    def getGroupChatbyOwner(self, gc_id):
        cursor = self.conn.cursor()
        query = "select username, first_name,last_name from groupchat as G  inner join users as U on G.admin_id = U.user_id where gc_id = %s;"
        cursor.execute(query, (gc_id,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getGroupChatbyOwnerAndAdmin(self,gc_id, admin_id):
        cursor = self.conn.cursor()
        query = "select username, first_name,last_name from groupchat as G  inner join users as U on G.admin_id = U.user_id where gc_id = %s and admin_id = %s;"
        cursor.execute(query, (gc_id, admin_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersInGroupChat(self, gc_id):
        cursor = self.conn.cursor()
        query = "select user_id, username, first_name, last_name from groupchat natural inner join users natural inner join belongsto where gc_id = %s;"
        cursor.execute(query, (gc_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def postGroupChat(self, gc_name, admin_id):
        cursor = self.conn.cursor()
        query = "insert into groupchat(gc_name,admin_id) values(%s,%s) returning gc_id;"
        cursor.execute(query, (gc_name, admin_id,))

        gid = cursor.fetchone()[0]

        self.conn.commit()

        return gid

    def deleteGroupChat(self, gc_id):
        cursor = self.conn.cursor()
        query = "delete from groupchat where gc_id = %s returning gc_id;"
        cursor.execute(query, (gc_id,))
        self.conn.commit()

        gid = cursor.fetchone()[0]
        return gid

    def addUserToGroupChat(self, gc_id, user_id):
        cursor = self.conn.cursor()
        query = "insert into belongsto(gc_id, user_id) values(%s,%s) returning user_id;"

        cursor.execute(query, (gc_id, user_id,))
        user = cursor.fetchone()[0]
        self.conn.commit()
        return user

    def deleteUserFromGroupChat(self, gc_id, user_id):
        cursor = self.conn.cursor()
        query = "delete from belongsto where gc_id=%s AND user_id=%s returning user_id;"
        cursor.execute(query, (gc_id, user_id,))
        self.conn.commit()
        id = cursor.fetchone()[0]
        return id

    def getUserInChatById(self, gc_id, user_id):
        cursor = self.conn.cursor()
        query = "select U.user_id,U.username,U.first_name,U.last_name from belongsto natural inner join users as U where gc_id=%s AND user_id=%s"
        cursor.execute(query, (gc_id, user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def deleteAllUsersFromGroupChat(self, gc_id):
        cursor = self.conn.cursor()
        query ="delete from belongsto where gc_id=%s;"
        cursor.execute(query, (gc_id,))
        self.conn.commit()
        id = cursor.fetchone()[0]
        return id

    def deleteAllUsersFromGroupChat(self, gc_id):
        cursor = self.conn.cursor()
        query ="delete from belongsto where gc_id=%s;"
        cursor.execute(query, (gc_id,))
        self.conn.commit()

    def getGroupChatsForUser(self, user_id):
        cursor = self.conn.cursor()
        query = "select gc_name , gc_id from users natural inner join belongsto natural inner join groupchat where user_id = %s;"
        cursor.execute(query, (user_id, ))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getPostIdInGroupChat(self, gc_id):
        cursor = self.conn.cursor()
        query = "select post_id from post where gc_id = %s;"
        cursor.execute(query, (gc_id, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def deleteImagesByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = "delete from images where post_id = %s;"
        cursor.execute(query, (post_id,))
        self.conn.commit()

    def deleteHashtagByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = "delete from hashashtag where post_id = %s;"
        cursor.execute(query, (post_id,))
        self.conn.commit()

    def deleteReactionsByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = "delete from reacts where post_id = %s;"
        cursor.execute(query, (post_id,))
        self.conn.commit()

    def deletePostsInGroupChat(self, gc_id):
        cursor = self.conn.cursor()
        query = "delete from post where gc_id = %s;"
        cursor.execute(query, (gc_id,))
        self.conn.commit()

    def deleteRepliesByPostId(self, post_id):
        cursor = self.conn.cursor()
        query = 'delete from isreply where original = %s'
        cursor.execute(query, (post_id, ))
        self.conn.commit()


