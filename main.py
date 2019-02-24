from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from handlers.convoHandler import convoHandler
from handlers.personHandler import personHandler


app = Flask(__name__)

CORS(app)


@app.route('/')
def welcomesheeple():
    return 'Sheeple!'


@app.route('/Sheeple/conversations', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getAllConvos():
    # if request.method == 'POST':
    #  print("REQUEST: ", request.json)
    #   return convoHandler().insertConvoJson(request.json)
    # elif request.method == 'GET':
    #   print("REQUEST: ", request.json)
    #  return convoHandler().getConvoJson(request.json)
    # elif request.method == 'PUT':
    #   print("REQUEST: ", request.json)
    #    return convoHandler().putConvoJson(request.json)
    # else:
    handler = convoHandler()
    return handler.getAllConvos()

# @app.route('/Sheeple/conversations/<int=id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

# @app.route('/Sheeple/contacts/')


@app.route('/Sheeple/person', methods=['GET'])
def gettAllPeople():
    handler = personHandler()
    return handler.getAllPeople()


if __name__ == '__main__':
    app.run()
