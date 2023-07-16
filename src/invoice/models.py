import uuid
from django.db import models
from src.client.models import Client 
from src.product.models import Product
from src.repair.models import Repair
from django.core.validators import MinValueValidator, MaxValueValidator
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    feature_date = models.DateField

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.PositiveIntegerField
    cost = models.PositiveIntegerField
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    repair_id = models.ForeignKey(Repair, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Invoice Item"
        verbose_name_plural = "Invoice Items"

