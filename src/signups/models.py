from django.db import models
import hashlib
#from django.utils.encoding import smart_unicode
# Controls the user database

class SignUp(models.Model):
    first_name=models.CharField(max_length=120,null=False,blank=False)
    last_name=models.CharField(max_length=120,null=False,blank=False)
    password=models.CharField(max_length=120,null=False,blank=False)
    Organization=models.CharField(max_length=120,null=True,blank=False)
    email=models.EmailField(null=False,blank=False)
    position=models.CharField(max_length=120,null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    
    def __str__(self):
        #sequence=('self.first_name', 'self.last_name', 'self.email', 'self.Organization')
        return str(self.last_name+','+self.first_name+' in '+self.Organization+' having email as '+self.email)
        #return str(self.first_name|self.last_name|self.email|self.Organization)
    
#class Login(models.Model):
#    #first_name=models.CharField(max_length=120,null=False,blank=False)
#    #last_name=models.CharField(max_length=120,null=False,blank=False)
#    password=models.CharField(max_length=120,null=False,blank=False)
#    #Organization=models.CharField(max_length=120,null=True,blank=False)
#    email=models.EmailField(null=False,blank=False,unique=True)
#    #timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
#    #updated = models.DateTimeField(auto_now_add=False,auto_now=True)
#    
#    
#    def __str__(self):
#        #sequence=('self.first_name', 'self.last_name', 'self.email', 'self.Organization')
#        return str(self.email)
#        #return str(self.first_name|self.last_name|self.email|self.Organization)
