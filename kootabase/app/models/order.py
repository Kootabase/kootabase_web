from django.db import models 
from enum import Enum


class ORDER_TYPE(Enum): 
    BID = "bid" 
    ASK = "ask"

class Order(models.Model): 
    """
    """
    class ORDER_STATE(Enum): 
        PENDING = "pending" 
        WAIT = "wait" 
        DONE = "done" 
        CANCEL = "cancel" 
        REJECT = "reject"


    STATE_CHOICES = (
        ('Pending', 'pending'), 
        ('Wait', 'wait'), 
        ('Cancel', 'cancel'), 
        ('Reject', 'reject')
    )

    ORDER_TYPE_CHOICES = (
        ('Market', 'market'), 
        ('Limit', 'limit')
    )

    uuid = models.BinaryField(max_length=16, null=False, unique=True)  
    remote_id = models.CharField(max_length=255) 
    bid = models.CharField(max_length=10, null=False) 
    ask = models.CharField(max_length=10, null=False)
    market_id = models.ForeignKey('Market', null=False) 
    price = models.DecimalField(max_digits=32, decimal_places=16) 
    volume = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    origin_volume = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    maker_fee = models.DecimalField(max_digits=17, decimal_places=16, default=0.0, null=False) 
    taker_fee = models.DecimalField(max_digits=17, decimal_places=16, default=0.0, null=False)
    state = models.CharField(max_length=255, choices=STATE_CHOICES, default=ORDER_STATE.PENDING)

    # the type of order to be executed it can either be a market or a limit order
    type = models.CharField(max_length=8, null=False, choices=ORDER_TYPE_CHOICES)

    # the member (user) who executed the order 
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    
    # the amount of locked funds in the member's account 
    locked = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    origin_locked = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    
    funds_received = models.DecimalField(max_digits=32, decimal_places=16, default=0.0) 
    trades_count = models.IntegerField(default=0, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)