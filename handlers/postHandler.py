from flask import jsonify

from daos.post import PostDAO


class postHandler:

    def build_post_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['post_content'] = row[1]
        p['post_date'] = row[2]
        p['user_id'] = row[3]
        p['gc_id'] = row[4]
        p['hashtag_id'] = row[5]
        p['reaction_id'] = row[6]
        p['reply_id'] = row[7]
        p['reaction_amount'] = row[8]
        p['reply_amount'] = row[9]

        return p

    def build_post_attributes (post_id, post_content, post_date, user_id, gc_id, hashtag_id, reaction_id,
                               reply_id, reaction_amount, reply_amount):
        groupchat = {}
        groupchat['post_id'] = post_id
        groupchat['post_content'] = post_content
        groupchat['post_date'] = post_date
        groupchat['user_id'] = user_id
        groupchat['gc_id'] = gc_id
        groupchat['hashtag_id'] = hashtag_id
        groupchat['reaction_id'] = reaction_id
        groupchat['reply_id'] = reply_id
        groupchat['reaction_amount'] = reaction_amount
        groupchat['reply_amount'] = reply_amount


    def getAllPosts(self):
        dao = PostDAO()
        apst = dao.getAllPosts()
        apsts = []
        for a in apst:
            apsts.append(self.build_post_dict(a))

        return jsonify(Posts=apsts)

    def searchByArgs(self, args):
        daop = PostDAO()

        param1 = args.get('post_content') #message, photo || both
        param2 = args.get('post_date')
        param3 = args.get('user_id')
        param4 = args.get('gc_id')
        param5 = args.get('hashtag_id')
        param6 = args.get('reaction_id')
        param7 = args.get('reply_id')
        param8 = args.get('reaction_amount')
        param9 = args.get('reply_amount')

        if param1:
            result = daop.getPostContent(param1)
        elif param2:
            result = daop.getPostDate(param2)
        elif param3:
            result = daop.getPostUser(param3)
        elif param4:
            result = daop.getPostGroupChat(param4)
        elif param5:
            result = daop.getPostHashtag(param5)
        elif param6:
            result = daop.getPostReactions(param6)
        elif param7:
            result = daop.getPostReplies(param7)
        elif param8:
            result = daop.getPostReactionAmount(param8)
        elif param9:
            result = daop.getPostRepliesAmount(param9)
        else:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for p in result:
            mapped_result.append(self.build_post_dict(p))
        return jsonify(Posts=mapped_result)


    def getPostById(self, post_id):
        dao = PostDAO()
        p = dao.getPostBy(post_id)
        if p == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            pmap = self.build_groupchat_dict(p)

        return jsonify(Posts=pmap)

    def updatePost(self, post_id, form):
        return jsonify(UpdatePost="OK"), 200

    def deletePost(self, post_id):
        return jsonify(DeletePost="OK"), 200

    def postPost(self, post_id):
        return jsonify(CreatePost="OK"), 201



