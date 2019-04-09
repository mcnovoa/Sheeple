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

# ---------------------Login & Register-------------------------#

# Registration page
@app.route("/Sheeple/register", methods=['POST'])
def register():
    if request.method =='POST':
        return userHandler().createUser(request.args)

# Login page
@app.route("/Sheeple/login", methods=['POST'])
def login():
    if request.method == 'POST':
        return userHandler().getUserByUsernameAndPassword(request.args)

# ------------------------Dashboard ----------------------------#
@app.route('/Sheeple/dashboard/posts', methods= ['GET'])
def getPostsByDay():
    handler = postHandler()
    if request.method == 'GET':
        return handler.getPostsByDay()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Sheeple/dashboard/hashtags', methods=['GET'])
def popularHashtags():
    handler = hashtagHandler()
    if request.method == 'GET':
        return handler.getPopularHashtags()
    else:
        return jsonify(Error="Method not allowed")

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


# Adds, Deletes or Gets the users in a given Contact List
@app.route('/Sheeple/contactlists/user/<int:user_id>', methods=['GET'])
def getContactListByUser_id(user_id):
    handler = contactListHandler()
    if request.method == 'GET':
        return handler.getContactListByOwnerId(user_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/posts/groupchat/<int:gc_id>', methods=['GET'])
def doByPostGC(gc_id):
    handler = postHandler()
    if request.method == 'GET':
        return handler.getPostsByGC(gc_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/groupchats/owner/<int:gc_id>', methods= ['GET'])
def getGroupChatByOwner(gc_id):
    handler = groupChatHandler()

    if request.method == 'GET':
        return handler.getGroupChatByOwner(gc_id)
    else:
        return jsonify(Error="Method not allowed"), 405


# --------------------Start Contact Lists----------------------#

@app.route('/Sheeple/contactlists', methods=['GET', 'POST'])
def getAllContactLists():
    handler = contactListHandler()
    if request.method == 'GET':
        if request.args:
            return handler.searchContactLists(request.args)
        else:
            return handler.getAllContactLists()
    elif request.method == 'PUT':
        return handler.postContactList(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405
#
@app.route('/Sheeple/contactlists/<int:cl_id>', methods=['GET', 'PUT', 'DELETE'])
def doContactListById(cl_id):
    handler = contactListHandler()
    if request.method == 'GET':
        return handler.getContactListByID(cl_id)
    elif request.method == 'PUT':
        pass
        # return handler.updateContactList(cl_id, request.args)
    elif request.method == 'DELETE':
        pass
        # return handler.deleteContactList(cl_id)
    else:
        return jsonify(Error="Method not allowed."), 405

# Add or Delete Contact from contact list of user X
@app.route('/Sheeple/contactlists/<int:cl_id>/user', methods=['DELETE', 'POST'])
def addOrDeleteFromContactList(cl_id):
    handler = contactListHandler()
    if request.method == 'POST':
        if request.args:
            return handler.postUserIntoContactList(cl_id, request.args)
        else:
            return jsonify(Error="Malformed request."), 405
    elif request.method == 'DELETE':
        if request.args:
            return handler.deleteUserFromContactList(cl_id, request.args)
        else:
            return jsonify(Error="Malformed request."), 405
    else:
        return jsonify(Error="Method not allowed."), 405

# -------------------------End Contact Lists--------------------------#


# --------------------------Start Group Chat--------------------------#


@app.route('/Sheeple/groupchats', methods=['GET', 'POST'])
def getAllGroupchats():
    handler = groupChatHandler()

    if request.method == 'POST':
        gc_name = request.args.get('gc_name')
        admin_id = request.args.get('admin_id')
        return handler.postGroupChat(gc_name, admin_id)
    elif request.args:
        return handler.searchByArgs(request.args)
    else:
        return handler.getAllGroupChats()


@app.route('/Sheeple/groupchats/<int:gc_id>', methods=['GET', 'PUT', 'DELETE'])
def doByGroupChatId(gc_id):
    handler = groupChatHandler()
    if request.method == 'GET':
        return groupChatHandler().getGroupChatById(gc_id)
    elif request.method == 'PUT':
        return handler.updateGroupChat(gc_id, request.form)
    elif request.method == 'DELETE':
        return handler.deleteGroupChat(gc_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/groupchats/<int:gc_id>/users', methods=['GET'])
def getAllGroupChatUsers(gc_id):
    handler = groupChatHandler()
    if request.method == 'GET':
        return handler.getAllGroupChatUsers(gc_id)

    else:
        jsonify(Error="Method not allowed."), 405

@app.route('/Sheeple/groupchats/<int:gc_id>/<int:user_id>', methods=['POST', 'DELETE'])
def addOrDeleteUserFromGroupchat(gc_id, user_id):
    handler = groupChatHandler()

    if request.method == 'POST':
        return handler.addUserToGroupChat(gc_id, user_id)
    elif request.method == 'DELETE':
        return handler.deleteUserFromGroupChat(gc_id, user_id)
    else:
        jsonify(Error = "Method not allowed"), 405

@app.route('/Sheeple/groupchats/user/<int:user_id>', methods=['GET'])
def getGroupchatsForUser(user_id):
    handler = groupChatHandler()
    if request.method == 'GET':
        return handler.getGroupChatsForUser(user_id)
    else:
        return jsonify(Error="Method not allowed"), 405

# -------------------------End Groupchats--------------------------#

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
        return handler.updatePost(post_id, request.args)
    elif request.method == 'DELETE':
        return handler.deletePost(post_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Sheeple/posts/<int:post_id>/likes', methods=['GET'])
def getUsersWhoLikesPost(post_id):
    handler = postHandler()

    if request.method == 'GET':
        return handler.getUserWhoLikesPost(post_id)

    else:
        return jsonify(Error="Method not allowed"), 405

# See the photos, the original message that came with the photo, and any replies
@app.route('/Sheeple/posts-and-replies', methods=['GET'])
def doGetPostsReplies():
    handler = postHandler()
    if request.method == 'GET':
       return handler.getPostsReplies()
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/Sheeple/posts/<int:post_id>/dislikes', methods=['GET'])
def getUsersWhoDisikesPost(post_id):
    handler = postHandler()

    if request.method == 'GET':
        return handler.getUserWhoDislikesPost(post_id)

    else:
        return jsonify(Error="Method not allowed"), 405

# Like or dislike a photo posted on a chat group:
@app.route('/Sheeple/posts/<int:post_id>/<string:reaction_type>/<int:user_id>', methods=['POST'])
def reactPost(post_id, reaction_type, user_id):
    handler = postHandler()
    if request.method == 'POST':
        return handler.reactPost(post_id, reaction_type, user_id)
    else:
        return jsonify(Error="Method not allowed."), 405

# Reply to the original photo message posted on a chat group
@app.route('/Sheeple/posts/<int:post_id>/reply/<int:original>', methods= ['POST'])
def replyPost(post_id, original):
    handler = postHandler()
    if request.method == 'POST':
        return handler.replyPost(post_id, original, request.args)
    else:
        return jsonify(Error="Method not allowed."), 405
# -----------------------------End Post-------------------------------#


# ---------------------------Start Users----------------------------#
@app.route('/Sheeple/users', methods=['GET', 'POST'])
def getAllUsers():
    handler = userHandler()
    if request.method == 'GET':
        if request.args:
            return handler.searchUsers(request.args)
        else:
            return handler.getAllUsers()
    else:
        return handler.createUser(request.args)


@app.route('/Sheeple/users/<int:user_id>', methods=['GET', 'PUT', "DELETE"])
def doUsersById(user_id):
    handler = userHandler()
    if request.method == 'GET':
        return handler.getUserByID(user_id)
    elif request.method == 'PUT':
        return handler.updateUser(user_id, request.args)
    else:
        return handler.deleteUser(user_id)

# -----------------------------End Users-------------------------------#



if __name__ == '__main__':
    app.run()