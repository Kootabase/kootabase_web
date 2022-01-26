from unicodedata import decimal
from django.db import models 

class TradingFee(models.Model): 
    """
    Trading fee table (trading_fees)
    """
    market_id = models.ForeignKey('Market', on_delete=models.CASCADE, default="any", null=False) 
    group = models.CharField(max_length=32, default="any", null=False) 
    maker = models.DecimalField(max_digits=7, decimal_places=6, default=0.0, null=False) 
    taker = models.DecimalField(max_digits=7, decimal_places=6, default=0.0, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)