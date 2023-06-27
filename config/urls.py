from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from src.person.API.routes import router as persons_router

api = NinjaAPI(
    title="Fixermate",
    description="Backend of Fixermate",
    auth=None,
)
api.add_router("persons", persons_router)

urlpatterns = [
    path('admin/', admin.site.urls), path('api/', api.urls)
]
