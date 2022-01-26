from argparse import ONE_OR_MORE
from django.db import models
from .user import BaseUser 


class Member(BaseUser): 
    
    accounts = models.ForeignKey('Account', on_delete=models.CASCADE)
    orders = models.ForeignKey('Order', on_delete=models.CASCADE) 
    payment_addresses = models.ForeignKey('PaymentAddress', on_delete=models.CASCADE) 
    withdraws = models.ForeignKey('Withdraw', on_delete=models.CASCADE) 
    deposits = models.ForeignKey('Deposit', on_delete=models.CASCADE) 
    beneficiaries = models.ForeignKey('self', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)