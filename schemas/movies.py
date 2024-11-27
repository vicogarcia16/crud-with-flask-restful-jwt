from marshmallow import Schema, fields

class MovieSchema(Schema):
    name = fields.Str()
    casts = fields.List(fields.Str())
    genres = fields.List(fields.Str())