from unicodedata import decimal
from django.db import models 

class Withdraw(models.Model): 

    FIAT = "FIAT" 
    CRYPTO = "CRYPTO" 

    DEPOSIT_TYPE_CHOICES = [
        (FIAT, "Fiat"), 
        (CRYPTO, "Crypto")
    ]

    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    beneficiary_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=False) 
    amount = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    fee = models.DecimalField(max_digits=32, decimal_places=16, null=False)
    txid = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    aasm_state = models.CharField(max_length=30)
    block_number = models.IntegerField() 
    sum = models.DecimalField(max_digits=32, decimal_places=16) 
    type = models.CharField(max_length=30, choices=DEPOSIT_TYPE_CHOICES, null=False) 
    transfer_type = models.CharField(max_length=30, choices=DEPOSIT_TYPE_CHOICES) 
    tid = models.CharField(max_length=64, null=False) 
    rid = models.CharField(max_length=256, null=False) 
    note = models.CharField(max_length=256) 
    metadata = models.JSONField() 
    error = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField()