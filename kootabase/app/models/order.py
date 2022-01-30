from xml.dom.expatbuilder import Rejecter
from django.db import models 
from enum import Enum



class Order(models.Model): 
    """
    """

    # Order states 
    PENDING = "PENDING" 
    WAIT = "WAIT" 
    DONE = "DONE" 
    CANCEL = "CANCEL" 
    REJECT = "REJECT"

    # Order choices
    STATE_CHOICES = [
        (PENDING, "Pending"), 
        (DONE, "Done"), 
        (CANCEL, "Cancel"), 
        (REJECT, "Reject"), 
        (WAIT, "Wait")
    ]

    # Order types Regular
    MARKET = "MARKET" 
    LIMIT = "LIMIT" 
    STOP_LOSS = "STOP_LOSS" 
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT" 
    TRAILING_STOP = "TRAILING_STOP" 
    TRAILING_STOP_LIMIT = "TRAILING_STOP_LIMIT" 
    OCO = "OCO" # Over the Counter Order 

    # Margin Order Types 
    MARGIN_MARKET = "MARGIN_MARKET" 
    MARGIN_LIMIT = "MARGIN_LIMIT" 
    MARGIN_STOP_LOSS ="MARGIN_STOP_LOSS" 
    MARGIN_STOP_LOSS_LIMIT = "MARGIN_STOP_LOSS_LIMIT" 
    MARGIN_TRAILING_STOP = "MARGIN_TRAILING_STOP" 
    MARGIN_TRAILING_STOP_LIMIT = "MARGIN_TRAILING_STOP_LIMIT" 
    MARGIN_OCO = "MARGIN_OCO"

    ORDER_TYPE_CHOICES = [
        (MARKET, 'market'), 
        (LIMIT, 'limit'), 
        (STOP_LOSS, "stop_loss"), 
        (STOP_LOSS_LIMIT, "stop_loss_limit"), 
        (TRAILING_STOP, "trailing_stop"), 
        (TRAILING_STOP_LIMIT, "trailing_stop_limit"), 
        (OCO, "oco"),

        # Margin order types 
        (MARGIN_MARKET, "margin_market"), 
        (MARGIN_LIMIT, "margin_limit"), 
        (MARGIN_STOP_LOSS, "margin_stop_loss"), 
        (MARGIN_STOP_LOSS_LIMIT, "margin_stop_loss_limit"), 
        (MARGIN_OCO, "margin_oco")
    ]

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
    state = models.CharField(max_length=255, choices=STATE_CHOICES, default=PENDING)

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