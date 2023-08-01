import uuid
from django.db import models
from src.invoice.manager import InvoiceManager, InvoiceItemManager
from src.client.models import Client 
from src.product.models import Product
from src.repair.models import Repair
from django.core.validators import MinValueValidator, MaxValueValidator
from src.base.models import BaseModel


class Invoice(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    feature_date = models.DateField
    objects = InvoiceManager()
    
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

class InvoiceItem(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.PositiveIntegerField
    cost = models.PositiveIntegerField
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    objects = InvoiceItemManager()

    class Meta:
        verbose_name = "Invoice Item"
        verbose_name_plural = "Invoice Items"

