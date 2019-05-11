from daos.dashboard import DashboardDAO
from daos.hashtag import hashtagDAO
from flask import jsonify

class dashboardHandler:

    def build_fro_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['total'] = row[1]
        return p

    def build_ps_dict(self, row):
        p = {}
        p['day'] = row[0]
        p['total'] = row[1]
        return p

    def build_dashboard_dict(self, row):
        hashtag = {}
        hashtag['Hashtag'] = row[0]
        hashtag['Total'] = row[1]

        return hashtag

    def getPopularHashtags(self):
        dao = DashboardDAO()
        result = dao.getPopularHashtags()
        mapped_result = []

        for row in result:
            mapped_result.append(self.build_dashboard_dict(row))

        return jsonify(Hashtag = mapped_result), 200

    def getPostsPerDay(self):
        dao = DashboardDAO()
        pts = dao.getPostsPerDay()
        result = []
        for a in pts:
            result.append(self.build_ps_dict(a))
        return jsonify(PostsPerDay=result)


    def getRepliesPerDay(self):
        dao = DashboardDAO()
        pts = dao.getRepliesPerDay()
        result = []
        for a in pts:
            result.append(self.build_ps_dict(a))
        return jsonify(RepliesPerDay=result)


    def getReactionsPerDay(self, reaction_type):
        dao = DashboardDAO()
        pts = dao.getReactionsPerDay(reaction_type)
        result = []
        for a in pts:
            result.append(self.build_ps_dict(a))

        if reaction_type == 'like':
            return jsonify(LikesPerDay=result)
        elif reaction_type == 'dislike':
            return jsonify(DislikesPerDay=result)
        else:
            return jsonify("Reaction not allowed.")


    def mostActiveUsersPerDay(self):
        dao = DashboardDAO()
        pts = dao.mostActiveUsersPerDay()
        result = []
        for a in pts:
            result.append(self.build_ps_dict(a))
        return jsonify(MostActiveUsersPerDay=result)


    def getnumPostsByUserPerDay(self, user_id):
        dao = DashboardDAO()
        pts = dao.getnumPostsByUserPerDay(user_id)
        result = []
        for a in pts:
            result.append(self.build_ps_dict(a))
        return jsonify(NumberOfPostsPerDayByXUser=result)


    def getnumRepliesOfPost(self, post_id):
        dao = DashboardDAO()
        pts = dao.getnumRepliesOfPost(post_id)
        result = []
        for a in pts:
            result.append(self.build_fro_dict(a))
        return jsonify(NumberOfRepliesOfPost=result)


    def getNumOfReactions(self, post_id, reaction_type):
        dao = DashboardDAO()
        p = dao.getPostById(post_id)
        if p == None:
            return jsonify(Error="NOT FOUND"), 404
        cr = dao.getNumOfReactions(post_id, reaction_type)
        result = []
        for a in cr:
            result.append(self.build_fro_dict(a))
        if reaction_type == 'like':
            return jsonify(NumberOfLikes=result), 200
        elif reaction_type == 'dislike':
            return jsonify(NumberOfDislikes=result), 200
        else:
            return jsonify(Error="Reaction Not Allowed"), 404
