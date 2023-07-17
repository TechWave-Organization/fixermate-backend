from django.db.models import manager
from django.apps import apps
from django.shortcuts import get_object_or_404
from src.person.models import Person 
from src.schemas.client import InClient, OutClient
from src.schemas.person import InPerson
class ClientManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()

    def __create_client(self, data:dict):
        response = self.model(**data)
        response.save()
        return response

    def create_client(self, data: InClient):
        try:
            status, person = Person.objects.create_person(InPerson(
                email = data.email,
                name = data.name,
                address = data.address,
                city = data.city,
                departament = data.departament,
                identity_card = data.identity_card
            ))
            if status != 201:
                raise Exception("Could not create the user person")
            client = self.__create_client({"person_id": person})
            UserInfo = self.__create_schema(client)
            return 201, UserInfo
        except Exception as ex:
            return 500, {"message": str(ex)}


    def update_client(self, client_id, data:InClient):
        client = get_object_or_404(self.model, id=client_id)
        for attr, value in data.dict().items():
            setattr(client.person_id, attr, value)
        client.person_id.save()
        UserInfo = self.__create_schema(client)
        return 200, UserInfo
	
    def get_client(self, client_id):
        client = get_object_or_404(self.model, id=client_id)
        UserInfo = self.__create_schema(client)
        return 200, UserInfo


    def delete_client(self, client_id):
        client = get_object_or_404(self.model, id=client_id)
        client.person_id.delete()
        client.delete()
        return 204, "Correctly delete"


    def __create_schema(self, client):
        return OutClient(
            id = client.id,
            email = client.person_id.email,
            name = client.person_id.name,
            address = client.person_id.address,
            city = client.person_id.city,
            departament = client.person_id.departament,
            identity_card = client.person_id.identity_card
        )