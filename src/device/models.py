import uuid
from django.db import models
from src.device.manager import BrandManager, DeviceModelManager, DeviceManager
from src.client.models import Client
from src.base.models import BaseModel


class Brand(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    objects = BrandManager()

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class DeviceModel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=130)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    objects = DeviceModelManager()

    class Meta:
        verbose_name = "Device Model"
        verbose_name_plural = "Device Models"


class Device(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,  editable=False)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, null=True)
    imei = models.CharField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    objects = DeviceManager()

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
