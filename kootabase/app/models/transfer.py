from django.db import models 

class Transfer(models.Model): 

    WIRE = "WIRE" 
    REFUND = "REFUND" 
    PURCHASES = "PURCHASES" 
    COMMISION = "COMMISSION" 

    TRANSFER_CATEGORIES = [
        (WIRE, "Wire"), 
        (REFUND, "Refund"), 
        (PURCHASES, "Purchases"), 
        (COMMISION, "Commission")
    ]
    
    key = models.CharField(max_length=30, null=False) 
    category = models.CharField(max_length=100, choices=TRANSFER_CATEGORIES, null=False)
    description = models.CharField(max_length=255, default="") 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)