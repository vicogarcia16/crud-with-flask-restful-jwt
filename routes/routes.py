from flask import Blueprint, jsonify, render_template
from routes.movies import MoviesApi, MovieApi 
from auth.auth import Login, Refresh
user = Blueprint('user', __name__)

@user.route('/user/<name>')
def get_user(name):
    data= [
        {'id':1, 'texto': 'dato'},
        {'id':2,'texto': 'dato2'},
        {'id':3, 'texto': 'dato3'}
    ]

    enlaces=[{"url":"http://www.google.es","texto":"Google"},
			{"url":"http://www.twitter.com","texto":"Twitter"},
			{"url":"http://www.facbook.com","texto":"Facebook"},
			]

    return render_template('index.html', name=name, data=data, enlaces=enlaces)


def initialize_routes(api):
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<int:id>')
    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')