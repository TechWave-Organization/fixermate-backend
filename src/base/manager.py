from django.db.models import manager
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404


class BaseManager(manager.Manager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db).exclude(is_deleted=True)

    def create(self, data: dict):
        response = self.model(**data)
        response.save()
        return response

    def get(self, id):
        return get_object_or_404(self.model, id=id)
