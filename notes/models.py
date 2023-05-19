from django.db import models
from user_api.models import AppUser
from cab.models import Cab
import datetime

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    dt = models.DateTimeField(default=datetime.datetime.now())
    user_id = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    cab = models.ForeignKey(Cab, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=1024)
    state = models.IntegerField(default=0)
    comment = models.CharField(max_length=1024, blank=True)

def __str__(self):
    return self.name