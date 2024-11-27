from schemas.auth import LoginResponseSchema, LoginRequestSchema, RefreshResponseSchema
from flask import jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, get_jwt_identity)
import os
from flask_apispec.views import MethodResource
from flask_apispec import use_kwargs, marshal_with, doc

class Login(MethodResource):
    @doc(description="Autenticación de usuario", tags=["Auth"], 
         security=[])
    @use_kwargs(LoginRequestSchema, location="json")
    @marshal_with(LoginResponseSchema)
    def post(self, username, password):
        if username != os.environ.get("USER") or password != os.environ.get("PASS"):
            return jsonify({"msg": "Bad username or password"}), 401
        data =  username
        access_token = create_access_token(identity=data, fresh=True)
        refresh_token = create_refresh_token(identity=data)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200

class Refresh(MethodResource):
    @doc(description="Refrescar el token de acceso", tags=["Auth"], 
         security=[{"ApiKeyAuth": []}])
    @marshal_with(RefreshResponseSchema)
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        return {"access_token": access_token}, 200


    