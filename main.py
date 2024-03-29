from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler
from handlers.personHandler import personHandler
from handlers.userHandler import userHandler
from handlers.replyHandler import replyHandler
from handlers.adminHandler import adminHandler
from handlers.reactionHandler import reactionHandler
from handlers.contactHandler import ContactHandler
from handlers.messageHandler import messageHandler
from handlers.imageHandler import imageHandler
from handlers.postHandler import postHandler
from handlers.contactListHandler import contactListHandler
from handlers.hashtagHandler import hashtagHandler

app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomesheeple():
    return 'Sheeple!'


# --------------------------Start People------------------------#
@app.route('/Sheeple/people', methods=['GET'])
def getAllPeople():
    if request.args:
        return personHandler().searchPeople(request.args)
    else:
        handler = personHandler()
        return handler.getAllPeople()


@app.route('/Sheeple/people/<int:person_id>', methods=['GET', 'POST', 'PUT', "DELETE"])
def getPersonById(person_id):
    handler = personHandler()
    if request.method == 'GET':
        return handler.getPersonByID(person_id)
    elif request.method == 'POST':
        return personHandler().postPerson()
    elif request.method == 'PUT':
        return personHandler().updatePerson()
    else:
        return personHandler().deletePerson()


# -------------------------End People--------------------------#

# ---------------------Start Conversation----------------------#
@app.route('/Sheeple/conversations', methods=['GET'])
def getAllConvos():
    handler = convoHandler()
    if request.args:
        return handler.searchByArgs(request.args)
    else:
        return handler.getAllConvos()


@app.route('/Sheeple/conversations/<int:convo_id>', methods=['GET', 'POST','PUT', 'DELETE'])
def doByConvoId(convo_id):
     handler = convoHandler()
     if request.method == 'GET':
        return convoHandler().getConvoById(convo_id)
     elif request.method == 'POST':
        return convoHandler().postConvo(convo_id)
     elif request.method == 'PUT':
        return convoHandler().updateConvo(convo_id, request.form)
     elif request.method == 'DELETE':
        return convoHandler().deleteConvo(convo_id)
     else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/conversations/<int:convo_id>/users', methods=['GET'])
def getAllConvoUsers(convo_id):
     handler = convoHandler()
     if request.method == 'GET':
         return handler.getAllConvoUsers(convo_id)
     else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/Sheeple/conversations/<int:convo_id>/posts/<int:post_id>/<string:reply_content>', methods=['POST'])
def replyP(convo_id, post_id, reply_content):
     handler = convoHandler()
     if request.method == 'POST':
         return handler.replyPost(convo_id, post_id, reply_content)
     else:
        return jsonify(Error="Method not allowed."), 405
#-------------------------End Conversations--------------------------#

#---------------------------Start Post-------------------------------#


@app.route('/Sheeple/posts/<int:post_id>', methods=['GET','PUT', 'DELETE'])
def doByPostId(post_id):
     handler = postHandler()
     if request.method == 'GET':
        return handler.getPostById(post_id)
     elif request.method == 'PUT':
        return handler.updatePost(post_id, request.form)
     elif request.method == 'DELETE':
        return handler.deletePost([post_id])
     else:
        return jsonify(Error="Method not allowed."), 405
@app.route('/Sheeple/posts', methods=['GET'])
def getAllPosts():
    handler = postHandler()
    if request.args:
        return handler.searchByArgs(request.args)
    else:
        return handler.getAllPosts()
@app.route('/Sheeple/posts/<int:post_id>/<string:post_content>/<int:user_id>/<int:convo_id>',methods=['POST'])
def postP(post_id, post_content, user_id, convo_id):
    handler = postHandler()
    if request.method == 'POST':
        return handler.postPost(post_id,post_content,user_id,convo_id)
    else:
        return jsonify(Error="Method not allowed."), 405
@app.route('/Sheeple/posts/<int:post_id>/<string:type>/<int:user_id>' ,methods=['POST'])
def reactP(post_id, type, user_id):
    handler = postHandler()
    if request.method == 'POST':
        return handler.reactPost(post_id, type, user_id)
    else:
        return jsonify(Error="Method not allowed."), 405
