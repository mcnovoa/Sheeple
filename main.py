from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import handlers.convoHandler

app = Flask(__name__)

CORS(app)

@app.route('/')
def welcomeShepple():
    return 'Shepple!'

#app.route(
app.route('/Sheeple/conversations/', methods=['GET', 'POST', 'PUT', 'DELETE' ])
    def getAllConvos():
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return convoHandler().insertConvoJson(request.json)
        elif request.method == 'GET':
            print("REQUEST: ", request.json)
            return convoHandler().getConvoJson(request.json)
        elif request.method == 'POST':
            print("REQUEST: ", request.json)
            return convoHandler().putConvoJson(request.json)
        else:
            if not request.args:
            return convoHandler().getAllConvos()
        else:
            return convoHandler().searchConvos(request.args)



#@app.route('/Sheeple/contacts/')

if __name__ == '__main__':
    app.run()

