from django.apps import apps
from django.db.models import manager

class RepairManager(manager.Manager):
    def __init__(self) -> None:
	    super().__init__()

class Repair_statusManager(manager.Manager):
    def __init__(self) -> None:
	    super().__init__()

class ServiceManager(manager.Manager):
	def __init__(self) -> None:
		super().__init__()
