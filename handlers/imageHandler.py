from daos.image import ImageDAO
from daos.user import UserDAO
from flask import Flask, jsonify, request

class imageHandler:
    def build_image_dict(self, row):
        img = {}
        img['image_id'] = row[0]
        img['message_id'] = row[1]

        return img

    def build_post_dict(self, row):
        p = {}
        p['post_id'] = row[0]
        p['post_content'] = row[1]
        p['post_date'] = row[2]
        p['user_id'] = row[3]
        p['convo_id'] = row[4]
        p['hashtag_id'] = row[5]
        p['reaction_id'] = row[6]
        p['reply_id'] = row[7]
        p['reaction_amount'] = row[8]
        p['reply_amount'] = row[9]

    def build_image_attributes (image_id, message_id):
        convo = {}
        convo['image_id'] = image_id
        convo['message_id'] = message_id


    def getAllImages(self):
        dao = ImageDAO()
        imgs = dao.getAllImages()
        imgmapped = []
        for m in imgs:
           imgmapped.append(self.build_image_dict(m))

        return jsonify(Images=imgmapped)

    def searchImagesByArgs(self, args):
        dao = ImageDAO()

        param1 = args.get('message_id')

        if param1:
            result = dao.searchByMessageId(param1)
        else:
            return jsonify(Error="NOT FOUND"), 404

        result1 = []
        for i in result:
            result1.append(self.build_image_dict(i))
        return jsonify(Images=result1)

    def getImageById(self, image_id):
        dao = ImageDAO()
        img = dao.getImagesById(image_id)
        if img == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            result = self.build_message_dict(img)

        return jsonify(Image=result)

    def updateImage(self, image_id, form):
        return jsonify(UpdateImage="OK"), 200

    def deleteImage(self, image_id):
        return jsonify(DeleteImage="OK"), 200

    def postImage(self,image_id):
        return jsonify(CreateImage="OK"), 201







