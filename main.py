from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler
from handlers.personHandler import personHandler
from handlers.userHandler import userHandler
from handlers.replyHandler import replyHandler
from handlers.adminHandler import adminHandler
from handlers.reactionHandler import reactionHandler
from handlers.hashtagHandler import hashtagHandler
app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomesheeple():
    return 'Sheeple!'


@app.route('/Sheeple/conversations', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getAllConvos():
    handler = convoHandler()
    return handler.getAllConvos()


@app.route('/Sheeple/people', methods=['GET', 'POST', 'PUT', "DELETE"])
def getAllPeople():
    if request.method == 'GET':
        if request.args:
            return personHandler().searchPeople(request.args)
        else:
            handler = personHandler()
            return handler.getAllPeople()
    elif request.method == 'POST':
        return personHandler().postPerson()
    elif request.method == 'PUT':
        return personHandler().updatePerson()
    else:
        return personHandler().deletePerson()


@app.route('/Sheeple/people/<int:person_id>', methods=['GET'])
def getPersonById(person_id):
    handler = personHandler()
    return handler.getPersonByID(person_id)

    if request.args:
        return handler.searchByArgs(request.args)
    else:
        return handler.getAllConvos()

@app.route('/Sheeple/conversations/<int:convo_id>', methods=['GET', 'PUT', 'DELETE'])
def getConvoById(convo_id):
     handler = convoHandler()
     if request.method == 'GET':
        return convoHandler().getConvoById(convo_id)
     elif request.method == 'PUT':
        return convoHandler().updateConvo(convo_id, request.form)
     elif request.method == 'DELETE':
        return convoHandler().deleteConvo(convo_id)
     else:
        return jsonify(Error="Method not allowed."), 405
     if request.args:
         return handler.searchArgsById(convo_id, request.args)


# @app.route('/Sheeple/conversations/<int:convo_id>/users', methods=['GET'])
# def getAllUsers(convo_id):
#     handler = convoHandler()
#     if request.method == 'GET':
#         return handler.geAllUsers(convo_id)


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


@app.route('/Sheeple/users/admins', methods=['GET', 'POST', 'PUT', 'DELETE'])
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
            return reactionHandler.searchReactions(request.args)
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
            return hashtagHandler.searchHashtags(request.args)
        else:
            handler = hashtagHandler()
            return handler.getAllHashtags()
    elif request.method == 'POST':
        return handler.postReaction()
    elif request.method == 'PUT':
        return handler.updateReaction()
    else:
        return handler.deleteReaction()



@app.route('/Sheeple/hashtags/<int:id>', methods=['GET'])
def getHashtagById(id):
    handler = hashtagHandler()
    return handler.getHashtagById(id)

#------------------------End Hashtag---------------------------#

@app.route('/Sheeple/users/<int:user_id>', methods=['GET'])
def getUsersById(user_id):
    handler = userHandler()
    return handler.getUserByID(user_id)



if __name__ == '__main__':
    app.run()
