import uuid
from django.db.models import manager
from src.base.manager import BaseManager
from src.schemas.user import InUserPermission
from src.user.models import User


class RoleManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()


class RolePermissionManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()


class UserPermissionManger(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def __create_user_permission(self, data: dict):
        response = self.model(**data)
        response.save()
        return response

    def create_user_permission(self, user_id: uuid.UUID, data: InUserPermission):
        try:
            user = User.objects.get(id=user_id)
            permissions = []
            if not user:
                return 404, {"error": "User not found"}
            for permission in data.permission_name_list:
                permissions.append(
                    self.__create_user_permission(
                        {"user": user, "permission_name": permission}
                    )
                )
            return 201, permissions
        except Exception as ex:
            return 500, {"message": str(ex)}
