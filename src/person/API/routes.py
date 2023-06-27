import uuid
from ninja import Router
from ninja.pagination import paginate
from utils.pagination import CustomPagination
from src.schemas import person
from src.person.models import Person
from typing import Any, List


router = Router(tags=["Persons"])

@router.post(
    "",
    response={
        201: person.OutPerson,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
def create_person(request, data: person.InPerson):
    return Person.objects.create_person(data)

@router.get(
    "{person_id}",
    response={
        200: person.InPerson,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
def get_person(request, person_id: uuid.UUID):
    return Person.objects.get_person(person_id)

@router.put(
    "{person_id}",
    response={
        200: person.OutPerson,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    }
)
def update_person(request, person_id: uuid.UUID, data: person.InPerson):
    return Person.objects.update_person(person_id, data)

@router.get(
    "",
    response={
        200: List[person.OutPerson],
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    }
)
def list_person(request):
    return Person.objects.all()

@router.delete(
    "{person_id}",
    response={
        204: Any,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    }
)
def delete_person(request, person_id: uuid.UUID):
    return Person.objects.delete_person(person_id)