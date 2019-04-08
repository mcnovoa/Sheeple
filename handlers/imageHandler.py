from daos.image import ImageDAO
from daos.post import PostDAO
from flask import jsonify


class imageHandler:

    def build_image_dict(self, row):
        img = {}
        img['image_id'] = row[0]
        img['image_url'] = row[1]
        img['post_id'] = row[2]

        return img

    def build_image_attributes(self, image_id, image_url, post_id):
        img = {}
        img['image_id'] = image_id
        img['image_url'] = image_url
        img['post_id'] = post_id

        return img

    def build_pimg_dict(self, row):
        img = {}
        img['post_id'] = row[0]
        img['post_content'] = row[1]
        img['gc_id'] = row[2]
        img['user_id'] = row[3]
        img['post_date'] = row[4]
        img['image_id'] = row[5]
        img['image_url'] = row[6]
        img['reply_id'] = row[7]

        return img

    def build_pimgr_dict(self, row):
        img = {}
        img['post_id'] = row[0]
        img['post_content'] = row[1]
        img['gc_id'] = row[2]
        img['user_id'] = row[3]
        img['post_date'] = row[4]
        img['image_id'] = row[5]
        img['image_url'] = row[6]
        img['reaction_by'] = row[7]

        return img

    def buil_r_dict(self, row):
        img = {}
        img['post_id'] = row[0]
        img['post_content'] = row[1]
        img['gc_id'] = row[2]
        img['user_id'] = row[3]
        img['post_date'] = row[4]
        img['image_id'] = row[5]
        img['image_url'] = row[6]
        img['reply_id'] = row[7]

        return img

    def getAllImages(self):
        dao = ImageDAO()
        imgs = dao.getAllImages()
        imgmapped = []
        for m in imgs:
           imgmapped.append(self.build_pimg_dict(m))

        return jsonify(Images=imgmapped)

    def getImageById(self, image_id):
        dao = ImageDAO()
        img = dao.getImagesById(image_id)
        if img == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            imap = self.build_pimg_dict(img)

        return jsonify(Images=imap)

    def updateImage(self, image_id, args):
        dao = ImageDAO()
        image_url = args.get('image_url')
        img = self.build_image_dict(dao.getImagesById(image_id))
        img.__setitem__('image_url', image_url)
        return jsonify(UpdateImage=img), 201

    def deleteImage(self, image_id):
        result = self.getImageById(image_id)
        return result, 200

    def createImage(self, image_id, args):
        image_url = args.get('image_url')
        post_id = args.get('post_id')

        result = self.build_image_attributes(image_id, image_url, post_id)
        return jsonify(CreateImage=result), 201


