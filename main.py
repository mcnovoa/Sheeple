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


@app.route('/Sheeple/person', methods=['GET', 'POST', 'PUT', "DELETE"])
def gettAllPeople():
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


@app.route('/Sheeple/person/<int:person_id>', methods=['GET'])
def getPersonById(person_id):
    handler = personHandler()
    return handler.getPersonByID(person_id)


if __name__ == '__main__':
    app.run()
