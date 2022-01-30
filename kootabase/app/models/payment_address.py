from django.db import models 

class PaymentAddress(models.Model): 
    """
        Payment address normaly refers to the deposits address
        (where deposits are madel :-) )
    """
    
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE) 
    wallet_id = models.ForeignKey('Wallet', on_delete=models.SET_NULL) 
    address = models.CharField(max_length=95) 
    secrect_encrypted = models.CharField(max_length=255) 
    details_encrypted = models.CharField(max_length=1024) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)