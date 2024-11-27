from flask import Blueprint, render_template
from routes.movies import MoviesApi, MovieApi 
from auth.auth import Login, Refresh
from flask_jwt_extended import jwt_required
from flask_apispec import doc

user = Blueprint('user', __name__)


@user.route('/user/<name>', methods=['GET'], provide_automatic_options=False)
@doc(description="Obtener información del usuario", tags=["User"], 
     security = [{"ApiKeyAuth": []}], methods = ['GET'])
@jwt_required()
def get_user(name):
    data= [
        {'id':1, 'texto': 'dato'},
        {'id':2,'texto': 'dato2'},
        {'id':3, 'texto': 'dato3'}
    ]

    enlaces=[{"id":1,"url":"http://www.google.com","texto":"Google"},
			{"id":2,"url":"http://www.twitter.com","texto":"Twitter"},
			{"id":3,"url":"http://www.facebook.com","texto":"Facebook"},
			]

    return render_template('index.html', name=name, data=data, enlaces=enlaces)

def initialize_routes(api):
    api.add_resource(MoviesApi, '/movies')
    api.add_resource(MovieApi, '/movies/<int:id>')
    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')


    
