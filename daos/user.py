import psycopg2
from sheepledb.dbconfig import pg_config
from daos.groupChat import groupChatDAO



class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "Select * from Users as U order by U.user_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByID(self, id):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.user_id = %s order by U.user_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.username=%s order by U.user_id;"
        cursor.execute(query, (username,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByPassword(self, password):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.password=%s order by U.user_id;"
        cursor.execute(query, (password,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByFirstName(self, name):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.first_name=%s order by U.user_id;"
        cursor.execute(query, (name,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByLastName(self, name):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.last_name=%s order by U.user_id;"
        cursor.execute(query, (name,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByGender(self, gender):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.gender=%s order by U.user_id"
        cursor.execute(query, (gender,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.email=%s order by U.user_id"
        cursor.execute(query, (email,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "Select * from Users as U where U.phone=%s order by U.user_id"
        cursor.execute(query, (phone,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByUsernameAndPassword(self, username, password):
        cursor = self.conn.cursor()
        query = "select * from Users as U where U.username = %s AND U.password = %s order by U.user_id;"
        cursor.execute(query, (username, password,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def insertUser(self, username, password, first_name, last_name, gender, email, phone):
        cursor = self.conn.cursor()
        query = "insert into Users(username, password, first_name, last_name, gender, email, phone)" \
                "values (%s, %s, %s, %s, %s, %s, %s) returning user_id;"
        cursor.execute(query, (username, password, first_name, last_name, gender, email, phone,))
        result = cursor.fetchone()
        query = "insert into contactlist (owner_id) values(%s);"
        cursor.execute(query, (result,))
        self.conn.commit()
        return result

    # def deleteUser(self, user_id):
    #     result = self.getUserByID(user_id)
    #     cursor = self.conn.cursor()
    #     query = "delete from IsPart where user_id = %s;"
    #     cursor.execute(query, (user_id,))
    #     query = "delete from contactlist where user_id = %s;"
    #     cursor.execute(query, (user_id,))
    #     query = "delete from Reacts where user_id = %s;"
    #     cursor.execute(query, (user_id,))
    #     query = "delete from BelongsTo where user_id = %s;"
    #     cursor.execute(query, (user_id,))
    #     # delete all from hashashtag (have to delete these references before posts)
    #     # delete all references from isreply of posts made by user
    #     # delete all references from posts made by user from all groupchats
    #     # delete all groupchats where the user is the owner (jonathan probably has a method for it done)
    #     query = "delete from Users where user_id = %s;"
    #     cursor.execute(query, (user_id,))
    #     self.conn.commit()
    #     return result
    #
    # def deletePostIDReferences
