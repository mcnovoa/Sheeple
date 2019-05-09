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
        result = dao.getFullContactListByOwnerId(owner_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_ByOwner_dict(r))
        if mapped_result is None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(ContactList=mapped_result)

    def postUserIntoContactList(self, owner_id, args):
        dao = contactListDAO()
        param3 = args.get('first_name')
        param4 = args.get('last_name')
        param6 = args.get('email')
        param7 = args.get('phone')
        if param3 and param4 and (param6 or param7) and owner_id:
            result = dao.insertUserIntoContactList(param3, param4, param6, param7, owner_id)
            return jsonify(AddedContact=result)
        else:
            return jsonify(Error="Invalid parameters. Please try again"), 404


    def deleteUserFromContactList(self, owner_id, args):
        dao = contactListDAO()
        param3 = args.get('first_name')
        param4 = args.get('last_name')
        param6 = args.get('email')
        param7 = args.get('phone')
        if param3 and param4 and (param6 or param7) and owner_id:
            result = dao.deleteUserIntoContactList(param3, param4, param6, param7, owner_id)
            return jsonify(DeletedContact=result)
        else:
            return jsonify(Error="Invalid parameters. Please try again"), 404



