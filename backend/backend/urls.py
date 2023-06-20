from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI


api = NinjaAPI(
    title="Fixermate",
    description="Backend of Fixermate",
    auth=None,
)

urlpatterns = [
    path('admin/', admin.site.urls), path('api/', api.urls)
]
