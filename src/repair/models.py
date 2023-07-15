from django.db import models
import uuid
from src.repair.manager import RepairManager, RepairStatusManager, ServiceManager
# Create your models here.

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    # device_model_id = models.ForeignKey("device_model", verbose_name="", on_delete=models.CASCADE)
    objects = ServiceManager()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Repair(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # client_id = models.ForeignKey("client", verbose_name=(""), on_delete=models.CASCADE) #Pending
    # device_id = models.ForeignKey("device", verbose_name=(""), on_delete=models.CASCADE) #Pending
    service_id = models.ForeignKey(Service, verbose_name=(""), on_delete=models.CASCADE)
    objects = RepairManager()

    class Meta:
        verbose_name = "Repair"
        verbose_name_plural = "Repairs"


class RepairStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100)
    repair_id = models.ForeignKey(Repair, verbose_name=(""), on_delete=models.CASCADE)
    description = models.TextField(max_length=450)
    objects = RepairStatusManager()

    class Meta:
        verbose_name = "Repair Status"
        verbose_name_plural = "Repairs Status"
