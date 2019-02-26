from flask import jsonify
from daos.admin import AdminDAO


class adminHandler:
    def build_admin_dict(self, row):
            admin = {}
            admin['admin_id'] = row[0]

            return admin

    def getAllAdmins(self):
        dao = AdminDAO()
        admins = dao.getAllAdmins()
        mapped_admins = []
        for row in admins:
            mapped_admins.append(self.build_admin_dict(row))
        return jsonify(Reply=mapped_admins)

    def getAdminById(self, id):
        dao = AdminDAO()
        admin = dao.getAdminById(id)
        if admin is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_admin_dict(admin)
            return jsonify(Admini=mapped)

    def searchAdmins(self, args):
        param1 = args.get('admin_id')
        dao = AdminDAO()

        if param1:
            admins = dao.getAdminById(int(param1))
        else:
            return jsonify(Admin="NOT FOUND"), 404

        admin_list = []
        for row in admins:
            admin_list.append(self.build_admin_dict())
        return jsonify(Admin=admin_list)

    def postAdmin(self):
        return jsonify(CreateAdmin="CREATED"), 201

    def updateAdmin(self):
        return jsonify(UpdateAdmin="OK"), 200

    def deleteAdmin(self):
        return jsonify(DeleteAdmin="OK"), 200
