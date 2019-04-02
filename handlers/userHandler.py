from flask import jsonify

from daos.user import UserDAO


class userHandler:

    def build_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['username'] = row[1]
        result['password'] = row[2]
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

        if param1:
            result = dao.getUserByUsername(param1)
        elif param2:
                result = dao.getUserByPassword(param2)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))

        return jsonify(User=mapped_result)


    def postUser(self):
        return jsonify(CreateUser="CREATED"), 201

    def updateUser(self):
        return jsonify(UpdateUser="OK"), 200

    def deleteUser(self):
        return jsonify(DeleteUser="OK"), 200
