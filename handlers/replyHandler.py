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
        id = args.get("reply_id")
        userId = args.get("user_id")
        dao = ReplyDAO()
        replies = []
        if (len(args) == 1) and id:
            replies = dao.getReplyById(id)
        elif len(args) == 1 and userId:
            replies = dao.getReplyByUserId(userId)
        else:
            return jsonify(Error="Malformed query String"), 400

        reply_list = []
        for row in replies:
            result = self.build_reply_dict(row)
            reply_list.append(result)
        return jsonify(Reply=reply_list)
