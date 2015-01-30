from django.db import models
#from django.utils.encoding import smart_unicode
# Controls the user database

class SignUp(models.Model):
    first_name=models.CharField(max_length=120,null=False,blank=False)
    last_name=models.CharField(max_length=120,null=False,blank=False)
    Organization=models.CharField(max_length=120,null=True,blank=False)
    email=models.EmailField(null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    #def __str__(self):
    #    return str(self.email)
    
    def __str__(self):
        return str(self.first_name)
    
    #def __str__(self):
     #   return str(self.last_name)
    
    
