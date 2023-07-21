from django.db import models
import uuid
from src.user.models import User
from src.permission.manager import RoleManager, RolePermissionManager, UserPermissionManger
# Create your models here.

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50, unique=True)
    objects = RoleManager()

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

class RolePermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    permission_name = models.TextField()
    objects = RolePermissionManager()

    class Meta:
        verbose_name = "Role Permission"
        verbose_name_plural = "Role Permissions"


class UserPermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    permission_name = models.TextField()
    objects = UserPermissionManger()

    class Meta:
        verbose_name = "User Permission"
        verbose_name_plural = "User Permissions"
