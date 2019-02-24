from flask import jsonify


class convoHandler:
    def build_convo_dict(self, row):
        convo = {}
        convo['convo_id'] = row[0]
        convo['convo_users'] = row[1]
        convo['convo_userAmounts'] = row[2]
        convo['admin_id'] = row[3]

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
        convo_list = {}
        result_list= {}
        for row in convo_list:
            result = self.build_convo_dict(row)
            result_list.append(result)
        return jsonify(Parts=result_list)
