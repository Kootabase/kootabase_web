from django.db import models 

class Trade(models.Model): 
    
    price = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    amount = models.DecimalField(max_digits=32, decimal_places=16, null=False) 
    total = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    maker_order_id = models.ForeignKey('Order', null=False)
    taker_order_id = models.ForeignKey('Order', null=False) 
    market_id = models.CharField(max_length=20, null=False) 
    taker_id = models.ForeignKey('Member', null=False, on_delete=models.CASCADE) 
    maker_id = models.ForeignKey('Member', null=False, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
