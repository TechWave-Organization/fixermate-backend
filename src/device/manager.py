import uuid
from django.apps import apps
from django.db.models import manager
from src.base.manager import BaseManager
from src.schemas.device import (
    OutBrand,
    OutDeviceModel,
    OutDevice,
    InDeviceModel,
    InDevice,
)
from django.shortcuts import get_object_or_404
from django.db import transaction
from utils.model_loads import (
    get_client_model,
    get_person_model,
    get_device_model_model,
    get_brand_model)

class BrandManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def update_brand(self, brand_id, data):
        brand = get_object_or_404(self.model, id=brand_id)
        brand.name = data.name
        brand.save()
        return 200, self.create_schema(brand)

    def create_schema(self, brand):
        return OutBrand(id=brand.id, name=brand.name)


class DeviceModelManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def create_device_model(self, data: InDeviceModel):
        brandObj = get_object_or_404(get_brand_model(), id=data.brand)
        newObj = self.create({"name": data.name, "type": data.type, "brand": brandObj})
        return self.create_schema(newObj)

    def update_device_model(self, id: uuid.UUID, data: InDeviceModel):
        devModel = get_object_or_404(self.model, id=id)
        for attr, value in data.dict().items():
            if attr != "brand":
                setattr(devModel, attr, value)
        brand = get_object_or_404(get_brand_model(), id=data.brand)
        setattr(devModel, "brand", brand)
        devModel.save()
        return 200, self.create_schema(devModel)

    def get_device_model(self, id: uuid.UUID):
        return get_object_or_404(self.model, id=id)

    def all_device_model(self):
        all_devMod = self.all()
        list_devMod = []
        for obj in all_devMod:
            list_devMod.append(self.create_schema(obj))
        return 200, list_devMod

    def create_schema(self, devModel):
        return OutDeviceModel(
            id=devModel.id,
            name=devModel.name,
            type=devModel.type,
            brand= get_brand_model().objects.create_schema(devModel.brand)
        )


class DeviceManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def all_device(self):
        all_dev = self.all()
        list_dev = []
        for obj in all_dev:
            list_dev.append(self.create_schema(obj))
        return 200, list_dev

    def create_device(self, data: InDevice):
        client = get_object_or_404(get_client_model(), id=data.client)
        dev_model = get_object_or_404(get_device_model_model(), id=data.device_model)
        newObj = self.create(
            {"device_model": dev_model, "imei": data.imei, "client": client}
        )
        return self.create_schema(newObj)
    
    def update_device(self, id: uuid.UUID, data: InDevice):
        dev = get_object_or_404(self.model, id=id)
        for attr, value in data.dict().items():
            if attr != "device_model" and attr != "client":
                setattr(dev, attr, value)
        devModel = get_object_or_404(get_device_model_model(), id=data.device_model)
        client = get_object_or_404(get_client_model(), id=data.client)
        setattr(dev, "device_model", devModel)
        setattr(dev, "client", client)
        dev.save()
        return 200, self.create_schema(dev)

    def create_schema(self, dev):
        return OutDevice(
            id=dev.id,
            device_model=get_device_model_model().objects.create_schema(dev.device_model),
            imei=dev.imei,
            client=get_client_model().objects.create_schema(dev.client),
        )
