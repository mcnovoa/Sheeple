from flask import jsonify
from daos.reaction import ReactionDAO


class reactionHandler:

    def build_reaction_dict(self, row):
        reaction = {}
        reaction['reaction_id'] = row[0]
        reaction['type'] = row[1]
        reaction['user_id'] = row[2]
        return reaction

    def getAllReactions(self):
        dao = ReactionDAO()
        reactions = dao.getAllReactions()
        mapped_reactions = []
        for row in reactions:
            mapped_reactions.append(self.build_reaction_dict(row))
        return jsonify(Reactions=mapped_reactions)

    def getReactionById(self, id):
        dao = ReactionDAO()
        reaction = dao.getReactionById(id)
        if reaction is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_reaction_dict(reaction)
            return jsonify(Reactions=mapped)

    def getReactionByUserId(self, userId):
        dao = ReactionDAO()
        reactions = dao.getReactionByUserId(userId)
        if reactions is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_reaction_dict(reactions)
            return jsonify(Reactions=mapped)

    def searchReactions(self, args):
        param1 = args.get('reaction_id')
        param2 = args.get('type')
        param3 = args.get('user_id')
        dao = ReactionDAO()

        if param1:
            reactions = dao.getReactionById(param1)
        elif param2:
            reactions = dao.getReactionByType(param2)
        elif param3:
            reactions = dao.getReactionbyUserId(param3)
        else:
            return jsonify(Reaction="NOT FOUND"), 404

        reactions_list = []
        for row in reactions:
            reactions_list.append(self.build_reaction_dict(row))
        return jsonify(Reply=reactions_list)

    def postReaction(self):
        return jsonify(CreateReaction="CREATED"), 201

    def updateReaction(self):
        return jsonify(UpdateReaction="OK"), 200

    def deleteReaction(self):
        return jsonify(DeleteReaction="OK"), 200