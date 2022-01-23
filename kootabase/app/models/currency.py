from random import choice
from django.db import models 


class Currency(models.Model): 
    CURRENCY_TYPES = (
        ('Fiat', 'fiat'), 
        ('Crypto', 'crypto')
    )
    type = models.CharField(choices=CURRENCY_TYPES)
    name = models.CharField(max_length=255, null=False) 
    description = models.CharField(max_length=65535, null=False) 
    blockchain_key = models.CharField(max_length=32) 
    parent_id = None