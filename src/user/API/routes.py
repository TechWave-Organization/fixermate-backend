
from ninja import Router
from typing import Any
from src.schemas.user import InUser, OutUser
from src.user.models import User
from utils.decorators.permissions import permissions_required

router = Router(tags=["Users"])


@router.post(
    "/create",
    response={
        201: OutUser,
        400: Any,
        401: Any,
        403: Any,
        404: Any,
        500: dict,
    },
    url_name="user-create",
    auth=None
)
@permissions_required(role="user", permissions=["create"])
def create_user(request, user_schema: InUser):
    return User.objects.create_user(user_schema)
