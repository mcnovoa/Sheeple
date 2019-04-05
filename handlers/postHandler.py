from daos.post import PostDAO

from flask import Flask, jsonify, request

class postHandler:

    def build_post_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['post_content'] = row[1]
        p['gc_id'] = row[2]
        p['user_id'] = row[3]
        p['post_date'] = row[4]

        return p

    def build_post_attributes(self, post_id, post_content, gc_id, user_id, post_date):
        post = {}
        post['post_id'] = post_id
        post['post_content'] = post_content
        post['post_date'] = post_date
        post['user_id'] = user_id
        post['gc_id'] = gc_id

        return post

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

        return jsonify(Posts=pmap)

    def updatePost(self, post_id, form):
        return jsonify(UpdatePost="OK"), 200

    def deletePost(self, post_id):
        return jsonify(DeletePost="OK"), 200

    def createPost(self, post_id, args):
        post_content = args.get('post_content')  # message, photo || both
        gc_id = args.get('gc_id')
        user_id = args.get('user_id')
        post_date = args.get('post_date')

        result = self.build_post_attributes(post_id, post_content, gc_id, user_id, post_date)
        return jsonify(CreatePost= result), 201



