from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class UserContacts(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=500)



    def __string__(self):
        return self.name
