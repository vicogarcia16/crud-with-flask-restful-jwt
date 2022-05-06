from flask import Blueprint, jsonify
from routes.movies import MoviesApi, MovieApi 
from auth.auth import Login, Refresh
user = Blueprint('user', __name__)

@user.route('/user/<name>')
def get_user(name):
    return jsonify({'Usuario': name})


def initialize_routes(api):
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<int:id>')
    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')