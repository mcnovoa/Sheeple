from daos.convo import ConvoDAO
from daos.user import UserDAO
from flask import Flask, jsonify, request

class convoHandler:
    def build_convo_dict(self, row):
        convo = {}
        convo['convo_id'] = row[0]
        convo['convo_users'] = row[1]
        convo['convo_userAmounts'] = row[2]
        convo['admin_id'] = row[3]

        return convo

    def build_post_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['post_content'] = row[1]
        p['post_date'] = row[2]
        p['user_id'] = row[3]
        p['convo_id'] = row[4]
        p['hashtag_id'] = row[5]
        p['reaction_id'] = row[6]
        p['reply_id'] = row[7]
        p['reaction_amount'] = row[8]
        p['reply_amount'] = row[9]

    def build_convo_attributes (convo_id, convo_users, convo_userAmounts, admin_id):
        convo = {}
        convo['convo_id'] = convo_id
        convo['convo_users'] = convo_users
        convo['convo_userAmounts'] = convo_userAmounts
        convo['admin_id'] = admin_id

    def getAllConvos(self):
        dao = ConvoDAO()
        convos = dao.getAllConvos()
        convomapped = []
        for c in convos:
            convomapped.append(self.build_convo_dict(c))

        return jsonify(Conversations=convomapped)

    def searchByArgs(self, args):
        dao = ConvoDAO()

        param1 = args.get('admin_id')
        param2 = args.get('convo_userAmounts')

        if param1:
            result = dao.searchByAdmin(param1)
        elif param2:
            result = dao.searchUserAmounts(param2)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for c in result:
            mapped_result.append(self.build_convo_dict(c))
        return jsonify(Conversations=mapped_result)

    def searchArgsById(self,convo_id, args):
        dao = ConvoDAO()

        param1 = args.get('admin_id')
        param2 = args.get('convo_userAmounts')

        if param1:
            result = dao.searchByAdmin(param1)
        elif param2:
            result = dao.getAllUsers()
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for c in result:
            mapped_result.append(self.build_convo_dict(c))
        return jsonify(Conversations=mapped_result)

    def getConvoById(self, convo_id):
        dao = ConvoDAO()
        rconvo = dao.getConvoById(convo_id)
        if rconvo == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            convomap = self.build_convo_dict(rconvo)

        return jsonify(Conversation=convomap)

    def updateConvo(self, convo_id, form):
        return self.getConvoById(convo_id), 200

    def deleteConvo(self, convo_id):
        return self.getConvoById(convo_id), 200

    def getAllConvoUsers(self, convo_id):
        daoc = ConvoDAO()
        daou = UserDAO()
        usr = daou.getAllUsers()
        result = []
        rconvo = daoc.getConvoById(convo_id)

        if rconvo == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for u in usr:
                if rconvo.__contains__(u):
                    result.append(u)
        return jsonify(Users=result)





