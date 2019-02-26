#import psycopg2
from daos.user import UserDAO


class PostDAO:
    def __init__(self):
    #An image_id = -1 means there's no image in the message
        P1 = [1, 'Dudas, inquietudes, temores, sin sabores', '08/17/2018', 0, 4, 0, 4, 0, 2, 3]
        P2 = [2, 'Manuel, por favor, danos la A', '02/25/2019', 1, 3,  4, 3, 1, 2, 0]
        P3 = [3, 'Viva Puerto Rico Libre', '01/22/2019', 2, 2, 2, 2, 2, 0, 1]
        P4 = [4, 'Pero con ciudadania americana', '01/22/2019', 3,  2, 3, 1, 3, 4, 6]
        P5 = [5, 'Ya que son unas bestias de icom 5016', '02/12/2019', 4, 0, 4, 0, 3, 2, 6]

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)


    def getAllPosts(self):
        return self.data

    def getPostById(self, post_id):
        for p in self.data:
            if int(post_id) == p[0]:
                return p
        return None

    def getPostContent(self, param1):
        result = []
        for p in self.data:
            if param1 == p[1]:
                result.append(p)
        return result

    def getPostDate(self, param2):
        result = []
        for p in self.data:
            if param2 == p[2]:
                result.append(p)
        return result

    def getPostUser(self, param3):
        result = []
        for p in self.data:
            if int(param3) == p[3]:
                result.append(p)
        return result


    def getPostConvo(self, param4):
        result = []
        for p in self.data:
            if int(param4) == p[4]:
                result.append(p)
        return result

    def getPostHashtag(self, param5):
        result = []
        for p in self.data:
            if int(param5) == p[5]:
                result.append(p)
        return result

    def getPostReactions(self, param6):
        result = []
        for p in self.data:
            if int(param6) == p[6]:
                result.append(p)
        return result

    def getPostReplies(self, param7):
        result = []
        for p in self.data:
            if int(param7) == p[7]:
                result.append(p)
        return result

    def getPostReactionAmount(self, param8):
        result = []
        for p in self.data:
            if int(param8) == p[8]:
                result.append(p)
        return result

    def getPostRepliesAmount(self, param9):
        result = []
        for p in self.data:
            if int(param9) == p[9]:
                result.append(p)
        return result


