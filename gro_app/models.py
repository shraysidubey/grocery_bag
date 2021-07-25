from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.IntegerField(max_length=12)
    address = models.TextField(max_length=300)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class GroceryItem(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    item_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    TYPE_SELECT = (('bought', 'bought'),('left', 'left'),('available','available'),)
    flag=models.CharField(max_length=11,choices=TYPE_SELECT)
    date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.item_name