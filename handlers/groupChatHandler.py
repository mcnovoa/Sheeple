from flask import jsonify

from daos.groupChat import groupChatDAO
from daos.user import UserDAO


class groupChatHandler:
    def build_groupchat_dict(self, row):
        groupchat = {}
        groupchat['gc_id'] = row[0]
        groupchat['gc_name'] = row[1]

        return groupchat

    def getAllGroupChatss(self):
        dao = groupChatDAO()
        groupchats = dao.getAllGroupChats()
        groupchatsmapped = []
        for c in groupchats:
            groupchatsmapped.append(self.build_groupchat_dict(c))

        return jsonify(Conversations=groupchatsmapped)

    def searchByArgs(self, args):
        dao = groupChatDAO()

        param = args.get('gc_name')

        if param:
            result = dao.getAllGroupChatNames(param)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for c in result:
            mapped_result.append(self.build_groupchat_dict(c))
        return jsonify(GroupChats=mapped_result)

    def getGroupChatById(self, gc_id):
        dao = groupChatDAO()
        rgroupchat = dao.getGroupChatById(gc_id)
        if rgroupchat == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            groupchatmap = self.build_groupchat_dict(rgroupchat)

        return jsonify(Conversation=groupchatmap)

    def updateGroupChat(self, groupchat_id, form):
        return jsonify(UpdateGroupChat="OK"), 200

    def deleteGroupChat(self, groupchat_id):
        return jsonify(DeleteGroupChat="OK"), 200

    def postGroupChat(self, groupchat_id):
        return jsonify(CreateGroupChat="OK"), 201

    def getAllGroupChatUsers(self, groupchat_id):
        daoc = groupChatDAO()
        daou = UserDAO()
        usr = daou.getAllUsers()
        result = []
        rgroupchat = daoc.getGroupChatsById(groupchat_id)

        if rgroupchat == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for u in usr:
                if rgroupchat.__contains__(u):
                    result.append(u)
        return jsonify(Users=result)
