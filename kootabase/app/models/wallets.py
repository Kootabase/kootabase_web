from django.db import models 

class Wallet(models.Model): 
    WALLET_STATUS = (
        ('Active', 'active'), 
        ('Disabled', 'disabled')
    )
    owner = models.ForeignKey('Member', on_delete=models.CASCADE) 
    balance = models.FloatField(null=False) 
    blockchain = models.ForeignKey('Blockchain', on_delete=models.CASCADE) 
    currencies = models.ForeignKey('Currency', on_delete=models.CASCADE) 
    name = models.CharField(max_length=255, null=False) 
    address = models.CharField(max_length=255, null=False) 
    status = models.CharField(max_length=255, choices=WALLET_STATUS)
    max_balance = models.FloatField(null=False)
    fee = models.FloatField(null=False) 
    deposits = models.ForeignKey('Deposit', on_delete=models.CASCADE) 
    withdraws = models.ForeignKey('Withdraw', on_delete=models.CASCADE)