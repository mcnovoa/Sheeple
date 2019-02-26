# import psycopg2



class ContactDAO:
    def __init__(self):
        P1 = [6, 'mcnovoa']
        P2 = [5, 'Zernin']
        P3 = [4, 'lm013']
        P4 = [3, 'manuelr417']
        P5 = [2, 'queSeYo']
        P6 = [1, 'thamarie']

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)
        self.data.append(P6)


    def getAllContacts(self):
        return self.data

    def getContactByID(self, id):
        for r in self.data:
            if id == r[0]:
                return r

        return None

    def getContactsByContactName(self, contact_name):
        result = []
        for r in self.data:
            if contact_name.__eq__(r[1]):
                result.append(r)

        return result
