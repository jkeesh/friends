from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Friend(models.Model):
    name        =   models.CharField(max_length=100, default=0)
    id          =   models.PositiveIntegerField(default=0, primary_key=True)
    
class DataPoint(models.Model):
    friends     =   models.ManyToManyField(Friend)
    created_at  =   models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    data_points =   models.ManyToManyField(DataPoint)
    user        =   models.ForeignKey(User, unique=True)