import uuid
from ninja.schema import Schema


class InPerson(Schema):
    email: str = None
    name: str
    address: str = None
    city: str = None
    departament: str = None
    identity_card: str = None


class OutPerson(Schema):
    id: uuid.UUID = None
    email: str = None
    name: str = None
    address: str = None
    city: str = None
    departament: str = None
    identity_card: str = None


class NotFoundSchema(Schema):
    msg: str
