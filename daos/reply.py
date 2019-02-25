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

    def getReplyById(self, reply_id):
        for r in self.replies:
            if reply_id == r[0]:
                return r
        return None

    def getReplyByUserId(self, user_Id):
        result = []
        for row in self.replies:
            if int(user_Id) == row[1]:
                result.append(row)
        return result
