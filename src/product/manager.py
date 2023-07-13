from django.db.models import manager
from django.apps import apps

class ProductManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()