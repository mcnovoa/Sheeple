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

    def searchPeople(self, args):
        dao = PersonDAO()
        param1 = args.get('first_name')
        param2 = args.get('last_name')
        param3 = args.get('gender')
        param4 = args.get('email')
        param5 = args.get('phone_number')

        if param1:
            result = dao.getPeopleByFirstName(param1)
        elif param2:
                result = dao.getPeopleByLastName(param2)
        elif param3:
            result = dao.getPeopleByGender(param3)
        elif param4:
                result = dao.getPeopleByEmail(param4)
        elif param5:
            result = dao.getPeopleByPhoneNumber(param5)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_person_dict(r))

        return jsonify(Person=mapped_result)


    def postPerson(self):
        return jsonify(CreatePerson="CREATED"), 201

    def updatePerson(self):
        return jsonify(UpdatePerson = "OK"), 200

    def deletePerson(self):
        return jsonify(DeletePerson = "OK"), 200
