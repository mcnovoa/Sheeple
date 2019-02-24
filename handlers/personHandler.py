from flask import jsonify
from daos.person import PersonDAO


class personHandler:

    def build_person_dict(self, row):
        result = {}
        result['person_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['gender'] = row[3]
        result['email'] = row[4]
        result['phone_number'] = row[5]
        return result

    # def getAllPeople(self):
    #     P1 = {}
    #     P1['person_id'] = 123
    #     P1['first_name'] = 'Maria'
    #     P1['last_name'] = 'Novoa'
    #     P1['gender'] = 'F'
    #     P1['email'] = 'mcnovoa@upr.com'
    #     P1['phone_number'] = '(787)787-7777'
    #
    #     P2 = {}
    #     P2['person_id'] = 456
    #     P2['first_name'] = 'Jonathan'
    #     P2['last_name'] = 'Flechas'
    #     P2['gender'] = 'M'
    #     P2['email'] = 'jmflechas@upr.com'
    #     P2['phone_number'] = '(787)787-8888'
    #
    #     P3 = {}
    #     P3['person_id'] = 789
    #     P3['first_name'] = 'Luis'
    #     P3['last_name'] = 'Rivera'
    #     P3['gender'] = 'M'
    #     P3['email'] = 'lmrivera@upr.com'
    #     P3['phone_number'] = '(787)787-7878'
    #
    #     P4 = {}
    #     P4['person_id'] = 147
    #     P4['first_name'] = 'Manuel'
    #     P4['last_name'] = 'Rodriguez'
    #     P4['gender'] = 'M'
    #     P4['email'] = 'mrodriguez@upr.com'
    #     P4['phone_number'] = '(787)787-8787'
    #
    #     P5 = {}
    #     P5['person_id'] = 147
    #     P5['first_name'] = 'Luis'
    #     P5['last_name'] = 'Rivera'
    #     P5['gender'] = 'M'
    #     P5['email'] = 'larivera@upr.com'
    #     P5['phone_number'] = '(787)878-7878'
    #
    #     P6 = {}
    #     P6['person_id'] = 147
    #     P6['first_name'] = 'Thalia'
    #     P6['last_name'] = 'Rodriguez'
    #     P6['gender'] = 'F'
    #     P6['email'] = 'tmrodriguez@upr.com'
    #     P6['phone_number'] = '(787)123-4567'
    #
    #     person = []
    #     person.append(P1)
    #     person.append(P2)
    #     person.append(P3)
    #     person.append(P4)
    #     person.append(P5)
    #     person.append(P6)
    #     return person

    def getAllPeople(self):
        dao = PersonDAO()
        result = dao.getAllPeople()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)

    def getPersonByID(self, id):
        dao = PersonDAO()
        result = dao.getPersonByID(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.build_person_dict(result)

        return jsonify(Person = mapped_result)

    def getPeopleByName(self, args):
        name = args.get('name')
        dao = PersonDAO()
        result = dao.getPeopleByFirstName(name)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)

    def getAllPeopleByLastName(self, args):
        lastName = args.get('lastName')
        dao = PersonDAO()
        result = dao.getPeopleByLastName(lastName)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)

    def getAllPeopleByGender(self, args):
        gender = args.get('gender')
        dao = PersonDAO()
        result = dao.getPeopleByGender(gender)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)

    def getAllPeopleByEmail(self, args):
        email = args.get('email')
        dao = PersonDAO()
        result = dao.getPeopleByEmail(email)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)

    def getAllPeopleByPhoneNumber(self, args):
        number = args.get('number')
        dao = PersonDAO()
        result = dao.getPeopleByPhoneNumber(number)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.build_person_dict(result)

        return jsonify(Person=mapped_result)

    def searchPeople(self, args):
        dao = PersonDAO
        if args is 'first_Name':
            param = args.get('first_name')
            result = dao.getPeopleByFirstName(param)
        elif args is 'last_Name':
            param = args.get('last_name')
            result = dao.getPeopleByLastName(param)
        elif args is 'gender':
            param = args.get('gender')
            result = dao.getPeopleByGender(param)
        elif args is 'email':
            param = args.get('email')
            result = dao.getPeopleByEmail(param)
        elif args is 'phone_number':
            param = args.get('phone_number')
            result = dao.getPeopleByPhoneNumber(param)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)


