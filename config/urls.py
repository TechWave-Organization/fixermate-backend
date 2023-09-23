from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from src.user.API.routes import router as users_router
from src.client.API.routes import router as clients_router
from src.device.API.brand_routes import router as brands_router
from src.device.API.device_model_routes import router as device_model_router
from src.device.API.device_routes import router as device_router

api = NinjaAPI(
    title="Fixermate",
    description="Backend of Fixermate",
    auth=None,
)

api.add_router("users", users_router)
api.add_router("clients", clients_router)
api.add_router("brands", brands_router)
api.add_router("device_models", device_model_router)
api.add_router("devices", device_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
