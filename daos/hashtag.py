class hashtagDAO:

    def __init__ (self):
        H1 = [1,"#yasssss" ]
        H2 = [2, "#queeeeen"]
        H3 = [3, "#slaaaay"]
        H4 = [4, "#metoo"]

        self.hashtags = []
        self.hashtags.append(H1)
        self.hashtags.append(H2)
        self.hashtags.append(H3)
        self.hashtags.append(H4)

    def getAllHashtags(self):
        return self.hashtags

    def getHashtagById(self, id):
        for row in self.hashtags:
            if id == row[0]:
                return row

    def getHashtagbyContent(self, content):
        for row in self.hashtags:
            if content == row[1]:
                return row


