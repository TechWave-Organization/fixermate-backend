import uuid
from ninja.schema import Schema


class InPerson(Schema):
	email: str = None
	name: str
	address: str = None
	city: str = None
	departament: str = None
	identity_card: int = None

class OutPerson(Schema):
	id: uuid.UUID = None
	name: str = None
	address: str 
	city: str
	departament: str
	identity_card: int = None


class NotFoundSchema(Schema):
	msg: str