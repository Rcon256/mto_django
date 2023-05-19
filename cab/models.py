from django.db import models
from user_api.models import AppUser

# Create your models here.
class Cab(models.Model):
    name = models.CharField(max_length=5)
    user_id = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)

def __str__(self):
    return self.name