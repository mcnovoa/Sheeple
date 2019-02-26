class ReactionDAO:

    def __init__(self):
        R1 = [1, "like", 1]
        R2 = [2, "like", 2]
        R3 = [3, "angry", 3]

        self.reactions = []
        self.reactions.append(R1)
        self.reactions.append(R2)
        self.reactions.append(R3)

    def getAllReactions(self):
        return self.reactions

    def getReactionById(self, id):
        for row in self.reactions:
            if id == row[0]:
                return row

    def getReactionByType(self, type):
        result = []
        for row in self.reactions:
            if type == row[1]:
                result.append(row)
        return result

    def getReactionbyUserId(self, userId):
        result = []
        for row in self.reactions:
            if int(userId) == row[2]:
                result.append(row)



