from django.db.models import manager

class RolManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()

class RolPermissionManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()

class UserPermissionManger(manager.Manager):
    def __init__(self) -> None:
        super().__init__()