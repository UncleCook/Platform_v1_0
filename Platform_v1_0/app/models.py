"""
Definition of models.
"""

from django.db import models

# Company financial data
class Financials(models.Model):
    company = models.CharField(max_length=25, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    turnover = models.IntegerField(null=True, blank=True)
    total_assets = models.IntegerField(null=True, blank=True)
    total_liabilities = models.IntegerField(null=True, blank=True)
    operating_profit = models.IntegerField(null=True, blank=True)
    net_income = models.IntegerField(null=True, blank=True)
    free_cash_flow = models.IntegerField(null=True, blank=True)
    shareholder_funds = models.IntegerField(null=True, blank=True)
    interest_expense = models.IntegerField(null=True, blank=True)
    long_term_debt = models.IntegerField(null=True, blank=True)
    equity = models.IntegerField(null=True, blank=True)
    operating_margin = models.FloatField(null=True, blank=True)
    net_profit_margin = models.FloatField(null=True, blank=True)
    free_cash_flow_margin = models.FloatField(null=True, blank=True)
    interest_cover = models.FloatField(null=True, blank=True)
    return_on_assets = models.FloatField(null=True, blank=True)
    solvency_ratio = models.FloatField(null=True, blank=True)
    gearing = models.FloatField(null=True, blank=True)
    solvency_ratio = models.FloatField(null=True, blank=True)


# Bidding data model
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
    
"""
class Menu(models.Model):
    name_menu = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name_item = models.CharField(max_length=30)
    price = models.FloatField(blank=True,null=True)

"""