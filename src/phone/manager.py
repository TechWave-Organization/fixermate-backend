from django.apps import apps
from django.db.models import manager

class PhoneManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()