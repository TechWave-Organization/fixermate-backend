from django.apps import apps
from django.db.models import manager
from django.shortcuts import get_object_or_404
from src.schemas.person import InPerson
from src.base.manager import BaseManager


class PersonManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def create_person(self, data: InPerson):
        try:
            return 201, self.create(data.dict())
        except Exception as ex:
            return 500, {"message": str(ex)}

    def update_person(self, person_id, data: InPerson):
        person = get_object_or_404(self.model, id=person_id)
        for attr, value in data.dict().items():
            setattr(person, attr, value)
        person.save()
        return 200, person

    def get_person(self, person_id):
        return get_object_or_404(self.model, id=person_id)

    def delete_person(self, person_id):
        person = get_object_or_404(self.model, id=person_id)
        person.delete()
        return 204, "Correctly delete"
