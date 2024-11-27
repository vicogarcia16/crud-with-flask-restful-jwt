from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_apispec.views import MethodResource
from flask_apispec import use_kwargs, marshal_with, doc
from schemas.movies import MovieSchema

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

class MoviesApi(MethodResource):
    @doc(description="Obtener todas las películas", tags=["Movies"], security = [])
    @marshal_with(MovieSchema(many=True))  # Serializa una lista de películas
    def get(self):
        return movies

    @doc(description="Agregar una nueva película", tags=["Movies"], security = [])
    @use_kwargs(MovieSchema, location="json")  # Extrae los datos del cuerpo JSON
    @marshal_with(None)  # Sin respuesta estructurada
    def post(self, **kwargs):
        movie = kwargs  # kwargs contendrá el JSON validado
        movies.append(movie)
        return {'id': len(movies) - 1}, 201

class MovieApi(MethodResource):
    @doc(description="Obtener una película por ID", id="id", tags=["Movies"], security = [])
    @marshal_with(MovieSchema)  # Serializa una película individual
    def get(self, id):
        if id < 0 or id >= len(movies):
            return {"error": "Película no encontrada"}, 404
        return movies[id]

    @doc(description="Actualizar una película por ID", tags=["Movies"], security = [])
    @use_kwargs(MovieSchema, location="json")
    @marshal_with(MovieSchema)  # Serializa la película actualizada
    def put(self, id, **kwargs):
        if id < 0 or id >= len(movies):
            return {"error": "Película no encontrada"}, 404
        movies[id] = kwargs
        return movies[id]

    @doc(
        description="Eliminar una película por ID",
        tags=["Movies"],
        security=[{"ApiKeyAuth": []}]  # Aplica el esquema de seguridad JWT
    )
    @jwt_required()
    def delete(self, id):
        if id < 0 or id >= len(movies):
            return {"error": "Película no encontrada"}, 404
        current_user = get_jwt_identity()
        movies.pop(id)
        return {'status': 'Eliminado', 'Eliminado por': current_user}, 200
