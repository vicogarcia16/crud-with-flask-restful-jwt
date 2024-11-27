from flask import Flask, jsonify
from flask_restful import Api, Resource
from routes.routes import user, initialize_routes, get_user
from flask_jwt_extended import JWTManager
from datetime import timedelta
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import FlaskApiSpec
from auth.auth import Login, Refresh
from routes.movies import MoviesApi, MovieApi
import os

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
    title="ApiSpec",
    version='v1',
    openapi_version='2.0.0',
    plugins=[MarshmallowPlugin()]
),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URL para Swagger
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'# Interfaz Swagger
})

docs = FlaskApiSpec(app)
#jwt._set_error_handler_callbacks(app)

security_scheme_api_key = {
    "type": "apiKey",
    "in": "header",
    "name": "Authorization"
}

docs.spec.components.security_scheme("ApiKeyAuth", security_scheme_api_key)

class Usuario(Resource):
    def get(self, name):
        return {'Hello': name}

@app.route('/')
def saludo():
    data= {
        '1': 'dato',
        '2': 'dato2',
        '3': 'dato3'
    }
    return {'data':data,'Hola': 'Mundito'}

@app.route('/welcome/<name>', methods=['GET'])
def welcome(name):
    return jsonify(f'Welcome {name}')

@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify(error="True", msg="Token a expirado, favor de refrescar"), 200


api.add_resource(Usuario, '/saludo/<name>')
initialize_routes(api)
app.register_blueprint(user)

docs.register(get_user, blueprint='user')
docs.register(MoviesApi)
docs.register(MovieApi)
docs.register(Login)
docs.register(Refresh)

if __name__ == '__main__':
    app.run(debug=True)