#-----------------------------End Post-------------------------------#
#--------------------------Start Message-----------------------------#
@app.route('/Sheeple/messages', methods=['GET'])
def getAllMessages():
        handler = messageHandler()
        if request.args:
            return handler.searchMessagesByArgs(request.args)
        else:
            return handler.getAllMessages()
@app.route('/Sheeple/messages/<int:message_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doByMessageId(message_id):
    handler = messageHandler()
    if request.method == 'GET':
        return handler.getMessageById(message_id)
    elif request.method == 'POST':
        return handler.postMessage(message_id)
    elif request.method == 'PUT':
        return handler.updateMessage(message_id, request.form)
    elif request.method == 'DELETE':
        return handler.deleteMessage(message_id)
    else:
        return jsonify(Error="Method not allowed."), 405

#----------------------------End Message----------------------------#

#---------------------------Start Image-----------------------------#
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
        return handler.postImage(image_id)
    elif request.method == 'PUT':
        return handler.updateImage(image_id, request.form)
    elif request.method == 'DELETE':
        return handler.deleteImage(image_id)
    else:
        return jsonify(Error="Method not allowed."), 405
#---------------------------End Message---------------------------#

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


# -------------------------Ends Users--------------------------#

#--------------------------Start Replies------------------------#
@app.route('/Sheeple/replies', methods=['GET', 'POST','PUT','DELETE'])
def searchReplies():
    if request.method == 'GET':
        if request.args:
            return replyHandler().searchReplies(request.args)
        else:
            handler = replyHandler()
            return handler.getAllReplies()
    elif request.method == 'POST':
        return replyHandler().postReply()
    elif request.method == 'PUT':
        return replyHandler().updateReply()
    else:
        return replyHandler().deleteReply()


@app.route('/Sheeple/replies/<int:id>', methods=['GET'])
def getRepliesById(id):
    handler = replyHandler()
    return handler.getReplyById(id)


@app.route('/Sheeple/replies/user/<int:userId>')
def getRepliesByUserId(userId):
    handler = replyHandler()
    return handler.getReplyByUserId(userId)

#----------------------------End Replies-----------------------#

#----------------------------Start Admins----------------------#


@app.route('/Sheeple/admins', methods=['GET', 'POST', 'PUT', 'DELETE'])
def searchAdmins():
    handler = adminHandler()
    if request.method == 'GET':
        if request.args:
            return handler.searchAdmins(request.args)
        else:
            return handler.getAllAdmins()
    elif request.method == 'POST':
        return adminHandler().postAdmin()
    elif request.method == 'PUT':
        return adminHandler().updateAdmin()
    else:
        return adminHandler().deleteAdmin()


@app.route('/Sheeple/admins/<int:id>', methods=['GET'])
def getAdminById(id):
    handler = adminHandler()
    return handler.getAdminById(id)

#----------------------------End Admins-----------------------#

#------------------------Start Reactions----------------------#



@app.route('/Sheeple/reactions', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getAllReactions():
    handler = reactionHandler()
    if request.method == 'GET':
        if request.args:
            return handler.searchReactions(request.args)
        else:
            handler = reactionHandler()
            return handler.getAllReactions()
    elif request.method == 'POST':
        return handler.postReaction()
    elif request.method == 'PUT':
        return handler.updateReaction()
    else:
        return handler.deleteReaction()



@app.route('/Sheeple/reactions/<int:id>', methods=['GET'])
def getReactionById(id):
    handler = reactionHandler()
    return handler.getReactionById(id)


#--------------------------End Reactions-----------------------#

#------------------------Start Hashtag-------------------------#

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

#------------------------End Hashtag---------------------------#


# ---------------------------Start Contacts----------------------------#
@app.route('/Sheeple/contacts', methods=['GET'])
def getAllContacts():
    if request.args:
        return ContactHandler().searchContacts(request.args)
    else:
        handler = ContactHandler()
        return handler.getAllContacts()


@app.route('/Sheeple/contacts/<int:contact_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doContactById(contact_id):
    handler = ContactHandler()
    if request.method == 'GET':
        return handler.getContactById(contact_id)
    elif request.method == 'POST':
        return ContactHandler().postContact()
    elif request.method == 'PUT':
        return ContactHandler().updateContact()
    else:
        return ContactHandler().deleteContact()


# -------------------------End Contacts--------------------------#


# ---------------------------Start Contact Lists----------------------------#
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


if __name__ == '__main__':
    app.run()