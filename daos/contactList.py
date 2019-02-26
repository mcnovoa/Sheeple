# import psycopg2


class contactListDAO:

    def __init__(self):
        P1 = [1, [], 56, 3]
        P2 = [2, [], 28, 6]
        P3 = [3, [], 199, 7]
        P4 = [4, [], 32, 8]

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

    def getAllContactLists(self):
        return self.data

    def getContactListByID(self, id):
        for r in self.data:
            if id == r[0]:
                return r

        return None

    def getContactListsByContacts(self, id):
        result = []
        for r in self.data:
            if id == r[1]:
                result.append(r)

        return r

    def getContactListsByUserAmount(self, amount):
        result = []
        for r in self.data:
            if int(amount) == r[2]:
                result.append(r)

        return result

    def getContactListByUserID(self, id):
        result = []
        for r in self.data:
            if int(id) == r[3]:
                result.append(r)

        return result
