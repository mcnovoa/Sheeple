#import psycopg2

class ConvoDAO:
    def __init__(self):
        CV1 = [1, [], 0, 4]
        CV2 = [2, [], 0, 3]
        CV3 = [3, [], 0, 2]
        CV4 = [4, [], 0, 1]

        self.data = []
        self.data.append(CV1)
        self.data.append(CV2)
        self.data.append(CV3)
        self.data.append(CV4)


    def getAllConvos(self):
        return self.data


    def getConvoById(self, id):
        for c in self.data:
            if id == c[0]:
                return c
        return None


    def searchByAdmin(self, admin_id):
        result = []
        for ca in self.data:
            if admin_id == ca[3]:
                result.append(ca)
        return result

