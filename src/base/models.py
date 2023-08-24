from django.db import models

class BaseModel(models.Model): 
    
    is_deleted = models.BooleanField(default=False)


    def delete(self): 
        """Mark the record as deleted instead of deleting it."""

        self.is_deleted = True 
        self.save()

    class Meta: 
        abstract = True
    