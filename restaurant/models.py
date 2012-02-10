from django.db import models
from django.contrib.auth.models import User, UserManager, Group
from datetime import datetime

# Create your models here.

class Restaurant (models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=500, blank=False, null=False) 
    #TODO: details of the restaurant
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class Item(models.Model): 
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=100, blank=True, null=True)
    #TODO:add details for allgeries
    addedby = models.ForeignKey(User, related_name="Added by")
    addedwhen = models.DateField(default=datetime.now())#add default date when added
    restaurant = models.ForeignKey(Restaurant, related_name="restaurant name")
    def __unicode__(self):
        return " %s from %s " % (self.name, self.restaurant)
#
class ItemReview(models.Model):
    itemid = models.ForeignKey(Item, related_name="item name")
    rating = models.IntegerField()
    review = models.TextField(blank=True, null=True)
    daterated = models.DateField(default=datetime.now())#add default date when added
    reviewby = models.ForeignKey(User, related_name="Reviewed by")

