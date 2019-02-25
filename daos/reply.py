class ReplyDAO:

    def __init__(self):
        R1 = [1, 1]
        R2 = [2, 2]
        R3 = [3, 3]
        R4 = [4, 4]

        self.replies = []
        self.replies.append(R1)
        self.replies.append(R2)
        self.replies.append(R3)
        self.replies.append(R4)

    def getAllReplies(self):
        return self.replies

    def getReplyById(self, id):
        for r in self.replies:
            if id == r[0]:
                return r
        return None

    def getReplyByUserId(self, userId):
        for row in self.replies:
            if userId == row[1]:
                return row
        return None
