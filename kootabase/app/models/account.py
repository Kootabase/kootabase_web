from unicodedata import decimal
from xml.etree.ElementInclude import default_loader
from django.db import models 

class Account(models.Model): 
    member_id = models.ForeignKey('Member', null=False, on_delete=models.CASCADE) 
    currency_id = models.ForeignKey('Currency', null=False, on_delete=models.DO_NOTHING) 
    balance = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False)
    locked = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)