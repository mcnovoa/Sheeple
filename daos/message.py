#import psycopg2
from daos.user import UserDAO


class MessageDAO:
    def __init__(self):
    #An image_id = -1 means there's no image in the message
        M1 = [1, 0]
        M2 = [2, 3]
        M3 = [3, 2]
        M4 = [4, 1]
        M5 = [5, 0]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)


    def getAllMessages(self):
        return self.data

    def getMessageById(self, message_id):
        for m in self.data:
            if int(message_id) == m[0]:
                return m
        return None

    def searchByImageId(self, image_id):
        result = []
        for m in self.data:
            if int(image_id) == m[1]:
                result.append(m)
        return result

    def searchMessagesSameImage(self, image_id):
        result = []
        for m in self.data:
            if int(image_id) == m[1]:
                result.append(m)
        return result

