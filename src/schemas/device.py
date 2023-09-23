import uuid
from ninja import Schema
from pydantic import validator
from src.schemas.client import OutClient
from django.shortcuts import get_object_or_404
from utils.model_loads import (
    get_brand_model,
    get_device_model_model,
    get_client_model,
    get_person_model)

class InBrand(Schema):
    name: str

    @validator("name")
    def name_must_be_unique(cls, name):

        if get_brand_model().objects.filter(name=name).exists():
            raise ValueError(f"Brand with name {name} already exists!")
        return name


class OutBrand(Schema):
    id: uuid.UUID = None
    name: str = None


class InDeviceModel(Schema):
    name: str = None
    type: str = None
    brand: uuid.UUID = None

    @validator("name")
    def name_must_be_unique(cls, name):
        if get_device_model_model().objects.filter(name=name).exists():
            raise ValueError(f"Device model with name {name} already exists!")
        return name

    @validator("brand")
    def brand_must_be_exist(cls, brand):

        if not get_brand_model().objects.filter(id=brand).exists():
            raise ValueError(f"Brand with name {brand} must be exists!")
        return brand


class OutDeviceModel(Schema):
    id: uuid.UUID = None
    name: str = None
    type: str = None
    brand: OutBrand = None


class InDevice(Schema):
    device_model: uuid.UUID = None
    imei: str = None
    client: uuid.UUID = None

    @validator("device_model")
    def device_model_must_be_exist(cls, device_model):
        if not get_device_model_model().objects.filter(id=device_model).exists():
            raise ValueError(f"Device with name {device_model} must be exists!")
        return device_model

    @validator("client")
    def client_must_be_exist(cls, client):
        if not get_object_or_404(get_client_model(), id=client):
            raise ValueError(f"The client {client} must be exists!")
        return client


class OutDevice(Schema):
    id: uuid.UUID = None
    device_model: OutDeviceModel = None
    imei: str = None
    client: OutClient = None
