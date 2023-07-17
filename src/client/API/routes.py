import uuid
from ninja import Router
from ninja.pagination import paginate
from utils.pagination import CustomPagination
from src.schemas import client
from src.client.models import Client
from typing import Any, List


router = Router(tags=["Clients"])

@router.post(
    "",
    response={
        201: client.OutClient,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
def create_client(request, data: client.InClient):
    return Client.objects.create_client(data)


@router.get(
    "{client_id}",
    response={
        200: client.OutClient,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
def get_client(request, client_id: uuid.UUID):
    return Client.objects.get_client(client_id)

@router.put(
    "{client_id}",
    response={
        200: client.OutClient,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    }
)
def update_client(request, client_id: uuid.UUID, data: client.InClient):
    return Client.objects.update_client(client_id, data)

@router.get(
    "",
    response={
        200: List[client.OutClient],
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    }
)
def list_person(request):
    return Client.objects.all()

@router.delete(
    "{client_id}",
    response={
        204: Any,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    }
)
def delete_client(request, client_id: uuid.UUID):
    return Client.objects.delete_client(client_id)