"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Bids(models.Model): 
   volume = models.IntegerField(null=True)
   bid_value = models.IntegerField()

"""
   def __str__(self): 
      return self.bid_value
"""


class Contact(models.Model): 
   name = models.CharField(max_length=50)
   city = models.CharField(max_length=50)
   state = models.CharField(max_length=2)
   create_date = models.DateTimeField()
   phone_number = models.CharField(max_length=20)
   email = models.CharField(max_length=20)

   def __str__(self):
      return self.name
    

class Menu(models.Model):
    name_menu = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name_item = models.CharField(max_length=30)
    price = models.FloatField(blank=True,null=True)

