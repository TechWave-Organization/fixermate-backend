from django.db import models
import uuid
from src.client.models import Client
from src.repair.manager import RepairManager, RepairStatusManager, ServiceManager
from src.device.models import Device, DeviceModel
from src.base.models import BaseModel

# Create your models here.

class Service(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    device_model = models.ForeignKey(DeviceModel, verbose_name="", on_delete=models.CASCADE)
    objects = ServiceManager()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Repair(BaseModel):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, verbose_name=(""), on_delete=models.CASCADE) #Pending
    device = models.ForeignKey(Device, verbose_name=(""), on_delete=models.CASCADE) #Pending
    service = models.ForeignKey(Service, verbose_name=(""), on_delete=models.CASCADE)
    objects = RepairManager()

    class Meta:
        verbose_name = "Repair"
        verbose_name_plural = "Repairs"


class RepairStatus(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100)
    repair = models.ForeignKey(Repair, verbose_name=(""), on_delete=models.CASCADE)
    description = models.TextField(max_length=450)
    objects = RepairStatusManager()

    class Meta:
        verbose_name = "Repair Status"
        verbose_name_plural = "Repairs Status"
