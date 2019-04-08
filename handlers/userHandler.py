from flask import jsonify

from daos.user import UserDAO


class userHandler:

    def build_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['username'] = row[1]
        result['password'] = row[2]
        result['first_name'] = row[3]
        result['last_name'] = row[4]
        result['gender'] = row[5]
        result['email'] = row[6]
        result['phone'] = row[8]
        return result

    def build_user_attributes(self, user_id, username, password, first_name, last_name, gender, email, phone):
        result = {}
        result['user_id'] = user_id
        result['username'] = username
        result['password'] = password
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['gender'] = gender
        result['email'] = email
        result['phone'] = phone
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))

        return jsonify(User=mapped_result)

    def getUserByID(self, id):
        dao = UserDAO()
        result = dao.getUserByID(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.build_user_dict(result)

        return jsonify(User=mapped_result)

    def searchUsers(self, args):
        dao = UserDAO()
        param1 = args.get('username')
        param2 = args.get('password')
        param3 = args.get('first_name')
        param4 = args.get('last_name')
        param5 = args.get('gender')
        param6 = args.get('email')
        param7 = args.get('phone')

        if param1:
            result = dao.getUserByUsername(param1)
        elif param2:
            result = dao.getUserByPassword(param2)
        elif param3:
            result = dao.getUserByFirstName(param3)
        elif param4:
            result = dao.getUserByLastName(param4)
        elif param5:
            result = dao.getUserByGender(param5)
        elif param6:
            result = dao.getUserByEmail(param6)
        elif param7:
            result = dao.getUserByPhone(param7)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))

        return jsonify(User=mapped_result)

    def createUser(self, args):
        param0 = args.get('user_id')
        param1 = args.get('username')
        param2 = args.get('password')
        param3 = args.get('first_name')
        param4 = args.get('last_name')
        param5 = args.get('gender')
        param6 = args.get('email')
        param7 = args.get('phone')

        if param0 and param1 and param2 and param3 and param4 and param5 and param6 and param7:
            result = self.build_user_attributes(param0, param1, param2, param3, param4, param5, param6, param7)
            return jsonify(CreateStatus=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUser(self, user_id, args):
        dao = UserDAO()
        if dao.getUserByID(user_id):
            param0 = args.get('user_id')
            param1 = args.get('username')
            param2 = args.get('password')
            param3 = args.get('first_name')
            param4 = args.get('last_name')
            param5 = args.get('gender')
            param6 = args.get('email')
            param7 = args.get('phone')

            if param0 != user_id:
                return jsonify(Error="User_id does not match"), 400
            elif param0 and param1 and param2 and param3 and param4 and param5 and param6 and param7:
                result = self.build_user_attributes(param0, param1, param2, param3, param4, param5, param6, param7)
                return jsonify(UpdateStatus=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
            return jsonify(UpdateStatus="OK"), 200
        else:
            return jsonify(Error="User not found."), 404


    def deleteUser(self, user_id):
        dao = UserDAO()
        if not dao.getUserByID(user_id):
            return jsonify(Error="User not found."), 404
        else:
            result = dao.getUserByID(user_id)

        return jsonify(DeleteStatus=result), 200

    def getUserByUsernameAndPassword(self, args):
        dao = UserDAO()
        username = args.get('username')
        password = args.get('password')
        result = dao.getUserByUsernameAndPassword(username, password)
        if not result:
            return jsonify(Error="Incorrect username or password. Please try again"), 400
        else:
            return jsonify(Succesful = self.build_user_dict(result)), 200
