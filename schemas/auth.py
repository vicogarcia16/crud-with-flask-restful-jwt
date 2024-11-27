from marshmallow import Schema, fields

class LoginRequestSchema(Schema):
    username = fields.String(required=True, description="Nombre de usuario")
    password = fields.String(required=True, description="Contraseña")

# Esquema para la respuesta de Login
class LoginResponseSchema(Schema):
    access_token = fields.String(description="Token de acceso JWT")
    refresh_token = fields.String(description="Token de refresco JWT")
    
class RefreshResponseSchema(Schema):
    access_token = fields.String(description="Nuevo token de acceso JWT")