from django import forms
from .models import SignUp
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['position'].label = ''
        self.fields['password'].label = ''
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
            #'password': forms.TextInput(attrs={'size':80,'placeholder':'Password'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password','size':50}),
            'email': forms.TextInput(attrs={'size':50,'placeholder':'Email'}),
            'Organization': forms.TextInput(attrs={'size':50,'placeholder':'University/Company'}),
        }
        fields = ['first_name','last_name','position','password','email','Organization']
        
        
        
#class LoginForm(forms.ModelForm):
#    
#    def __init__(self, *args, **kwargs):
#        super(SignUpForm, self).__init__(*args, **kwargs)
#        self.fields['first_name'].label = ''
#        self.fields['last_name'].label = ''
#        self.fields['password'].label = ''
#        self.fields['email'].label = ''
#        self.fields['Organization'].label = ''
#
#    
#    class Meta:
#        #'password':forms.PasswordInput()
#        #password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#        model=SignUp
#        widgets={
#            'first_name': forms.TextInput(attrs={'size':40,'placeholder':'First Name'}),
#            'last_name': forms.TextInput(attrs={'size':40,'placeholder':'Last Name'}),
#            #'password': forms.TextInput(attrs={'size':80,'placeholder':'Password'}),
#            'password':forms.PasswordInput(attrs={'placeholder': 'Password','size':40}),
#            'email': forms.TextInput(attrs={'size':40,'placeholder':'Email'}),
#            'Organization': forms.TextInput(attrs={'size':40,'placeholder':'University/Company'}),
#        }
#        fields = ['first_name','last_name','password','email','Organization']