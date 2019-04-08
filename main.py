from flask import Flask, jsonify, request
from flask_cors import CORS

from handlers.contactListHandler import contactListHandler
from handlers.groupChatHandler import groupChatHandler
from handlers.hashtagHandler import hashtagHandler
from handlers.imageHandler import imageHandler
from handlers.postHandler import postHandler
from handlers.userHandler import userHandler

app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomesheeple():
    return 'Sheeple!'


# --------------------------Overview---------------------------#
# @app.route('/Sheeple/users?<string: username>&<string:password>&<string:first_name>&<string:last_name>&<char:gender>&<string:email>&<string:phone_number>', methods=['POST'])
#
#
# @app.route('/Sheeple/login?<string:username>&<string:password', methods=['POST'])
#
#
# @app.route('/Sheeple/groupchat?<string:gc_name>&<string:user_id>', methods=['POST', 'DELETE'])
#
#
# @app.route('/Sheeple/contactlist/<int:cl_id>/<int:user_id>', methods=['POST', 'DELETE'])
#
#
# @app.route('/Sheeple/groupchat/<int:gc_id>', methods=['DELETE'])
#
#Este route ya existe:
# @app.route('/Sheeple/posts/<int:gc_id>?<string:image_url>&<string:post_content>', methods=['POST'])
#
#
@app.route('/Sheeple/posts-and-replies', methods=['GET'])
def doGetPostsReplies():
    handler = postHandler()
    if request.method == 'GET':
       return handler.getPostsReplies()
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/posts/<int:post_id>/<string:reaction_type>/<int:user_id>' ,methods=['POST'])
def reactPost(post_id, reaction_type, user_id):
    handler = postHandler()
    if request.method == 'POST':
        return handler.reactPost(post_id, reaction_type, user_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/posts/<int:post_id>/reply/<int:original>', methods= ['POST'])
def replyPost(post_id, original):
    handler = postHandler()
    if request.method == 'POST':
        return handler.replyPost(post_id,original, request.args)
    else:
        return jsonify(Error="Method not allowed."), 405
#
# # ------------------- ----Second Phase-------------------------#
#
@app.route('/Sheeple/posts', methods=['GET'])
def getAllPosts():
    handler = postHandler()

    if request.method == 'GET':
        return handler.getAllPosts()
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/posts/reactions/<string:reaction_type>/<int:post_id>', methods=['GET'])
def getNumOfReactions(post_id, reaction_type):
    handler = postHandler()
    if request.method == 'GET':
        return handler.getNumOfReactions(post_id, reaction_type)
    else:
        return jsonify(Error="Method not allowed."), 405

#
#
# @app.route('/Sheeple/contactlist/user_id', methods= ['GET'])
#
#
@app.route('/Sheeple/posts/groupchat/<int:gc_id>', methods= ['GET'])
def doByPostGC(gc_id):
    handler = postHandler()
    if request.method == 'GET':
        return handler.getPostsByGC(gc_id)
    else:
        return jsonify(Error="Method not allowed."), 405

# @app.route('/Sheeple/users/gc_id', methods= ['GET'])
#
#
# @app.route('/Sheeple/users', methods= ['GET'])
#
#
# @app.route('/Sheeple/groupchat', methods= ['GET'])
#
#
# @app.route('/Sheeple/owner/gc_id', methods= ['GET'])
#
#
# @app.route('/Sheeple/users/<int:user_id>', methods= ['GET'])
#
#
# @app.route('/Sheeple/users?<string:username>', methods=['GET'])
#


# --------------------Start Contact Lists----------------------#

@app.route('/Sheeple/ContactLists', methods=['GET'])
def getAllContactLists():
    if request.args:
        return contactListHandler().searchContactLists(request.args)
    else:
        handler = contactListHandler()
        return handler.getAllContactLists()


@app.route('/Sheeple/ContactLists/<int:contact_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doContactListById(contact_id):
    handler = contactListHandler()
    if request.method == 'GET':
        return handler.getContactListByID(contact_id)
    elif request.method == 'POST':
        return handler.postContactList()
    elif request.method == 'PUT':
        return handler.updateContactList()
    else:
        return handler.deleteContactList()


@app.route('/Sheeple/ContactLists/deleteUser/<int:user_id>', methods=['DELETE'])
def RemoveUserFromContactLists(user_id):
    return jsonify(DeletedUser='OK'), 200


# -------------------------End Contact Lists--------------------------#


# --------------------------Start Group Chat--------------------------#


@app.route('/Sheeple/groupchats', methods=['GET'])
def getAllGroupchats():
    handler = groupChatHandler()
    if request.args:
        return handler.searchByArgs(request.args)
    else:
        return handler.getAllGroupChatss()


@app.route('/Sheeple/conversations/<int:gc_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doByGroupChatId(gc_id):
    handler = groupChatHandler()
    if request.method == 'GET':
        return groupChatHandler().getGroupChatById(gc_id)
    elif request.method == 'POST':
        return groupChatHandler().postGroupChat(gc_id)
    elif request.method == 'PUT':
        return groupChatHandler().updateGroupChat(gc_id, request.form)
    elif request.method == 'DELETE':
        return groupChatHandler().deleteGroupChat(gc_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/conversations/<int:gc_id>/users', methods=['GET'])
def getAllGroupChatUsers(gc_id):
    handler = groupChatHandler()
    if request.method == 'GET':
        return handler.getAllGroupChatUsers(gc_id)


# -------------------------End Conversations--------------------------#

#------------------------Start Hashtag--------------------------------#

@app.route('/Sheeple/hashtags', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getAllHashtags():
    handler = hashtagHandler()
    if request.method == 'GET':
        if request.args:
            return handler.searchHashtags(request.args)
        else:
            handler = hashtagHandler()
            return handler.getAllHashtags()
    elif request.method == 'POST':
        return handler.postHashtag()
    elif request.method == 'PUT':
        return handler.updateHashtag()
    else:
        return handler.deleteHashtag()



@app.route('/Sheeple/hashtags/<int:id>', methods=['GET'])
def getHashtagById(id):
    handler = hashtagHandler()
    return handler.getHashtagById(id)

#------------------------End Hashtag----------------------------------#


# ---------------------------Start Images-----------------------------#
@app.route('/Sheeple/images', methods=['GET'])
def getAllImages():
    handler = imageHandler()
    if request.args:
        return handler.searchImagesByArgs(request.args)
    else:
        return handler.getAllImages()


@app.route('/Sheeple/images/<int:image_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doByImageId(image_id):
    handler = imageHandler()
    if request.method == 'GET':
        return handler.getImageById(image_id)
    elif request.method == 'POST':
        return handler.createImage(image_id, request.args)
    elif request.method == 'PUT':
        return handler.updateImage(image_id, request.args)
    elif request.method == 'DELETE':
        return handler.deleteImage(image_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# ---------------------------End Images-----------------------------#

# ---------------------------Start Post-------------------------------#


@app.route('/Sheeple/posts/<int:post_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doByPostId(post_id):
    handler = postHandler()
    if request.method == 'GET':
        return handler.getPostById(post_id)
    elif request.method == 'POST':
        return handler.createPost(post_id, request.args)
    elif request.method == 'PUT':
        return handler.updatePost(post_id)
    elif request.method == 'DELETE':
        return handler.deletePost(post_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# -----------------------------End Post-------------------------------#


# ---------------------------Start Users----------------------------#
@app.route('/Sheeple/users', methods=['GET', 'POST', 'PUT', "DELETE"])
def getAllUsers():
    if request.method == 'GET':
        if request.args:
            return userHandler().searchUsers(request.args)
        else:
            handler = userHandler()
            return handler.getAllUsers()
    elif request.method == 'POST':
        return userHandler().postUser()
    elif request.method == 'PUT':
        return userHandler().updateUser()
    else:
        return userHandler().deleteUser()


@app.route('/Sheeple/users/<int:user_id>', methods=['GET'])
def getUsersById(user_id):
    handler = userHandler()
    return handler.getUserByID(user_id)








if __name__ == '__main__':
    app.run()