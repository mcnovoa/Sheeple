from flask import jsonify
from daos.reply import ReplyDAO


class replyHandler:
    def build_reply_dict(self, row):
            reply = {}
            reply['reply_id'] = row[0]
            reply['user_id'] = row[1]
            return reply

    def getAllReplies(self):
        dao = ReplyDAO()
        replies = dao.getAllReplies()
        mapped_replies = []
        for row in replies:
            mapped_replies.append(self.build_reply_dict(row))
        return jsonify(Reply=mapped_replies)

    def getReplyById(self, id):
        dao = ReplyDAO()
        replies = dao.getReplyById(id)
        if replies is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_reply_dict(replies)
            return jsonify(Reply=mapped)

    def getReplyByUserId(self, userId):
        dao = ReplyDAO()
        replies = dao.getReplyByUserId(userId)
        if replies is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_reply_dict(replies)
            return jsonify(Reply=mapped)

    def searchReplies(self, args):
        param1 = args.get("reply_id")
        param2 = args.get("user_id")
        dao = ReplyDAO()

        if param1:
            replies = dao.getReplyById(param1)
        elif param2:
            replies = dao.getReplyByUserId(param2)
        else:
            return jsonify(Error="NOT FOUND"), 404

        reply_list = []
        for row in replies:
            reply_list.append(self.build_reply_dict(row))
        return jsonify(Reply=reply_list)
