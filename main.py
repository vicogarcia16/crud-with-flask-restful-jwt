from flask import Flask
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

api.add_resource(Usuario, '/saludo/<name>')
initialize_routes(api)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run(debug=True)