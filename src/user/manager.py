from django.db import transaction
import bcrypt
from django.apps import apps
from django.db.models import manager
from utils.model_loads import get_person_model
from src.schemas.person import InPerson
from src.base.manager import BaseManager
from src.schemas.user import InUser, OutUser


class UserManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def __create_user(self, data: dict):
        response = self.model(**data)
        response.save()
        return response

    def create_user(self, data: InUser):
        try:
            with transaction.atomic():
                status, person = get_person_model().objects.create_person(
                    InPerson(
                        name=data.name,
                        email=data.email,
                        address=data.address,
                        city=data.city,
                        departament=data.departament,
                        identity_card=data.identity_card,
                    )
                )

                if status != 201:
                    raise Exception("Could not create the user person")

                return 201, self.__create_schema(
                    self.__create_user(
                        {
                            "username": data.username,
                            "password": bcrypt.hashpw(
                                data.password.encode(), bcrypt.gensalt()
                            ).decode(),
                            "person": person,
                        }
                    )
                )

        except Exception as ex:
            return 500, {"message": str(ex)}

    def __create_schema(self, user):
        return OutUser(
            id=user.id,
            username=user.username,
            email=user.person.email,
            name=user.person.name,
            address=user.person.address,
            city=user.person.city,
            departament=user.person.departament,
            identity_card=user.person.identity_card,
        )
