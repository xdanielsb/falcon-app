from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class PathInfo:
    autonomy: int
    departure: str
    arrival: str
    routes_db: str


class PathInfoSchema(Schema):
    autonomy = fields.Int(required=True)
    departure = fields.Str(required=True)
    arrival = fields.Str(required=True)
    routes_db = fields.Str(required=True)

    @post_load
    def make_route_info(self, data, **kwargs):
        return PathInfo(**data)
