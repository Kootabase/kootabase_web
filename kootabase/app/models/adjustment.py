from django.db import models 

class Adjustment(models.Model):

    # Adjustment statuses 
    PENDING = "PENDING" 
    ACCEPTED = "ACCEPTED" 
    REJECTED = "REJECTED"

    # Adjustment types
    ASSET_REGISTRATION = "ASSET_REGISTRATION" 
    INVESTMENT = "INVESTMENT" 
    MINTING_TOKEN = "MINTING_TOKEN" 
    BALANCE_ANOMALY = "BALANCE_ANOMALY" 
    MISC = "MISC" 
    REFUND = "REFUND" 
    COMPENSATION = "COMPENSATION" 
    INCENTIVE = "INCENTIVE"  
    BANK_FEES = "BANK_FEES" 
    BANK_INTEREST = "BANK_INTEREST" 
    MINOR = "MINOR"

    ADJUSTMENT_CATEGORIES = [
        (ASSET_REGISTRATION, "asset_registration"), 
        (INVESTMENT, "anvestment"), 
        (MINTING_TOKEN, "minting_token"), 
        (BALANCE_ANOMALY, "balance_anomaly"), 
        (MISC, "misc"), 
        (REFUND, "refund"), 
        (COMPENSATION, "compensation"), 
        (INCENTIVE, "incentive"), 
        (BANK_FEES, "bank_fees"), 
        (BANK_INTEREST, "bank_interest"), 
        (MINOR, "minor")
    ]

    ADJUSTMENT_STATUSES = [
        (PENDING, "pending"), 
        (ACCEPTED, "accepted"), 
        (REJECTED, "rejected")
    ]

    reason = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=65535, null=False) 
    creator_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    validator_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    amount = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    asset_account_code = models.IntegerField(null=False) 
    receivning_account_number = models.CharField(max_length=64, null=False) 
    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=False) 
    category = models.CharField(max_length=90, choices=ADJUSTMENT_CATEGORIES, null=False)
    state = models.CharField(max_length=30, choices=ADJUSTMENT_STATUSES, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)