# Controls the user database

from django.db import models
import hashlib
import datetime
#from django.utils.encoding import smart_unicode


class SignUp(models.Model):
    first_name=models.CharField(max_length=120,null=False,blank=False)
    last_name=models.CharField(max_length=120,null=False,blank=False)
    password=models.CharField(max_length=120,null=False,blank=False)
    password_conf=models.CharField(max_length=120,null=False,blank=False)
    Organization=models.CharField(max_length=120,null=True,blank=False)
    email=models.EmailField(null=False,blank=False)
    position=models.CharField(max_length=120,null=False,blank=False)
    is_active=models.BooleanField(default=False) # not active until he opens activation link
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    
    def __str__(self):
        
        return str(self.last_name+','+self.first_name+' in '+self.Organization+' having email as '+self.email)
        

class MyLogin(models.Model):
    email=models.EmailField(null=False,blank=True)
    password=models.CharField(max_length=120,null=False,blank=True)
    
    def __str__(self):
        return str(self.email)
    
class MyForgotPassword(models.Model):
    email=models.EmailField(null=False,blank=True)
    
    
    def __str__(self):
        return str(self.email)
    
class MyPasswordReset(models.Model):
    email=models.EmailField(null=False,blank=True)
    password=models.CharField(max_length=120,null=False,blank=False)
    password_conf=models.CharField(max_length=120,null=False,blank=False)
    
    def __str__(self):
        return str(self.email)
