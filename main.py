from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler
from handlers.replyHandler import replyHandler
from handlers.adminHandler import AdminHandler

app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomeSheeple():
    return 'Sheeple!'


app.route('/Sheeple/conversations/', methods=['GET', 'POST', 'PUT', 'DELETE' ])
def getAllConvos():
        # if request.method == 'POST':
        #     print("REQUEST: ", request.json)
        #     return convoHandler().insertConvoJson(request.json)
        # elif request.method == 'GET':
        #     print("REQUEST: ", request.json)
        #     return convoHandler().getConvoJson(request.json)
        # elif request.method == 'POST':
        #     print("REQUEST: ", request.json)
        #     return convoHandler().putConvoJson(request.json)
        # else:
        #     if not request.args:
        #         return convoHandler().getAllConvos()
        #     else:
                 return convoHandler().searchConvos(request.args)


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


@app.route('/Sheeple/users/admins', methods=['GET'])
def getAllAdmins():
    if request.method == 'POST':
        print("REQUEST: ", request.json)

    else:
        handler = AdminHandler()
        return handler.getAllAdmins()


# @app.route('/Sheeple/users/admins/<int:id>', methods='GET')
# def getAdminById(id):
#     handler = AdminHandler()
#     return handler.getAdminById()


#@app.route('/Sheeple/contacts/')


if __name__ == '__main__':
    app.run()

