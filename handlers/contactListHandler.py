from flask import jsonify

from daos.contactList import contactListDAO


class contactListHandler:

    def build_contactList_ByUsers_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['cl_id'] = row[1]
        result['username'] = row[2]
        result['first_name'] = row[4]
        result['last_name'] = row[5]
        result['email'] = row[7]
        result['phone'] = row[9]
        return result

    def build_contactList_ByAttribute_dict(self, uid, cl_id, username, fname, lname, email, phone):
        result = {}
        result['user_id'] = uid
        result['cl_id'] = cl_id
        result['username'] = username
        result['first_name'] = fname
        result['last_name'] = lname
        result['email'] = email
        result['phone'] = phone
        return result

    def build_contactList_ByOwner_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['cl_id'] = row[1]
        result['username'] = row[2]
        result['first_name'] = row[3]
        result['last_name'] = row[4]
        result['email'] = row[5]
        result['phone'] = row[6]
        return result

    def build_contactList_dict(self, row):
        result = {}
        result['cl_id'] = row[0]
        result['owner_id'] = row[1]
        return result

    def build_user_attributes(self, cl_id, owner_id):
        result = {}
        result['cl_id'] = cl_id
        result['owner_id'] = owner_id
        return result

    def getAllContactLists(self):
        dao = contactListDAO()
        result = dao.getAllContactLists()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_dict(r))

        return jsonify(ContactList=mapped_result)

    def getContactListByID(self, id):
        dao = contactListDAO()
        result = dao.getContactListByID(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.build_contactList_dict(result)

        return jsonify(ContactList=mapped_result)

    def searchContactLists(self, args):
        dao = contactListDAO()
        param1 = args.get('owner_id')

        if param1:
            result = dao.getContactListsByOwnerId(param1)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_dict(r))
        if result is None:
            return jsonify(Error="NOT FOUND"), 404

        return jsonify(ContactList=mapped_result)

    def postContactList(self, args):
        param0 = args.get('cl_id')
        param1 = args.get('owner_id')

        if param0 and param1:
            result = self.build_user_attributes(param0, param1)
            return jsonify(CreateStatus=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    # def updateContactList(self, cl_id, args):
    #     param0 = args.get('cl_id')
    #     param1 = args.get('owner_id')
    #     if param0 and param1:
    #         result = self.build_user_attributes(param0, param1)
    #         return jsonify(UpdateStatus=result), 201
    #     else:
    #         return jsonify(Error="Unexpected attributes in post request"), 400
    #
    # def deleteContactList(self, cl_id):
    #     dao = contactListDAO()
    #     if not dao.getContactListByID(cl_id):
    #         return jsonify(Error="User not found."), 404
    #     else:
    #         result = dao.getContactListByID(cl_id)
    #     return jsonify(DeleteStatus=result), 200

    def getUserFromContactList(self, cl_id):
        dao = contactListDAO()
        result = dao.getUsersFromContactList(cl_id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_ByUsers_dict(r))
        return jsonify(ContactList=mapped_result)

    def getContactListByOwnerId(self, owner_id):
        dao = contactListDAO()
        result = dao.getContactListByOwnerId(owner_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_ByOwner_dict(r))
        if mapped_result is None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(ContactList=mapped_result)

    def postUserIntoContactList(self, cl_id, args):
        param0 = args.get('user_id')
        param1 = args.get('username')
        param3 = args.get('first_name')
        param4 = args.get('last_name')
        param6 = args.get('email')
        param7 = args.get('phone')
        if param0 and param1 and param3 and param4 and param6 and param7 and cl_id:
            result = self.build_contactList_ByAttribute_dict(param0, cl_id, param1, param3, param4, param6, param7)
        if result is None:
            return jsonify(Error="User not added"), 404
        # mapped_result = []
        # for r in result:
        #     mapped_result.append(self.build_contactList_ByUsers_dict(r))
        return jsonify(AddedContact=result)

    def deleteUserFromContactList(self, cl_id, args):
        dao = contactListDAO()
        user_id = args.get('user_id')
        result = dao.getUserFromContactListById(cl_id, user_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_ByUsers_dict(r))
        if mapped_result is None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(DeletedContact=mapped_result)



