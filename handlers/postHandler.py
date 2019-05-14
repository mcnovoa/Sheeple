from daos.post import PostDAO
from daos.hashtag import hashtagDAO
from daos.groupChat import groupChatDAO
from daos.user import UserDAO
from handlers.groupChatHandler import groupChatHandler
from flask import Flask, jsonify, request


class postHandler:
    def build_post_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['post_content'] = row[1]
        p['post_date'] = row[2]
        p['image_url'] = row[3]
        p['user_id'] = row[4]
        p['gc_id'] = row[5]
        p['original_post'] = row[6]
        return p
    def build_pr_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['post_content'] = row[1]
        p['user_id'] = row[2]
        return p
    def build_ps_dict(self, row):
        p = {}
        p['day'] = row[0]
        p['total'] = row[1]
        return p

    def build_post_attributes(self, post_id, post_content, post_date, image_url, user_id, gc_id, original_post):
        p = {}
        p['post_id'] = post_id
        p['post_content'] = post_content
        p['post_date'] = post_date
        p['image_url'] = image_url
        p['user_id'] = user_id
        p['gc_id'] = gc_id
        p['original_post'] = original_post
        return p
    def build_r_attributes(self, post_id, post_content, post_date, image_url, user_id, gc_id, original_post):
        p = {}
        p['post_id'] = post_id
        p['post_content'] = post_content
        p['post_date'] = post_date
        p['image_url'] = image_url
        p['user_id'] = user_id
        p['gc_id'] = gc_id
        p['original_post'] = original_post
        return p

    def build_nr_attributes(self, post_id, number_of_reactions):
        nr = {}
        nr['post_id'] = post_id
        nr['total'] = number_of_reactions
        return nr

    def getAllPosts(self):
        dao = PostDAO()
        apst = dao.getAllPosts()
        apsts = []
        for a in apst:
            apsts.append(self.build_post_dict(a))
        return jsonify(Posts=apsts)

    def getPostById(self, post_id):
        dao = PostDAO()
        p = dao.getPostById(post_id)
        if p == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            pmap = self.build_post_dict(p)
        return jsonify(Posts=pmap), 200

    def updatePost(self, post_id, json):
        post_content = json['post_content']  # message, photo || both
        gc_id = json['gc_id']
        user_id = json['user_id']
        post_date = json['post_date']
        image_url = json['image_url']
        original_post = json['original_post']
        result = self.build_post_attributes(post_id, post_content, post_date, image_url, user_id, gc_id, original_post)
        return jsonify(UpdatePost=result), 201

    def deletePost(self, post_id):
        dao = PostDAO()
        p = dao.getPostById(post_id)
        if p == None:
            return jsonify(Error="NOT FOUND"), 404
        result = self.build_post_dict(p)
        return jsonify(DeletePost=result), 200

    def createPost(self, json):
        daop = PostDAO()
        daoh = hashtagDAO()
        gc_id = json['gc_id']
        user_id = json['user_id']
        post_date = json['post_date']
        image_url = json['image_url']
        post_content = json['post_content']
        if post_content is None or post_date is None or gc_id is None or user_id is None:
            return jsonify(Error='Must have post content, groupchat id, user id and post date'), 400
        p = daop.insertPost(post_content, post_date, image_url, user_id, gc_id)
        if p is not None:
            tag = post_content
            X = {tag.strip("#") for tag in tag.split() if tag.startswith("#")}
            for h in X:
                daoh.postHashtag(p, h)
            result = {}
            result = self.build_post_attributes(p, post_content, post_date, image_url, user_id, gc_id, 'None')
            return jsonify(CreatePost=result), 201
        else:
            return jsonify(Error="User is not subscribed in this groupchat.")

    def replyPost(self, json):
        daop = PostDAO()
        daoh = hashtagDAO()
        gc_id = json['gc_id']
        user_id = json['user_id']
        post_date = json['post_date']
        image_url = json['image_url']
        post_content = json['post_content']
        original_post = json['original_post']
        if post_content is None or post_date is None or gc_id is None or user_id is None or original_post is None:
            return jsonify(Error='Must have post content, groupchat id, user id, post date and original post'), 400
        p = daop.insertReply(post_content, post_date, image_url, user_id, gc_id, original_post)
        if p is not None:
            tag = post_content
            X = {tag.strip("#") for tag in tag.split() if tag.startswith("#")}
            for h in X:
                daoh.postHashtag(p, h)
            result = {}
            result = self.build_post_attributes(p, post_content, post_date, image_url, user_id, gc_id, original_post)
            return jsonify(ReplyPost=result), 201
        else:
            return jsonify(Error="User is not subscribed in this groupchat.")

    def getPostsByGC(self, gc_id):
        dao = PostDAO()
        gcp = dao.getPostsByGC(gc_id)
        result = []
        for a in gcp:
            result.append(self.build_post_dict(a))
        return jsonify(Posts=result)

    def getPostsReplies(self):
        dao = PostDAO()
        ps = dao.getAllPosts()
        result = []
        for i in ps:
            result.append(self.build_post_dict(i))
        return jsonify(PostAndReplies=result), 200

    def reactPost(self, reaction_type, json):
        dao = PostDAO()

        post_id = json['post_id']
        user_id = json['user_id']

        if post_id is None or reaction_type is None or user_id is None:
            return jsonify(Error='Must have reaction type, post id, group chat if and user id'), 400
        p = dao.reactPost(reaction_type, post_id, user_id)
        if p == 1:
            result = self.build_post_dict(dao.getPostById(post_id))
            if reaction_type == 'like':
                return jsonify(PostLike=result), 200
            elif reaction_type == 'dislike':
                return jsonify(PostDislike=result), 200
            else:
                return jsonify(Error="Reaction Not Allowed."), 404
        elif p == -1:
            return jsonify(Error="User already liked or disliked post.")
        else:
            return jsonify(Error="User is not subscribed in this groupchat or post does not belong to this group chat.")

    def getUserWhoLikesPost(self, post_id):
        dao = PostDAO()
        result = dao.getUserWhoLikesPost(post_id)
        mappped_result = []
        for row in result:
            mappped_result.append(self.build_react_dict(row))
        return jsonify(Likes=mappped_result)

    def getUserWhoDislikesPost(self, post_id):
        dao = PostDAO()
        result = dao.getUserWhoDislikesPost(post_id)
        mappped_result = []
        for row in result:
            mappped_result.append(self.build_react_dict(row))
        return jsonify(Dislikes=mappped_result)

    # def getPostsPerDay(self):
    #     dao = PostDAO()
    #     pts = dao.getPostsPerDay()
    #     result = []
    #     for a in pts:
    #         result.append(self.build_ps_dict(a))
    #     return jsonify(PostsPerDay=result)
    #
    # def getRepliesPerDay(self):
    #     dao = PostDAO()
    #     pts = dao.getRepliesPerDay()
    #     result = []
    #     for a in pts:
    #         result.append(self.build_ps_dict(a))
    #     return jsonify(RepliesPerDay=result)
    #
    # def getReactionsPerDay(self, reaction_type):
    #     dao = PostDAO()
    #     pts = dao.getReactionsPerDay(reaction_type)
    #     result = []
    #     for a in pts:
    #         result.append(self.build_ps_dict(a))
    #
    #     if reaction_type == 'like':
    #         return jsonify(LikesPerDay=result)
    #     elif reaction_type == 'dislike':
    #         return jsonify(DislikesPerDay=result)
    #     else:
    #         return jsonify("Reaction not allowed.")
    #
    # def mostActiveUsersPerDay(self):
    #     dao = PostDAO()
    #     pts = dao.mostActiveUsersPerDay()
    #     result = []
    #     for a in pts:
    #         result.append(self.build_ps_dict(a))
    #     return jsonify(MostActiveUsersPerDay=result)
    #
    # def getnumPostsByUserPerDay(self, user_id):
    #     dao = PostDAO()
    #     pts = dao.getnumPostsByUserPerDay(user_id)
    #     result = []
    #     for a in pts:
    #         result.append(self.build_ps_dict(a))
    #     return jsonify(NumberOfPostsPerDayByXUser=result)
    #
    # def getnumRepliesOfPost(self, post_id):
    #     dao = PostDAO()
    #     pts = dao.getnumRepliesOfPost(post_id)
    #     result = []
    #     for a in pts:
    #         result.append(self.build_fro_dict(a))
    #     return jsonify(NumberOfRepliesOfPost=result)
    #
    # def getNumOfReactions(self, post_id, reaction_type):
    #     dao = PostDAO()
    #     p = dao.getPostById(post_id)
    #     if p == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     cr = dao.getNumOfReactions(post_id, reaction_type)
    #     result = []
    #     for a in cr:
    #         result.append(self.build_fro_dict(a))
    #     if reaction_type == 'like':
    #         return jsonify(NumberOfLikes=result), 200
    #     elif reaction_type == 'dislike':
    #         return jsonify(NumberOfDislikes=result), 200
    #     else:
    #         return jsonify(Error="Reaction Not Allowed"), 404
