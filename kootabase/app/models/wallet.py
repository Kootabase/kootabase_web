from unicodedata import decimal
from django.db import models 

class Wallet(models.Model): 
    ACTIVE = 'ACTIVE' 
    DISABLED = 'DISABLED'
    
    WALLET_STATUS = [
        (ACTIVE, 'Active'), 
        (DISABLED, 'Disabled')
    ]
    owner = models.ForeignKey('Member', on_delete=models.CASCADE) 
    balance = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False)
    blockchain = models.ForeignKey('Blockchain', on_delete=models.CASCADE) 
    currencies = models.ForeignKey('Currency', on_delete=models.CASCADE) 
    name = models.CharField(max_length=255, null=False) 
    address = models.CharField(max_length=255, null=False) 
    status = models.CharField(max_length=255, choices=WALLET_STATUS)
    max_balance = models.DecimalField(default=0.0, null=False)
    fee = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False)
    deposits = models.ForeignKey('Deposit', on_delete=models.SET_NULL) 
    withdraws = models.ForeignKey('Withdraw', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)