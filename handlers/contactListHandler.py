from flask import jsonify
from daos.contactList import contactListDAO


class contactListHandler:

    def build_contactList_dict(self, row):
        result = {}
        result['contact_List_id'] = row[0]
        result['contacts'] = row[1]
        result['contact_amount'] = row[2]
        result['owner_id'] = row[3]
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
        param1 = args.get('contacts')
        param2 = args.get('contact_amount')
        param3 = args.get('user_id')

        if param1:
            result = dao.getContactListsByContacts(param1)
        elif param2:
                result = dao.getContactListsByUserAmount(param2)
        elif param3:
            result = dao.getContactListByUserID(param3)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contactList_dict(r))

        return jsonify(ContactList=mapped_result)

    def postContactList(self):
        return jsonify(CreateContactList="CREATED"), 201

    def updateContactList(self):
        return jsonify(UpdateContactList="OK"), 200

    def deleteContactList(self):
        return jsonify(DeleteContactList="OK"), 200
