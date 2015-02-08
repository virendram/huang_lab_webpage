from django import forms
from .models import SignUp
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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
        #'password':forms.PasswordInput()
        #password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
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
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        
        if SignUp.objects.filter(email=email).exists():
            raise forms.ValidationError('A User with this email already exists!')
        else:
            return email
    
    def clean(self):
        if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password_conf']:
            raise forms.ValidationError("The password does not match ")
        return self.cleaned_data
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()
        return user
    
    lastSeenId = float('-Inf')
    rows = SignUp.objects.all().order_by('email')

    for row in rows:
        if row.email == lastSeenId:
            row.delete() # We've seen this id in a previous row
        else: # New id found, save it and check future rows for duplicates.
            lastSeenId = row.email
        pass