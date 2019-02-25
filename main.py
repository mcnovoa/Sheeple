from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler

app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomesheeple():
    return 'Sheeple!'


@app.route('/Sheeple/conversations', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getAllConvos():
    handler = convoHandler()
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


if __name__ == '__main__':
    app.run()
