import uuid
from ninja import Router
from utils.decorators.permissions import permissions_required
from src.schemas import device
from utils.model_loads import get_device_model_model
from typing import Any, List

router = Router(tags=["Device_models"])


@router.get(
    "",
    response={
        200: List[device.OutDeviceModel],
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device_model", permissions=["view"])
def list_device_model(request):
    return get_device_model_model().objects.all_device_model()


@router.get(
    "{device_model_id}",
    response={
        200: device.OutDeviceModel,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device_model", permissions=["view"])
def get_device_model(request, device_model_id: uuid.UUID):
    return get_device_model_model().objects.create_schema(
        get_device_model().objects.get_device_model(device_model_id)
    )


@router.post(
    "",
    response={
        201: device.OutDeviceModel,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device_model", permissions=["create"])
def create_device_model(request, data: device.InDeviceModel):
    return 201, get_device_model_model().objects.create_device_model(data)


@router.put(
    "{device_model_id}",
    response={
        200: device.OutDeviceModel,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="device_model", permissions=["update"])
def update_device_model(
    request, device_model_id: uuid.UUID, data: device.InDeviceModel
):
    return get_device_model_model().objects.update_device_model(device_model_id, data)


@router.delete(
    "{device_model_id}",
    response={
        200: Any,
        204: Any,
        401: Any,
        403: Any,
        404: Any,
        500: Any,
    },
)
@permissions_required(role="device_model", permissions=["delete"])
def delete_device_model(request, device_model_id: uuid.UUID):
    return get_device_model_model().objects.deleted(device_model_id)
