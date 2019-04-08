from flask import jsonify

from daos.hashtag import hashtagDAO


class hashtagHandler:
    def build_hashtag_dict(self, row):
            hashtag = {}
            hashtag['hashtag_id'] = row[0]
            hashtag['content'] = row[1]
            return hashtag

    def build_dashboard_dict(self, row):
        hashtag = {}
        hashtag['Hashtag'] = row[0]
        hashtag['Total'] = row[1]

        return hashtag

    def getAllHashtags(self):
        dao = hashtagDAO()
        result = dao.getAllHashtags()
        mapped_results = []
        for row in result:
            mapped_results.append(self.build_hashtag_dict(row))
        return jsonify(Reply=mapped_results)

    def getHashtagById(self, id):
        dao = hashtagDAO()
        hashtags = dao.getHashtagById(id)
        if hashtags is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_hashtag_dict(hashtags)
            return jsonify(Reply=mapped)

    def getHashtagByContent(self, content):
        dao = hashtagDAO()
        hashtags = dao.getHashtagByContent(content)
        if hashtags is None:
            return jsonify(Error="Not Found"), 404
        else:
            mapped = self.build_hashtag_dict(hashtags)
            return jsonify(Reply=mapped)

    def searchHashtags(self, args):
        param1 = args.get('hashtag_id')
        param2 = args.get('content')
        dao = hashtagDAO()
        print(param2)
        if param1:
            hashtags = dao.getHashtagById(param1)
        elif param2:
            hashtags = dao.getHashtagByContent(param2)
        else:
            return jsonify(Reaction="NOT FOUND"), 404

        hashtag_list = []
        for row in hashtags:
            hashtag_list.append(self.build_hashtag_dict(row))
        return jsonify(Hashtag=hashtag_list)

    def getPopularHashtags(self):
        dao = hashtagDAO()
        result = dao.getPopularHashtags()
        mapped_result = []

        for row in result:
            mapped_result.append(self.build_dashboard_dict(row))

        return jsonify(Hashtag = mapped_result), 200

    def postHashtag(self):
        return jsonify(CreateHashtag="CREATED"), 201

    def updateHashtag(self):
        return jsonify(UpdatePerson="OK"), 200

    def deleteHashtag(self):
        return jsonify(DeletePerson="OK"), 200