from flask import jsonify, request, Response, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

class MoviesApi(Resource):
    def get(self):
        return jsonify(movies)

    def post(self):
        movie = request.get_json()
        movies.append(movie)
        return {'id': len(movies)-1}, 200

class MovieApi(Resource):
    def put(self,id):
        movie = request.get_json()
        movies[id] = movie
        return make_response(jsonify(movies[id]),200)
    
    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        movies.pop(id)
        return make_response(jsonify({'status':'Eliminado'}, {'Eliminado por':current_user}), 200)
