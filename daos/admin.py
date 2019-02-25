class AdminDAO:
    def __init__(self):
        A1 = [1]
        A2 = [2]
        A3 = [3]

        self.admins = []
        self.admins.append(A1)
        self.admins.append(A2)
        self.admins.append(A3)


    def getAllAdmins(self):
        return self.admins

    def getAdminById(self, id):
        for row in self.admins:
            if int(id) == row[0]:
                return row
        return None


