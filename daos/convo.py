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

