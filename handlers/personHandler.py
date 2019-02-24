from flask import jsonify


class PersonHandler:

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
        P1 = {}
        P1['person_id'] = 123
        P1['first_name'] = 'Maria'
        P1['last_name'] = 'Novoa'
        P1['gender'] = 'F'
        P1['email'] = 'mcnovoa@upr.com'
        P1['phone_number'] = '(787)787-7777'

        P2 = {}
        P2['person_id'] = 456
        P2['first_name'] = 'Jonathan'
        P2['last_name'] = 'Flechas'
        P2['gender'] = 'M'
        P2['email'] = 'jmflechas@upr.com'
        P2['phone_number'] = '(787)787-8888'

        P3 = {}
        P3['person_id'] = 789
        P3['first_name'] = 'Luis'
        P3['last_name'] = 'Rivera'
        P3['gender'] = 'M'
        P3['email'] = 'lmrivera@upr.com'
        P3['phone_number'] = '(787)787-7878'

        P4 = {}
        P4['person_id'] = 147
        P4['first_name'] = 'Manuel'
        P4['last_name'] = 'Rodriguez'
        P4['gender'] = 'M'
        P4['email'] = 'mrodriguez@upr.com'
        P4['phone_number'] = '(787)787-8787'

        person = []
        person.append(P1)
        person.append(P2)
        person.append(P3)
        person.append(P4)
        return person




