#import psycopg2
from daos.user import UserDAO


class ConvoDAO:
    def __init__(self):
        daou = UserDAO().getAllUsers()

        CV1 = [1, daou, len(daou), 4, 'Los Ganchos de Black']
        CV2 = [2, [], 0, 3, 'Don Q Coco']
        CV3 = [3, [], 0, 2, 'SweetPineapple']
        CV4 = [4, [], 0, 1, 'Los Medalleros']

        self.data = []
        self.data.append(CV1)
        self.data.append(CV2)
        self.data.append(CV3)
        self.data.append(CV4)


    def getAllConvos(self):
        return self.data

    def getAllConvoAmount(self, param2):
        result = []
        for c in self.data:
            if int(param2) == c[2]:
                result.append(c)
        return result

    def getAllConvoNames(self, param3):
        result = []
        for c in self.data:
            if param3 == c[4]:
                result.append(c)
        return result

    def getConvoById(self, convo_id):
        for c in self.data:
            if int(convo_id) == c[0]:
                return c
        return None

    def searchByAdmin(self, admin_id):
        result = []
        for c in self.data:
            if int(admin_id) == c[3]:
                result.append(c)
        return result

    def searchUserAmounts(self, convo_userAmounts):
        result = []
        for c in self.data:
            if int(convo_userAmounts) == c[2]:
                result.append(c)
        return result

