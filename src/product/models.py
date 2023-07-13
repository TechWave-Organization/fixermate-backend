from django.db import models
from src.product.manager import ProductManager
import uuid
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    price = models.PositiveIntegerField
    name = models.CharField
    description = models.TextField
    # device_models_id = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    cost = models.PositiveIntegerField
    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"