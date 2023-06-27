import uuid
from ninja import Schema


class InPerson(Schema):
	email: str
	name: str
	address: str
	city: str
	departament: str
    
class OutPerson(Schema):
	id: uuid.UUID = None
	name: str = None
    

class NotFoundSchema(Schema):
	msg: str