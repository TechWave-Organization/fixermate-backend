import uuid
from src.authentication.permission_data import get_permissions
from src.permission.models import UserPermission
from src.schemas.user import InUser, InUserPermission
from src.user.models import User
from decouple import config
from django.db import transaction

@transaction.atomic
def create_user_root():
    root = User.objects.filter(username="root")
    if len(root) > 0:
        return None
    status, new_root = User.objects.create_user(InUser(
            username = "root",
            password = config("ROOT_PASSWORD"),
            name = "root",
            email = "root@techwaveinn.com",
            address = "",
            city = "",
            departament = "",
            identity_card = "11111111"
    ))
    
    if status != 201:
        return None
    permission_all = get_permissions()
    status, permissions = UserPermission.objects.create_user_permission(user_id=new_root.id, data = InUserPermission(permission_name_list=permission_all))
    if status != 201:
        raise Exception("Could not create the root user")
    print("Root Created")
    
if __name__ == "django.core.management.commands.shell":
    create_user_root()