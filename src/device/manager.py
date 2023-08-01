from django.apps import apps
from django.db.models import manager
from src.base.manager import BaseManager


class DeviceManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()


class BrandManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()


class DeviceModelManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()
