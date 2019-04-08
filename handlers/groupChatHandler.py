from flask import jsonify

from daos.groupChat import groupChatDAO
from daos.user import UserDAO


class groupChatHandler:
    def build_groupchat_dict(self, row):
        groupchat = {}
        groupchat['gc_id'] = row[0]
        groupchat['gc_name'] = row[1]

        return groupchat

    def build_useringroupchat_dict(self, row):
        groupchat = {}
        groupchat['user_id'] = row[0]
        groupchat['username'] = row[1]
        groupchat['first_name'] = row[2]
        groupchat['last_name'] = row[3]

        return groupchat

    def build_owner_dict(self, row):
        groupchat = {}
        groupchat['username'] = row[0]
        groupchat['first_name'] = row[1]
        groupchat['last_name'] = row[2]

        return groupchat

    def build_one_dict(self, row):
        groupchat = {}
        groupchat['gc_name'] = row[0]

        return groupchat

    def getAllGroupChats(self):
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

    def deleteGroupChat(self, gc_id):
        dao = groupChatDAO()
        dao.deleteGroupChat(gc_id)
        return jsonify(DeleteGroupChat="OK"), 200

    def postGroupChat(self, gc_name, admin_id):
        dao = groupChatDAO()
        dao.postGroupChat(gc_name, admin_id)
        return jsonify(CreateGroupChat="OK"), 201

    def getAllGroupChatUsers(self, gc_id):
        dao = groupChatDAO()

        result = dao.getUsersInGroupChat(gc_id)
        mapped_result = []

        for row in result:
            mapped_result.append(self.build_useringroupchat_dict(row))

        return jsonify(Users=mapped_result)

    def addUserToGroupChat(self, gc_id, user_id):
        dao = groupChatDAO()

        dao.addUserToGroupChat(gc_id, user_id)

        return jsonify(UserAdded = "OK"),200

    def deleteUserFromGroupChat(self, gc_id, user_id):
        dao = groupChatDAO()
        dao.deleteUserFromGroupChat(gc_id, user_id)

        return jsonify(UserDeleted = "OK"), 200

    def getGroupChatsForUser(self, user_id):
        dao = groupChatDAO()
        result = dao.getGroupChatsForUser(user_id)

        mapped_result = []
        for row in result:
            mapped_result.append(self.build_one_dict(row))
        return jsonify(GroupChats=mapped_result), 200

    def getGroupChatByOwner(self, gc_id):
        dao = groupChatDAO()
        result = dao.getGroupChatbyOwner(gc_id)

        mapped_result = []
        for row in result:
            mapped_result.append(self.build_owner_dict(row))
        return jsonify(Owner=mapped_result)
