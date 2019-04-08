import psycopg2
from sheepledb.dbconfig import pg_config


class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P order by U.user_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByID(self, id):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.user_id = %s order by U.user_id;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.username=%s order by U.user_id;"
        cursor.execute(query, (username,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByPassword(self, password):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.password=%s order by U.user_id;"
        cursor.execute(query, (password,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByFirstName(self, name):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.first_name=%s order by U.user_id;"
        cursor.execute(query, (name,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByLastName(self, name):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.last_name=%s order by U.user_id;"
        cursor.execute(query, (name,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByGender(self, gender):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.gender=%s order by U.user_id"
        cursor.execute(query, (gender,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByEmail(self, email):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where U.email=%s order by U.user_id"
        cursor.execute(query, (email,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "Select * from Users as U natural inner join PhoneNumber as P where P.phone=%s order by U.user_id"
        cursor.execute(query, (phone,))
        result = []
        for r in cursor:
            result.append(r)
        return result

    def getUserByUsernameAndPassword(self, username, password):
        cursor = self.conn.cursor()
        query = "select * from Users as U natural inner join PhoneNumber as P where U.username = %s AND U.password = %s order by U.user_id;"
        cursor.execute(query, (username, password,))
        result = cursor.fetchone()
        if not result:
            return None
        return result


#more methods need to be added due to routes.
