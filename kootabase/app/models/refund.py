from django.db import models 

class Refund(models.Model): 

    PENDING = "PENDING" 
    PROCESSED = "PROCESSED" 
    FAILED = "FAILED" 

    REFUND_STATUS = [
        (PENDING, "pending"), 
        (PROCESSED, "processed"), 
        (FAILED, "failed")
    ]

    deposit_id = models.ForeignKey('Deposit', on_delete=models.CASCADE, null=False) 
    state = models.CharField(max_length=30, choices=REFUND_STATUS, null=False) 
    address = models.CharField(max_length=255, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)