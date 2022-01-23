from unittest.util import _MAX_LENGTH
from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager  


class UserAccountManager(BaseUserManager): 
    def create_user(self, email, password=None, **extra_fields): 
        if not email: 
            raise ValueError('Users must have an email address') 

        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 

        user.set_password(password) 
        user.save()
        return user 

    def create_super_user(self, email, password=None, **extra_fields): 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True.') 
        return self.create_user(email, password, **extra_fields) 

    
    def create_staffuser(self, email, password=None, **extra_fields): 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Staff user must have is_staff=True') 
        return self.create_user(email, password, **extra_fields)


class BaseUser(AbstractBaseUser, PermissionsMixin): 
    ADMIN = 'Admin' 
    USER = 'User' 
    roles = (
        (ADMIN, 'Admin'), 
        (USER, 'User')
    )

    email = models.EmailField(max_length=255, unique=True, null=False, blank=False) 
    first_name = models.CharField(max_length=255, null=False) 
    last_name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, unique=True, null=False) 
    password = models.CharField(max_length=30, null=False, blank=False) 
    is_admin = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False) 
    last_login = models.DateTimeField(auto_now=True) 
    role = models.CharField(choices=roles, default="User", max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number'] 

    