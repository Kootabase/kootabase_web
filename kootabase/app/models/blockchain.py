from django.db import models 

class BlockChain(models.Model): 
    """
    """
    ACTIVE = "ACTIVE" 
    INACTIVE = "INACTIVE" 

    BLOCKCHAIN_STATUSES = [
        (ACTIVE, 'active'), 
        (INACTIVE, 'inactive')
    ]

    key = models.CharField(max_length=255, null=False) 
    name = models.CharField(max_length=255) 
    client = models.CharField(max_length=255, null=False) 
    server = models.CharField(max_length=255) 
    height = models.BigIntegerField(null=False) 
    explorer_address = models.CharField(max_length=255) 
    explorer_transaction = models.CharField(max_length=255) 
    min_confirmations = models.IntegerField(default=6, null=False) 
    status = models.CharField(max_length=255, null=False, choices=BLOCKCHAIN_STATUSES, default=ACTIVE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)