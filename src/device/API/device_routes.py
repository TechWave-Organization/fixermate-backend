import uuid
from ninja import Router
from utils.decorators.permissions import permissions_required
from src.schemas import device
from utils.model_loads import get_device_model
from typing import Any, List

router = Router(tags=["Devices"])


@router.get(
    "",
    response={
        200: List[device.OutDevice],
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device", permissions=["view"])
def list_device(request):
    return get_device_model().objects.all_device()


@router.get(
    "{device_id}",
    response={
        200: device.OutDevice,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device", permissions=["view"])
def get_device(request, device_id: uuid.UUID):
    return get_device_model().objects.create_schema(get_device_model().objects.get(device_id))


@router.post(
    "",
    response={
        201: device.OutDevice,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device", permissions=["create"])
def create_device(request, data: device.InDevice):
    return 201, get_device_model().objects.create_device(data)


@router.put(
    "{device_id}",
    response={
        200: device.OutDevice,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device", permissions=["update"])
def update_device(request, device_id: uuid.UUID, data: device.InDevice):
    return get_device_model().objects.update_device(device_id, data)


@router.delete(
    "{device_id}",
    response={
        200: Any,
        204: Any,
        401: Any,
        403: Any,
        404: Any,
        500: Any,
    },
)
@permissions_required(role="device", permissions=["delete"])
def delete_device(request, device_id: uuid.UUID):
    return get_device_model().objects.deleted(device_id)
