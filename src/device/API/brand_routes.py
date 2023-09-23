import uuid
from ninja import Router
from utils.decorators.permissions import permissions_required
from src.schemas import device
from utils.model_loads import get_brand_model
from typing import Any, List

router = Router(tags=["Brands"])


@router.get(
    "",
    response={
        200: List[device.OutBrand],
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="brand", permissions=["view"])
def list_brand(request):
    return get_brand_model().objects.all()


@router.get(
    "{brand_id}",
    response={
        200: device.OutBrand,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="brand", permissions=["view"])
def get_brand(request, brand_id: uuid.UUID):
    return get_brand_model().objects.create_schema(get_brand_model().objects.get(brand_id))


@router.post(
    "",
    response={
        201: device.OutBrand,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="brand", permissions=["create"])
def create_brand(request, data: device.InBrand):
    return 201, get_brand_model().objects.create_schema(get_brand_model().objects.create(dict(data)))


@router.put(
    "{brand_id}",
    response={
        200: device.OutBrand,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
)
@permissions_required(role="brand", permissions=["update"])
def update_brand(request, brand_id: uuid.UUID, data: device.InBrand):
    return get_brand_model().objects.update_brand(brand_id, data)


@router.delete(
    "{brand_id}",
    response={
        200: Any,
        204: Any,
        401: Any,
        403: Any,
        404: Any,
        500: Any,
    },
)
@permissions_required(role="brand", permissions=["delete"])
def delete_brand(request, brand_id: uuid.UUID):
    return get_brand_model().objects.deleted(brand_id)
