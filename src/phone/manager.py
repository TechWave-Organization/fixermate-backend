from django.apps import apps
from django.db.models import manager
from src.base.manager import BaseManager


class PhoneManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()
