import uuid
from ninja import Router
from ninja.pagination import paginate
from utils.decorators.permissions import permissions_required
from utils.pagination import CustomPagination
from src.schemas import client
from src.client.models import Client
from typing import Any, List

router = Router(tags=["Clients"])


@router.get(
    "",
    response={
        200: List[client.OutClient],
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="client", permissions=["view"])
def list_client(request):
    return Client.objects.get_list()


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
@permissions_required(role="client", permissions=["view"])
def get_client(request, client_id: uuid.UUID):
    return Client.objects.create_schema(Client.objects.get(client_id))


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
@permissions_required(role="client", permissions=["create"])
def create_client(request, data: client.InClient):
    return Client.objects.create_client(data)


@router.put(
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
@permissions_required(role="client", permissions=["update"])
def update_client(request, client_id: uuid.UUID, data: client.InClient):
    return Client.objects.update_client(client_id, data)


@router.delete(
    "{client_id}",
    response={
        200: Any,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: Any,
    },
)
@permissions_required(role="client", permissions=["delete"])
def delete_client(request, client_id: uuid.UUID):
    return Client.objects.delete_client(client_id)
