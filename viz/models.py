from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Friend(models.Model):
    name        =   models.CharField(max_length=100, default='')
    fbid        =   models.BigIntegerField(default=0)
    active      =   models.BooleanField(default=True)
    
    def __unicode__(self):
        return "%s" % self.name
        
    def __hash__(self):
        return self.fbid
    
class DataPoint(models.Model):
    friends     =   models.ManyToManyField(Friend)
    friend_list =   models.TextField(default='')
    created_at  =   models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    data_points =   models.ManyToManyField(DataPoint)
    user        =   models.ForeignKey(User, unique=True)
    id          =   models.BigIntegerField(default=0, primary_key=True)
    access_token=   models.CharField(max_length=200, default='')
    
    def __unicode__(self):
        return "%s" % self.user