from sre_constants import MAX_UNTIL
from django.db import models 

class Transaction(models.Model): 
    
    PENDING = "PENDING" 
    SUCCEED = "SUCCEED"

    TRANSACTION_STATUS = [
        (PENDING, "Pending"), 
        (SUCCEED, "Succeed")
    ]

    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=False) 
    currency_name = models.CharField(max_length=255, null=False) 
    reference_type = models.CharField(max_length=255) 
    reference_id = models.BigIntegerField() 
    txid = models.CharField(max_length=255) 
    from_address = models.CharField(max_length=255) 
    to_address = models.CharField(max_length=255) 
    amount = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    block_number = models.IntegerField() 
    status = models.CharField(max_length=30, choices=TRANSACTION_STATUS, default=PENDING)
    options = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)