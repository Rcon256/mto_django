from django.db import models
from user_api.models import AppUser
import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=1024)
    dt = models.DateTimeField(default=datetime.datetime.now())
    user_id = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)

def __str__(self):
    return self.name