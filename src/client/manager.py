from django.db.models import manager
from django.apps import apps
from django.shortcuts import get_object_or_404
from src.base.manager import BaseManager
from src.person.models import Person
from src.schemas.client import InClient, OutClient
from src.schemas.person import InPerson
from django.db import transaction


class ClientManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def create_client(self, data: InClient):
        try:
            with transaction.atomic():
                status, person = Person.objects.create_person(
                    InPerson(
                        email=data.email,
                        name=data.name,
                        address=data.address,
                        city=data.city,
                        departament=data.departament,
                        identity_card=data.identity_card,
                    )
                )
                if status != 201:
                    raise Exception(f"Could not create the user person {person}")
                client = self.create({"person": person})
                user_info = self.create_schema(client)
                return 201, user_info
        except Exception as ex:
            return 500, {"message": str(ex)}

    def update_client(self, client_id, data: InClient):
        client = get_object_or_404(self.model, id=client_id)
        for attr, value in data.dict().items():
            setattr(client.person, attr, value)
        client.person.save()
        client.save()
        client_info = self.create_schema(client)
        return 200, client_info

    def get_list(self):
        client_list = []
        clients = self.all()
        for client in clients:
            client_list.append(self.create_schema(client))
        return 200, client_list

    def delete_client(self, client_id):
        client = get_object_or_404(self.model, id=client_id)
        client.person.delete()
        client.delete()
        return f"It was eliminated: {client.is_deleted}"

    def create_schema(self, client):
        return OutClient(
            id=client.id,
            email=client.person.email,
            name=client.person.name,
            address=client.person.address,
            city=client.person.city,
            departament=client.person.departament,
            identity_card=client.person.identity_card,
        )
