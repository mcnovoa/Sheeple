from flask import jsonify
from daos.convo import ConvoDAO


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

        return jsonify(Convos=convomapped)


        def getConvoById(self, id):
            dao = ConvoDAO()
            convo = dao.getConvoById(self,id)
            if convo == None:
                return jsonify(Error="NOT FOUND"), 404
            else:
                convomap = self.build_convo_dict(convo)

        return jsonify(Convo=convomap)
