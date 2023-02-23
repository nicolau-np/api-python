from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [
    {
        'id':1,
        'title': 'Obras'
    },{
        'id':2,
        'title': 'Caras'
    },{
        'id':3,
        'title': 'Roubos'
    },
]

@app.route('/', methods=['GET'])
def home():
    return jsonify(dados)

