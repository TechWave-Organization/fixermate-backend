from django.db import models
import uuid
from src.user.models import User
from src.permissions.manager import RolManager, RolPermissionManager, UserPermissionManger
# Create your models here.

class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    objects = RolManager()

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

class RolPermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    permission_name = models.TextField()
    objects = RolPermissionManager()

    class Meta:
        verbose_name = "Rol Permission"
        verbose_name_plural = "Rol Permissions"


class UserPermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    permissions_name = models.TextField()
    objects = UserPermissionManger()

    class Meta:
        verbose_name = "User Permission"
        verbose_name_plural = "User Permissions"
