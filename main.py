from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

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
            return ConvoHandler().insertConvoJson(request.json)
        elif request.method == 'GET':
            print("REQUEST: ", request.json)
            return ConvoHandler().getConvoJson(request.json)
        elif request.method == 'POST':
            print("REQUEST: ", request.json)
            return ConvoHandler().putConvoJson(request.json)
#@app.route('/Sheeple/contacts/')

if __name__ == '__main__':
    app.run()

