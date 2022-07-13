from flask import Flask, jsonify
from flask_restful import Api, Resource
from routes.routes import user, initialize_routes
from flask_jwt_extended import JWTManager
from datetime import timedelta


import os

app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)
api = Api(app)
#jwt._set_error_handler_callbacks(app)
class Usuario(Resource):
    def get(self, name):
        return f'Welcome {name}'

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
    return f'Welcome {name}'

@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify(error="True", msg="Token a expirado, favor de refrescar"), 200


api.add_resource(Usuario, '/saludo/<name>')
initialize_routes(api)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run(debug=True)