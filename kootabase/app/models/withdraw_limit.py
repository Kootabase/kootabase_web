from django.db import models 

class WithdrawLimit(models.Model): 

    # Default value for kyc_level, group name and currency_id in WithdrawLimit table: 
    ANY = "any"

    group = models.CharField(max_length=32, default=ANY, null=False) 
    kyc_level = models.CharField(max_length=32, default=ANY, null=False) 
    limit_24_hour = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    limit_1_month = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)