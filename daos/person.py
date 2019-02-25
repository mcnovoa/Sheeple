#import psycopg2


class PersonDAO:

    def __init__(self):
        P1 = [1, 'Maria', 'Novoa', 'F', 'mcnovoa@upr.com', '(787)787-7777']
        P2 = [2, 'Jonathan', 'Flechas', 'M', 'jmflechas@upr.com', '(787)787-8888']
        P3 = [3, 'Luis', 'Rivera', 'M', 'lmrivera@upr.com', '(787)787-7878']
        P4 = [4, 'Manuel', 'Rodriguez', 'M', 'mrodriguez@upr.com', '(787)787-8787']
        P5 = [5, 'Luis', 'Rivera', 'M', 'larivera@upr.com', '(787)878-7878']
        P6 = [6, 'Thalia', 'Rodriguez', 'F', 'tmrodriguez@upr.com', '(787)123-4567']

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)
        self.data.append(P6)


    def getAllPeople(self):
        return self.data

    def getPersonByID(self, id):
        for r in self.data:
            if id.__eq__(r[0]):
                return r

        return None

    def getPeopleByFirstName(self, name):
        result = []
        for r in self.data:
            if name == r[1]:
                result.append(r)

        return result

    def getPeopleByLastName(self, lastName):
        result = []
        for r in self.data:
            if lastName.__eq__(r[2]):
                result.append(r)

        return result

    def getPeopleByGender(self, gender):
        result = []
        for r in self.data:
            if gender.__eq__(r[3]):
                result.append(r)

        return result

    def getPeopleByEmail(self, email):
        result = []
        for r in self.data:
            if email.__eq__(r[4]):
                result.append(r)

        return result

    def getPeopleByPhoneNumber(self, number):
        result = []
        for r in self.data:
            if number.__eq__(r[5]):
                return r

        return None


