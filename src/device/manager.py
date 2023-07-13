from django.apps import apps
from django.db.models import manager

class DeviceManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()


class BrandManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()

class Device_modelManager(manager.Manager):
    def __init__(self) -> None:
        super().__init__()