from django.db import models 

class Engine(models.Model): 

    ONLINE = "ONLINE" 
    OFFLINE = "OFFLINE" 
    STATES_MAPPING = [
        (ONLINE, "online"), 
        (OFFLINE, "offline")
    ]

    name = models.CharField(max_length=255, null=False) 
    driver = models.CharField(max_length=255, null=False) 
    uid = models.CharField(max_length=255) 
    url = models.CharField(max_length=255) 
    key_encrypted = models.CharField(max_length=255) 
    secret_encrypted = models.CharField(max_length=255)  
    data_encrypted = models.CharField(max_length=1024) 
    state = models.CharField(max_length=100, default=ONLINE, choices=STATES_MAPPING)