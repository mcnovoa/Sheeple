from daos.post import PostDAO
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
        nr['numer_of_reactions'] = number_of_reactions

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

    def updatePost(self, post_id, args):
        post_content = args.get('post_content')  # message, photo || both
        gc_id = args.get('gc_id')
        user_id = args.get('user_id')
        post_date = args.get('post_date')
        image_url = args.get('image_url')
        original_post = args.get('original_post')
        result = self.build_post_attributes(post_id, post_content, post_date, image_url, user_id,  gc_id, original_post)

        return jsonify(UpdatePost=result), 201

    def deletePost(self, post_id):
        dao = PostDAO()
        p = dao.getPostById(post_id)
        if p == None:
            return jsonify(Error="NOT FOUND"), 404
        result = self.build_post_dict(p)

        return jsonify(CreatePost=result), 200

    def createPost(self, post_id, args):
        dao = PostDAO()
        s = dao.getPostById(post_id)

        if s != None:
            return jsonify(Error="Post Already Exists"), 404

        post_content = args.get('post_content')
        gc_id = args.get('gc_id')
        user_id = args.get('user_id')
        post_date = args.get('post_date')
        image_url = args.get('image_url')
        original_post = args.get('original_post')

        result = {}
        if post_content and gc_id and user_id and post_date:
            result = self.build_post_attributes(post_id, post_content, post_date, image_url, user_id, gc_id, original_post)

        return jsonify(CreatePost= result), 201

    def replyPost(self, post_id, original_post, args):
        post_content = args.get('post_content')  # message, photo || both
        gc_id = args.get('gc_id')
        user_id = args.get('user_id')
        post_date = args.get('post_date')
        image_url = args.get('image_url')
        r = self.build_post_attributes(post_id, post_content, post_date, image_url, user_id, gc_id, original_post)

        return jsonify(CreateReply=r), 200

    def getNumOfReactions(self, post_id, reaction_type):
        dao = PostDAO()
        p = dao.getPostById(post_id)
        if p == None:
            return jsonify(Error="NOT FOUND"), 404
        cr = dao.getNumOfReactions(post_id, reaction_type)
        nr = self.build_nr_attributes(post_id, cr)
        if reaction_type == 'like':
            return jsonify(NumberOfLikes=nr), 200
        elif reaction_type == 'dislike':
            return jsonify(NumberOfDislikes=nr), 200
        else:
            return jsonify(Error="Reaction Not Allowed"), 404

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

    def reactPost(self, post_id, reaction_type, user_id):
        dao = PostDAO()
        img = self.build_post_dict(dao.getPostById(post_id))
        if reaction_type == 'like':
            return jsonify(PostLike=img), 200
        elif reaction_type == 'dislike':
            return jsonify(PostDislike=img), 200
        else:
            return jsonify(Error="Reaction Not Allowed"), 404

    def getPostsByDay(self):
        dao = PostDAO()
        pts = dao.getPostsByDay()
        result = []
        for a in pts:
            result.append(self.build_ps_dict(a))
        return jsonify(PostsByDay=result)

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
