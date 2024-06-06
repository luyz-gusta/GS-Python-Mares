from flask import Flask, jsonify, request, abort
import json
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = True
CORS(app, origins='*')

with open('./mares.json', encoding='utf-8') as f:
    mares = json.load(f)

def save_mares():
    with open('mares.json', 'w') as f:
        json.dump(mares, f)

@app.route('/', methods=['GET'])
def start():
    return jsonify({"message": "Olá! Bem vindo ao backend da OceanGuardian." }
 )
    
@app.route('/get_mares', methods=['GET'])
def todos_mares():
    return jsonify(mares)

@app.route('/get_mar/<int:mar_id>', methods=['GET'])
def get_mar(mar_id):
    mar_encontrado = None
    for mar in mares:
        if mar['id'] == mar_id:
            mar_encontrado = mar
            break

    if mar_encontrado is None:
        abort(404, description="Mar não encontrado")

    return jsonify(mar_encontrado)

@app.route('/add_mar', methods=['POST'])
def add_mar():
    if not request.json or not 'nome' in request.json:
        abort(400, description="Dados inválidos")

    novo_mar = {
        'id': mares[-1]['id'] + 1 if mares else 1,
        'nome': request.json['nome'],
        'localizacao': request.json.get('localizacao', ""),
        'ph': request.json.get('ph', 0),
        'turbidez': request.json.get('turbidez', 0),
        'temperatura': request.json.get('temperatura', 0)
    }
    mares.append(novo_mar)
    save_mares()
    return jsonify(novo_mar), 201

@app.route('/update_mar/<int:mar_id>', methods=['PUT'])
def update_mar(mar_id):
    mar_encontrado = None
    for mar in mares:
        if mar['id'] == mar_id:
            mar_encontrado = mar
            break

    if mar_encontrado is None:
        abort(404, description="Mar não encontrado")

    if not request.json:
        abort(400, description="Dados inválidos")

    mar_encontrado['nome'] = request.json.get('nome', mar_encontrado['nome'])
    mar_encontrado['localizacao'] = request.json.get('localizacao', mar_encontrado['localizacao'])
    mar_encontrado['ph'] = request.json.get('ph', mar_encontrado['ph'])
    mar_encontrado['turbidez'] = request.json.get('turbidez', mar_encontrado['turbidez'])
    mar_encontrado['temperatura'] = request.json.get('temperatura', mar_encontrado['temperatura'])

    save_mares()
    return jsonify(mar_encontrado)

@app.route('/delete_mar/<int:mar_id>', methods=['DELETE'])
def delete_mar(mar_id):
    mar_encontrado = None
    for mar in mares:
        if mar['id'] == mar_id:
            mar_encontrado = mar
            break

    if mar_encontrado is None:
        abort(404, description="Mar não encontrado")

    mares.remove(mar_encontrado)
    save_mares()
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(port=5000)
