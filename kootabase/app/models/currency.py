from random import choice
from django.db import models 


class Currency(models.Model): 
    CURRENCY_TYPES = (
        ('Fiat', 'fiat'), 
        ('Coin', 'coin')
    )
    
    name = models.CharField(max_length=255, null=False) 
    description = models.CharField(max_length=65535, null=False) 
    blockchain_key = models.CharField(max_length=32) 
    parent_id = models.CharField(max_length=255) 
    type = models.CharField(max_length=255, choices=CURRENCY_TYPES)
    deposit_fee = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    min_deposit_amount = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    min_withdraw_amount = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    withdraw_limit_24h = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    withdraw_limit_72h = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    position = models.IntegerField(null=False, default=0) 
    options = models.JSONField() 
    visible = models.BooleanField(default=True, null=False)  
    deposit_enabled = models.BooleanField(default=True, null=False) 
    withdrawal_enabled = models.BooleanField(default=True, null=False) 
    base_factor = models.BigIntegerField(default=1, null=False) 
    precision = models.IntegerField(default=8, null=False) 
    icon_url = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=32, decimal_places=16, default=1.0, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    