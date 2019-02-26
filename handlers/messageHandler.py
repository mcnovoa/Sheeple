from daos.message import MessageDAO
from daos.user import UserDAO
from flask import Flask, jsonify, request

class messageHandler:
    def build_message_dict(self, row):
        message = {}
        message['message_id'] = row[0]
        message['image_id'] = row[1]

        return message

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

    def build_message_attributes (message_id, image_id):
        convo = {}
        convo['message_id'] = message_id
        convo['image_id'] = image_id


    def getAllMessages(self):
        dao = MessageDAO()
        msgs = dao.getAllMessages()
        msgmapped = []
        for m in msgs:
           msgmapped.append(self.build_message_dict(m))

        return jsonify(Messages=msgmapped)

    def searchMessagesByArgs(self, args):
        dao = MessageDAO()

        param1 = args.get('image_id')

        if param1:
            result = dao.searchByImageId(param1)
        else:
            return jsonify(Error="NOT FOUND"), 404

        result1 = []
        for m in result:
            result1.append(self.build_message_dict(m))
        return jsonify(Messages=result1)

    def getMessageById(self, message_id):
        dao = MessageDAO()
        msg = dao.getMessageById(message_id)
        if msg == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            result = self.build_message_dict(msg)

        return jsonify(Message=result)

    def updateMessage(self, message_id, form):
        return jsonify(UpdateMessage="OK"), 200

    def deleteMessage(self, message_id):
        return jsonify(DeleteMessage="OK"), 200

    def postMessage(self,message_id):
        return jsonify(CreateMessage="OK"), 201







