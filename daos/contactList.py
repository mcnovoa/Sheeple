import psycopg2
from sheepledb.dbconfig import pg_config


class contactListDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllContactLists(self):
        cursor = self.conn.cursor()
        query = "select cl_id, owner_id from ContactList;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactListByID(self, id):
        cursor = self.conn.cursor()
        query = "select cl_id, owner_id from ContactList where cl_id=%s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getContactListsByOwnerId(self, id):
        cursor = self.conn.cursor()
        query = "select cl_id, owner_id from ContactList where owner_id=%s;"
        cursor.execute(query, (id,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUsersFromContactList(self, id):
        cursor = self.conn.cursor()
        query = "Select * from IsPart as I inner join (Users as U)using (user_id) where cl_id = %s order by U.user_id;"
        cursor.execute(query, (id,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserFromContactListById(self, cl_id, user_id):
        cursor = self.conn.cursor()
        query = "Select * from IsPart as I inner join (Users as U) using(user_id) where cl_id = %s and user_id=%s order by U.user_id;"
        cursor.execute(query, (cl_id, user_id,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getFullContactListByOwnerId(self, owner_id):
        cursor = self.conn.cursor()
        query = "Select U.user_id, C.cl_id, U.username, U.first_name, U.last_name, U.email, U.phone from ContactList as C natural inner join Users as U natural inner join IsPart as I where C.owner_id=%s"
        cursor.execute(query, (owner_id,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def insertUserIntoContactList(self, first_name, last_name, email, phone, owner_id):
        cursor = self.conn.cursor()
        query = "select user_id from users where first_name=%s and last_name=%s and (email=%s or phone=%s);"
        cursor.execute(query, (first_name, last_name, email, phone,))
        user_id = cursor.fetchone()
        query = "select cl_id from ContactList where owner_id = %s;"
        cursor.execute(query, (owner_id,))
        cl_id = cursor.fetchone()
        query = "select user_id from IsPart where cl_id = %s AND user_id = %s;"
        cursor.execute(query, (cl_id, user_id,))
        copy_id = cursor.fetchone()
        if not copy_id:
            query = "insert into IsPart (cl_id, user_id) values(%s, %s) returning *;"
            cursor.execute(query, (cl_id, user_id,))
            result = cursor.fetchone()
            self.conn.commit()
            return [result, cl_id, user_id]
        else:
            return ['User already in contact list', cl_id, user_id]

    def deleteUserIntoContactList(self, first_name, last_name, email, phone, owner_id):
        cursor = self.conn.cursor()
        query = "select user_id from users where first_name=%s and last_name=%s and (email=%s or phone=%s);"
        cursor.execute(query, (first_name, last_name, email, phone,))
        user_id = cursor.fetchone()[0]
        query = "select cl_id from ContactList where owner_id = %s;"
        cursor.execute(query, (owner_id,))
        cl_id = cursor.fetchone()
        if user_id:
            query = "delete from IsPart where user_id=%s;"
            cursor.execute(query, (user_id,))
            self.conn.commit()
            return [cl_id, user_id]
        else:
            return ['User not in contact list', cl_id, user_id]



