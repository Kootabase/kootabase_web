from django.db import models 

class StatsMemberPnl(models.Model): 

    member_id = models.ForeignKey('Member', on_delete=models.CASCADE, null=False) 
    pnl_currency_id = models.CharField(max_length=10, null=False) 
    currency_id = models.ForeignKey('Currency', on_delete=models.CASCADE, null=False) 
    total_credit = models.DecimalField(max_digits=48, decimal_places=16, default=0.0, null=False) 
    total_credit_fees = models.DecimalField(max_digits=48, decimal_places=16, default=0.0) 
    total_debit_fees = models.DecimalField(max_digits=48, decimal_places=16, default=0.0)
    total_debit = models.DecimalField(max_digits=48, decimal_places=16, default=0.0) 
    total_credit_value = models.DecimalField(max_digits=48, decimal_places=16, default=0.0) 
    total_debit_value = models.DecimalField(max_digits=48, decimal_places=16, default=0.0) 
    total_balance_value = models.DecimalField(max_digits=48, decimal_places=16, default=0.0) 
    average_balance_price = models.DecimalField(max_digits=48, decimal_places=16, default=0.0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)