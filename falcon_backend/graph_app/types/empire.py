from dataclasses import dataclass, field

from marshmallow import Schema, post_load, fields


# dataclasses for the empire


@dataclass
class BountyHunterWithPlanetId:
    day: int
    node_id: int


@dataclass
class BountyHunterDC:
    day: int
    planet: str


@dataclass
class EmpireDC:
    countdown: int
    bounty_hunters: list[BountyHunterDC] = field(default_factory=list)


# validation schemas


class BountyHunterSchema(Schema):
    day = fields.Int(required=True)
    planet = fields.Str(required=True)

    @post_load
    def make_bounty_hunter(self, data, **kwargs):
        return BountyHunterDC(**data)


class EmpireSchema(Schema):
    countdown = fields.Int(required=True)
    bounty_hunters = fields.List(fields.Nested(BountyHunterSchema), required=True)

    @post_load
    def make_empire(self, data, **kwargs):
        return EmpireDC(**data)
