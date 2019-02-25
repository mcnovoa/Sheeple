from flask import jsonify
from daos.contact import ContactDAO


class ContactHandler:

    def build_contact_dict(self, row):
        result = {}
        result['contact_id'] = row[0]
        result['contact_name'] = row[1]
        return result

    def getAllContacts(self):
        dao = ContactDAO()
        result = dao.getAllContacts()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contact_dict(r))

        return jsonify(User=mapped_result)

    def getContactById(self, id):
        dao = ContactDAO()
        result = dao.getContactByID(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.build_contact_dict(result)

        return jsonify(Contact=mapped_result)

    def searchContacts(self, args):
        dao = ContactDAO()
        param1 = args.get('contact_name')
        result = dao.getContactsByContactName(param1)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contact_dict(r))

        return jsonify(Contact=mapped_result)

    def postContact(self):
        return jsonify(CreateContact="CREATED"), 201

    def updateContact(self):
        return jsonify(UpdateContact="OK"), 200

    def deleteContact(self):
        return jsonify(DeleteContact="OK"), 200
