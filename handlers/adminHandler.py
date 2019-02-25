from flask import jsonify
from daos.admin import AdminDAO


class AdminHandler:
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
            return jsonify(Reply=mapped)

