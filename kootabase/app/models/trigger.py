from django.db import models 
from .order import Order

class Trigger(models.Model): 
    
    ORDER_TYPES = Order.ORDER_TYPE_CHOICES
    
    # Trigger status 
    PENDING = "PENDING" 
    DONE = "DONE" 
    ACTIVE = "ACTIVE" 
    CANCELLED = "CANCELLED" 

    TRIGGER_STATES = [
        (PENDING, "pending"), 
        (DONE, "done"), 
        (ACTIVE, "active"), 
        (CANCELLED, "cancelled")
    ]

    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, null=False) 
    order_type = models.CharField(max_length=255, choices=ORDER_TYPES, null=False)
    value = models.BinaryField(max_length=128, null=False) 
    state = models.CharField(max_length=30, choices=TRIGGER_STATES, null=False, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)