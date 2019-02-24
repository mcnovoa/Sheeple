from flask import jsonify


class AdminHandler:
    def build_admin_dict(row,self):
            admin = {}
            result['admin_id'] = row[0]
