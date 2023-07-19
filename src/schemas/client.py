import uuid
from ninja import Schema

class InClient(Schema):
	email: str = None
	name: str 
	address: str = None
	city: str = None
	departament: str = None
	identity_card: int = None

class OutClient(Schema):
	id: uuid.UUID = None
	email: str = None
	name: str = None
	address: str = None
	city: str = None
	departament: str = None
	identity_card: int = None

class NotFoundSchema(Schema):
	msg: str