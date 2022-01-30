from django.db import models 


class Beneficiary(models.Model): 
    
    PENDING = "PENDING" 
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED" 
    AML_PROCESSING = "AML_PROCESSING" 
    AML_SUSPICIOUS = "AML_SUSPICIOUS" 

    STATES_MAPPING = [
        (PENDING, "pending"), 
        (ACTIVE, "active"), 
        (ARCHIVED, "archived"), 
        (AML_PROCESSING, "aml_Processing"), 
        (AML_SUSPICIOUS, "aml_Suspicious")
    ]

    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=False) 
    name = models.CharField(max_length=64, null=False) 
    description = models.CharField(max_length=255, default="") 
    data_encrypted = models.CharField(max_length=1024) 
    pin = models.IntegerField(null=False) 
    sent_at = models.DateTimeField(auto_now=True) 
    state = models.CharField(max_length=255, default=PENDING, choices=STATES_MAPPING) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)