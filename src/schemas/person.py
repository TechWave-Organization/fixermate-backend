import uuid
from ninja import Schema


class InPerson(Schema):
	email: str = None
	name: str
	address: str = None
	city: str = None
	departament: str = None
	identity_card: str = None

class OutPerson(Schema):
	id: uuid.UUID = None
	name: str = None
	address: str 
	city: str
	departament: str
	identity_card: str = None


class NotFoundSchema(Schema):
	msg: str