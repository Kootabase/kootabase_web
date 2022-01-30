from django.db import models 


class Deposit(models.Model): 
    """
    """
    
    FIAT = 'FIAT' 
    CRYPTO = 'CRYPTO'
    DEPOSIT_TYPES = [
        (FIAT, 'fiat'), 
        (CRYPTO, 'crypto')
    ]

    TRANSFERT_TYPES = [
        (FIAT, 'fiat'), 
        (CRYPTO, 'crypto')
    ]

    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=False)
    amount = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    fee = models.DecimalField(max_digits=32, decimal_places=16, null=False)    
    address = models.CharField(max_length=95) 
    from_address = models.CharField(max_length=1000) 
    txid = models.CharField(max_length=128) 
    txout = models.IntegerField() 
    aasm_state = models.CharField(max_length=30)
    block_number = models.IntegerField() 
    type = models.CharField(max_length=30, null=False, choices=DEPOSIT_TYPES)
    transfer_type = models.CharField(max_length=30) 
    tid = models.CharField(max_length=64, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)