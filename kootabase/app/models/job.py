from pyexpat import model
from django.db import models 

class Job(models.Model): 

    name = models.CharField(max_length=255, null=False) 
    pointer = models.IntegerField() 
    counter = models.IntegerField() 
    data = models.JSONField()
    error_code = models.IntegerField() 
    error_message = models.CharField(max_length=255) 
    started_at = models.DateTimeField(auto_now_add=True) 
    finished_at = models.DateTimeField(auto_now=True)