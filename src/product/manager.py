from django.db.models import manager
from django.apps import apps
from src.base.manager import BaseManager


class ProductManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()
