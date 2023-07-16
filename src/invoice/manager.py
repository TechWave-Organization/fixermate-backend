from django.apps import apps
from django.db.models import manager

class InvoiceManager(manager.Manager):
    def __init__(self) -> None:
        super(). __init__()

class InvoiceItemManager(manager.Manager):
    def __init__(self) -> None:
        super(). __init__()
