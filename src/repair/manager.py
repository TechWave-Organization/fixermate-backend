from django.apps import apps
from django.db.models import manager
from src.base.manager import BaseManager


class RepairManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()


class RepairStatusManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()


class ServiceManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()
