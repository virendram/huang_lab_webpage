from django import forms
from .models import SignUp,MyLogin,MyForgotPassword,MyPasswordReset
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable)
import datetime

class SignUpForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['position'].label = ''
        self.fields['password'].label = ''
        self.fields['password_conf'].label = ''
        self.fields['email'].label = ''
        self.fields['Organization'].label = ''

    
    class Meta:
        
        model=SignUp
        widgets={
            'first_name': forms.TextInput(attrs={'size':50,'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'size':50,'placeholder':'Last Name'}),
            'position': forms.TextInput(attrs={'size':50,'placeholder':'Student/Postdoc/Faculty/Research Scientist'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password','size':50}),
            'password_conf':forms.PasswordInput(attrs={'placeholder': 'Re-enter Password','size':50}),
            'email': forms.TextInput(attrs={'size':50,'placeholder':'Email'}),
            'Organization': forms.TextInput(attrs={'size':50,'placeholder':'University/Company'}),
        }
        fields = ['first_name','last_name','position','password','password_conf','email','Organization']
        
    
    #def clean_email(self):
    #    if 'first_name' in self.cleaned_data and 'last_name' in self.cleaned_data and 'Organization' in self.cleaned_data:
    #        email = self.cleaned_data["email"]
    #        user = super(SignUpForm, self).save(commit=False)
    #        if SignUp.objects.filter(email=email).exists():
    #            raise forms.ValidationError('A User with this email has already been registered. Pleae login from the link below!')
    #        else:
    #            return email
    
    def clean(self):
        
        if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password_conf']:
            raise forms.ValidationError("The password does not match ")
        
        email = self.cleaned_data['email']
        if SignUp.objects.filter(email=email).exists():
            raise forms.ValidationError('A User with this email has already been registered. Pleae login from the link below!')
        return self.cleaned_data
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()
        #else:
        #    raise forms.ValidationError('Something is wrong')
        return user
        
    
    
    

class MyLoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['password'].label = ''
        
    class Meta:
        
        model=MyLogin
        widgets={
            'email': forms.TextInput(attrs={'size':50,'placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password','size':50}),
        }
        fields = ['email','password']
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if SignUp.objects.filter(email=email).exists():
            if len(SignUp.objects.filter(email=email,is_active=True))>=1:
                
                return email
                
            else:
                
                raise forms.ValidationError('Please activate yourself by clicking on the email sent to your registered email or Please click below to request activation email!')
            
        else:
            
            raise forms.ValidationError('A User with this email does not exist!')
        
       
   
    def clean(self):
        
        if 'email' in self.cleaned_data:
            password = self.cleaned_data["password"]
            email = self.cleaned_data["email"]
            
            stored_password=SignUp.objects.get(email=email,is_active=True)
            if check_password(password,stored_password.password)== False:
                raise forms.ValidationError('Entered password does not match the registered password!')


class MyForgotPasswordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyForgotPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        
        
    class Meta:
        
        model= MyForgotPassword
        widgets={
            'email': forms.TextInput(attrs={'size':50,'placeholder':'Email'}),
            
        }
        fields = ['email']
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if SignUp.objects.filter(email=email).exists():
            return email
                     
        else:            
            raise forms.ValidationError('A User with this email does not exist!')
        
class MyPasswordResetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['password'].label = ''
        self.fields['password_conf'].label = ''
        
    
    class Meta:
        
        model=MyPasswordReset
        widgets={
            'email': forms.TextInput(attrs={'size':50,'placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password','size':50}),
            'password_conf':forms.PasswordInput(attrs={'placeholder': 'Re-enter Password','size':50}),
            
            
        }
        fields = ['email','password','password_conf']
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        user = super(MyPasswordResetForm, self).save(commit=False)
        
        if SignUp.objects.filter(email=email).exists():
            return email
        else:
            raise forms.ValidationError('A User with this email does not exist!')
            
    
    def clean(self):
        if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password_conf']:
            raise forms.ValidationError("The password does not match ")
        return self.cleaned_data
    

    
    
    