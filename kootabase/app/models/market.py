from unicodedata import decimal
from django.db import models 

class Market(models.Model): 
    """
    People exchange commodities in markets. Each market focuses on certain
    commodity pair (A,B). By convention, we call people exchange A for B 
    'sellers' who submit 'ask' orders, and people who exchange B for A 'buyers'
    who submit bid 'orders'
    
    the ID of the market (here market_name) is always in the form {B}#{A}. for example, in 'btcusd'
    market, the commodity pair is {btc, usd}. sellers sell out _btc_ for _usd_, buyers buy in 
    _btc_ with usd. _btc_ is the base 'unit', while _usd_ is the quote_unit
    
    Given market BTC/USD. 
    Ask/Base currency/unit = BTC 
    Bid/Quote currency/unit = USD"""

    DB_DECIMAL_PRECISION = 16 
    FUNDS_PRECISION = 10 
    TOP_POSITION = 1

    ENABLED = "ENBABLED" # user can view and trade
    DISABLED = "DISABLED" # none can trade, user can't view
    HIDDEN = "HIDDEN" # user can't view but can trade
    LOCKED = "LOCKED" # user can view but can't trade
    SALE = "SALE" # user can't view but can trade with market orders.
    PRESALE = "PRESALE" # user can't view and trade. Admin can trade

    MARKET_STATES = [
        (ENABLED, "enabled"), 
        (DISABLED, "disabled"), 
        (HIDDEN, "hidden"), 
        (LOCKED, "locked"), 
        (SALE, "sale"), 
        (PRESALE, "presale")
    ]

    # base_currency and quote_currency is preferred names instead of legacy 
    # base_unit and quote_unit

    market_name = models.CharField(max_length=20, null=False, primary_key=True)
    base_currency = models.CharField(max_length=20, null=False) 
    quote_currency = models.CharField(max_length=10, null=False) 
    engine_id = models.BigIntegerField(null=False) 
    amount_precision = models.IntegerField(default=4, null=False) 
    price_precision = models.IntegerField(default=4, null=False) 
    min_price = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    max_price = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    min_amount = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    position = models.IntegerField(null=False) 
    data = models.JSONField() 
    state = models.CharField(max_length=32, default=ENABLED, choices=MARKET_STATES, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)