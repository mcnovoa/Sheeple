from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler
from handlers.personHandler import personHandler
from handlers.userHandler import userHandler
from handlers.replyHandler import replyHandler
from handlers.adminHandler import AdminHandler
from handlers.contactHandler import ContactHandler
from handlers.messageHandler import messageHandler
from handlers.imageHandler import imageHandler
from handlers.contactListHandler import contactListHandler

app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomesheeple():
    return 'Sheeple!'

#--------------------------Start People------------------------#


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

#-------------------------End Conversations--------------------------#


#--------------------------Start Conversations------------------------#
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
     if request.args:
         return handler.searchArgsById(convo_id, request.args)


@app.route('/Sheeple/conversations/<int:convo_id>/users', methods=['GET'])
def getAllConvoUsers(convo_id):
     handler = convoHandler()
     if request.method == 'GET':
         return handler.getAllConvoUsers(convo_id)

#-------------------------End Conversations--------------------------#

#---------------------------Start Message----------------------------#
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

#----------------------------End Messages---------------------------#


#---------------------------Start Images----------------------------#
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

#---------------------------End Messages---------------------------#

#---------------------------Start Users----------------------------#
@app.route('/Sheeple/users', methods=['GET'])
def getAllUsers():
    if request.args:
        return userHandler().searchUsers(request.args)
    else:
        handler = userHandler()
        return handler.getAllUsers()


@app.route('/Sheeple/users/<int:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def doUsersById(user_id):
    if request.method == 'GET':
        handler = userHandler()
        return handler.getUserByID(user_id)
    elif request.method == 'POST':
        return userHandler().postUser()
    elif request.method == 'PUT':
        return userHandler().updateUser()
    else:
        return userHandler().deleteUser()

#-------------------------Ends Users--------------------------#

#------------------------Start Replies-------------------------#

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


#---------------------------Start Contacts----------------------------#


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

#-------------------------End Contacts--------------------------#

#---------------------------Start Contact Lists----------------------------#


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
    return jsonify(DeletedUser = 'OK'), 200

#-------------------------End Contact Lists--------------------------#



if __name__ == '__main__':
    app.run()