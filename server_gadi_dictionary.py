# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify, abort, request, make_response
app = Flask(__name__)
api = Api(app)

DICTIONARY = [
    {
        'id': 1,
        'ca': u'Oju',
        'es': u'Vaya'
    },
    {
        'id': 2,
        'ca': u'Bastinazo',
        'es': u'Tremendo'
    },
    {
        'id': 3,
        'ca': u'Killo',
        'es': u'Cabesa'
    },
    {
        'id': 4,
        'ca': u'Pixa',
        'es': u'Conocido'
    }

]

# Devuelve todas las definiciones
@app.route('/', methods=['GET'])
@app.route('/palabras', methods=['GET'])
def get_words():
    return jsonify({'DICTIONARY': DICTIONARY})


# Conversión de una palabra en gaditano a español
@app.route('/ga_es/<string:p_ca>', methods=['GET'])
def get_word_es(p_ca):
    p_es = [palabra for palabra in DICTIONARY if palabra['ca'] == p_ca]
    if len(p_es) == 0:
        abort(404)
    return jsonify({'palabra': p_es[0]['es']})

# Conversión de una palabra del español al gaditano
@app.route('/es_ga/<string:p_es>', methods=['GET'])
def get_word_ga(p_es):
    p_ga = [palabra for palabra in DICTIONARY if palabra['es'] == p_es]
    if len(p_ga) == 0:
        abort(404)
    return jsonify({'palabra': p_ga[0]['ca']})

# Eliminar entrada dada una id
@app.route('/palabra/<int:palabra_id>', methods=['DELETE'])
def delete_word(palabra_id):
    palabra = [palabra for palabra in DICTIONARY if palabra['id'] == palabra_id]
    if len(palabra) == 0:
        abort(404)
    DICTIONARY.remove(palabra[0])
    return jsonify({'result': True})

# Crear una nueva palabra
@app.route('/palabras', methods=['POST'])
def create_word():
    if not request.json or not 'ca' in request.json:
        abort(400)
    palabra = {
        'id': DICTIONARY[-1]['id'] + 1,
        'ca': request.json['ca'],
        'es': request.json['es'],
    }
    DICTIONARY.append(palabra)
    return jsonify({'palabra': palabra}), 201

# Actualizar el diccionario
@app.route('/palabras/<int:palabra_id>', methods=['PUT'])
def update_word(palabra_id):
    palabra = [palabra for palabra in DICTIONARY if palabra['id'] == palabra_id]
    if len(palabra) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'es' in request.json and type(request.json['es']) is not unicode:
        abort(400)
    if 'ca' in request.json and type(request.json['es']) is not unicode:
        abort(400)
    palabra[0]['es'] = request.json['es']
    palabra[0]['ga'] = request.json['ga']
    return jsonify({'palabra': palabra[0]})

# Captura errores
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)