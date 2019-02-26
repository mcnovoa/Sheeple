class AdminDAO:
    def __init__(self):
        A1 = [1]
        A2 = [2]
        A3 = [3]

        self.data = []
        self.data.append(A1)
        self.data.append(A2)
        self.data.append(A3)

    def getAllAdmins(self):
        return self.data

    def getAdminById(self, id):
        for row in self.data:
            if id == row[0]:
                return row
        return None


