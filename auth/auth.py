
from flask import jsonify, make_response
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import jwt_required, get_jwt_identity
import os



class Login(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
    
        if username != os.environ.get("USER") or password != os.environ.get("PASS"):
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username,fresh=True)
        refresh_token = create_refresh_token(identity=username)
        return make_response(jsonify(access_token=access_token,refresh_token=refresh_token))


class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        return jsonify(access_token=access_token)


    