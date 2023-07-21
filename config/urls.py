from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from src.user.API.routes import router as users_router

api = NinjaAPI(
    title="Fixermate",
    description="Backend of Fixermate",
    auth=None,
)

api.add_router("users", users_router)

urlpatterns = [
    path('admin/', admin.site.urls), path('api/', api.urls),
]
