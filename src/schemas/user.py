from typing import List
import uuid
from pydantic import validator
from ninja.schema import Schema

from src.authentication.permission_data import get_permissions



class InUser(Schema):
    username: str
    password: str
    email: str = None
    name: str
    address: str = None
    city: str = None
    departament: str = None
    identity_card: int = None
    
class OutUser(Schema):
    id: uuid.UUID
    username: str
    email: str = None
    name: str
    address: str = None
    city: str = None
    departament: str = None
    identity_card: int = None
 
class InUserPermission(Schema):
    permission_name_list: List[str]
    
    @validator("permission_name_list")
    def validate_permission_name_list(cls, permission_name_list):
        for permission in permission_name_list:
            if not permission in get_permissions():
                raise ValueError(f"{permission} not found")
        return permission_name_list

class UserAuth(Schema):
    id: uuid.UUID
    username: str
    permissions: List[str]

class CreateUser(Schema):
    password: str
    person_id: uuid.UUID
 