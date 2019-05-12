from flask import jsonify, request, abort

from . import app


@app.route('/movies', methods=['POST', 'GET'])
def movies():
    if request.method == 'GET':
        return jsonify({"message": "success"})