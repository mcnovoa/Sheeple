from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler
from handlers.personHandler import personHandler
from handlers.userHandler import userHandler
from handlers.replyHandler import replyHandler
from handlers.adminHandler import AdminHandler
from handlers.reactionHandler import reactionHandler
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


@app.route('/Sheeple/conversations/<int:convo_id>/users', methods=['GET'])
def getAllUsers(convo_id):
    handler = convoHandler()
    if request.method == 'GET':
        return handler.geAllUsers(convo_id)


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

@app.route('/Sheeple/posts/replies', methods=['GET', 'POST'])
def searchReplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return 200

    else:
        handler = replyHandler()
        if not request.args:
            return handler.getAllReplies()
        else:
            return handler.searchReplies(request.args)


@app.route('/Sheeple/posts/replies/<int:id>', methods=['GET'])
def getRepliesById(id):
    handler = replyHandler()
    return handler.getReplyById(id)


@app.route('/Sheeple/posts/replies/user/<int:userId>')
def getRepliesByUserId(userId):
    handler = replyHandler()
    return handler.getReplyByUserId(userId)

#----------------------------End Replies-----------------------#

#----------------------------Start Admins----------------------#

@app.route('/Sheeple/users/admins', methods=['GET'])
def getAllAdmins():
    if request.method == 'POST':
        print("REQUEST: ", request.json)

    else:
        handler = AdminHandler()
        return handler.getAllAdmins()


@app.route('/Sheeple/users/admins/<int:id>', methods=['GET'])
def getAdminById(id):
    handler = AdminHandler()
    return handler.getAdminById(id)

#----------------------------End Admins-----------------------#

#------------------------Start Reactions----------------------#


@app.route('/Sheeple/reactions', methods=['GET','POST', 'PUT', 'DELETE'])
def getAllReactions():
    handler = reactionHandler()
    if request.methods =='GET':
        if not request.args:
            return handler.getAllReactions()
        else:
            return handler.searchReactions()
    # elif request.method == 'POST':
    #     return handler.postReaction()
    # elif request.method == 'PUT'
    #     return handler.updateReaction()
    # else:
    #     return handler.deleteReacion()

    return handler.getAllReactions()

@app.route('/Sheeple/reactions/<int:id>')
def getReactionById(id):
    handler = reactionHandler
    return handler.getReactionById(id)



#--------------------------End Reactions-----------------------#


@app.route('/Sheeple/users/<int:user_id>', methods=['GET'])
def getUsersById(user_id):
    handler = userHandler()
    return handler.getUserByID(user_id)



if __name__ == '__main__':
    app.run()
