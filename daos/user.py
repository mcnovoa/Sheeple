import psycopg2

from sheepledb.dbConfig import pg_config


class UserDAO:
    def __init__(self):
        # P1 = [1, 'mcnovoa', 'minix']
        # P2 = [2, 'Zernin', 'JoJo']
        # P3 = [3, 'lm013', 'dameUnaA']
        # P4 = [4, 'manuelr417', 'ronYWhiskey']
        # P5 = [5, 'queSeYo', 'adidas']
        # P6 = [6, 'thamarie', 'badbunny']
        #
        # self.data = []
        # self.data.append(P1)
        # self.data.append(P2)
        # self.data.append(P3)
        # self.data.append(P4)
        # self.data.append(P5)
        # self.data.append(P6)
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
    self.conn = psycopg2._connect(connection_url)


    def getAllUsers(self):
        return self.data

    def getUserByID(self, id):
        for r in self.data:
            if id.__eq__(r[0]):
                return r

        return None

    def getUserByUsername(self, username):
        result = []
        for r in self.data:
            if username == r[1]:
                result.append(r)

        return result

    def getUserByPassword(self, password):
        result = []
        for r in self.data:
            if password.__eq__(r[2]):
                result.append(r)

        return result

