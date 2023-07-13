import uuid
from django.db import models
from src.device.manager import BrandManager, Device_modelManager, DeviceManager

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    objects = BrandManager()

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Device_model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=130)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    objects = Device_modelManager()

    class Meta:
        verbose_name = "Device_model"
        verbose_name_plural = "Device_models"


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,  editable=False)
    device_model_id = models.ForeignKey(Device_model, on_delete=models.CASCADE, null=True)
    imei = models.CharField(max_length=30)
    # client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True) # pending
    objects = DeviceManager()

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
