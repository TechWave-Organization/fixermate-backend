from django.db import models
import uuid
from src.repair.manager import RepairManager, RepairStatusManager, ServiceManager
# Create your models here.

class repair(models.Model):
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # client_id = models.ForeignKey("client", verbose_name=(""), on_delete=models.CASCADE) #Pending
    # device_id = models.ForeignKey("device", verbose_name=(""), on_delete=models.CASCADE) #Pending
    service_id = models.ForeignKey("service", verbose_name=(""), on_delete=models.CASCADE)
    objects = RepairManager()

    class Meta:
        verbose_name = "repair"
        verbose_name_plural = "repairs"

class repair_status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100)
    repair_id = models.ForeignKey("repair", verbose_name=(""), on_delete=models.CASCADE)
    description = models.CharField(max_length=450)
    objects = RepairStatusManager()

    class Meta:
        verbose_name = "repair_status"
        verbose_name_plural = "repairs_status"

class service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    # device_model_id = models.ForeignKey("device_model", verbose_name="", on_delete=models.CASCADE)
    objects = ServiceManager()

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"    