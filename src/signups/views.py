# Create your views here.


from django.conf import settings
from django.contrib import messages,auth
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse,get_object_or_404
from huang_webpage.settings import MEDIA_ROOT
from django.core.context_processors import csrf
import os
import hashlib,datetime,random
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms



from .forms import SignUpForm
from .models import SignUp

from .forms import MyLoginForm
from .models import MyLogin



def home(request):
    
    
    
    return render_to_response("index.html")

def research(request):
    
    
    return render_to_response("research.html")

def publications(request):
    
    
    return render_to_response("publications.html")

def contact_us(request):
    
    
    return render_to_response("contact_us.html")


def download(request):
    form = SignUpForm(request.POST or None)
    
    
    if form.is_valid():
        
        save_it = form.save()
        
        save_it.password = make_password(password=save_it.password,
                                   salt=None,
                                   hasher='pbkdf2_sha256')
        
        save_it.password_conf = save_it.password
        
        user_firstname = save_it.first_name
        user_lastname = save_it.last_name
        user_email = save_it.email
        user_organization = save_it.Organization
        user_password = save_it.password
        
        save_it.save()
        
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]            
        activation_key = hashlib.sha1((salt+user_email).encode('utf-8')).hexdigest()            
        key_expires = datetime.datetime.today() + datetime.timedelta(2)
        #key_expires = datetime.datetime.now() + datetime.timedelta()
        
        #Get user by username
        user = SignUp.objects.get(email=user_email)


        # Create and save user profile                                                                                                                                  
        
        
        
        new_profile = SignUp(first_name=user.first_name,
                             last_name=user.last_name,
                             email=user.email,
                             password=user.password,
                             position=user.position,
                             password_conf=user.password_conf,
                             Organization=user.Organization,
                             activation_key=activation_key,key_expires=key_expires)
        new_profile.save()
        
        # Send email with activation key
        email_subject = 'Account confirmation'
        email_body = "Dear %s, \
                     \n\nThank you for signing up. \
                     \n\nTo activate your account, please click this link within 48 hours http://127.0.0.1:8000/register_confirm/%s \
                     \n\nWarm Regards, \
                     \n\nWebmaster, \
                     \nBrain MRI Maps. \
                     \nwww.brainmrimaps.org" % (user_firstname, activation_key)
                     
        
        from_email=settings.EMAIL_HOST_USER
        to_list=[user_email]
            
            
        send_mail(email_subject,email_body,from_email,to_list,fail_silently=False)
            
        return render_to_response("verify_user.html")    
        
        
    else:
        return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))
    
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))
    

def register_confirm(request, activation_key):
    

    # check if there is UserProfile which matches the activation key (if not then display 404)
    signup_user = get_object_or_404(SignUp, activation_key=activation_key)


    #check if the activation key has expired, if it hase then render confirm_expired.html
    if signup_user.key_expires < timezone.now():
        
        #Get user by registered email and delete the instance
        user = SignUp.objects.filter(email=signup_user.email).delete()
        
        return render_to_response("confirmation_expired.html")

    #if the key hasn't expired save user and set him as active and render downloads page and send him an email
    
    signup_user_first_name = signup_user.first_name
    signup_user_last_name = signup_user.last_name
    signup_user_password = signup_user.password
    signup_user_email = signup_user.email
    signup_user_organization = signup_user.Organization
    
    
    signup_user.is_active = True
    signup_user.save()
    
    user = SignUp.objects.get(email=signup_user_email,is_active=False)
    user.delete()
    
    subject='Thank you for your interest'
        
    message = "Dear %s, \
              \n\nThank you for verifying your account. \
              \n\nYou can now access the download page by logging through your registered email address and password. \
              \n\nWe will be in touch when we have some new research to share! \
              \n\nWarm Regards, \
              \n\nWebmaster, \
              \nBrain MRI Maps. \
              \nwww.brainmrimaps.org" % (signup_user_first_name )
        
       
        
        
    from_email=settings.EMAIL_HOST_USER
    to_list=[signup_user_email]
    send_mail(subject,message,from_email,to_list,fail_silently=False)
        
    return render_to_response("thank-you.html")
   
       
    return render_to_response("login.html",
                              locals(),
                              context_instance=RequestContext(request))

def verify_user(request):
    return render_to_response("verify_user.html")

def confirmation_expired(request):
    return render_to_response("confirmation_expired.html")

def mass_email(request,permission_key):
    
    if request.method=='GET':
        totalusers=SignUp.objects.filter(is_active=True).count()
        
        if totalusers!=0:
            
            for i in range(totalusers):
                
                user=SignUp.objects.filter(is_active=True)[i]
                
                subject = 'News from Brain MRI Maps'
                message = "Dear %s, \
                          \n\nWe have some exciting news! \
                          \n\nPlease visit our webpage to have more information. \
                          \n\nWarm Regards, \
                          \n\nWebmaster, \
                          \nBrain MRI Maps. \
                          \nwww.brainmrimaps.org" % (user.first_name )
                from_email=settings.EMAIL_HOST_USER
                to_list=[user.email]
                
                send_mail(subject,message,from_email,to_list,fail_silently=False)
                
    
    return render_to_response("mass_email.html",
                              locals(),
                              context_instance=RequestContext(request))
    

def thank_you(request):
    return render_to_response("thank-you.html")

def login(request):
    form = MyLoginForm(request.POST or None)
    
    
    if form.is_valid():
        save_it = form.save()
        superuser_email = 'virendra.mishra@gmail.com'
        if superuser_email == save_it.email:
            subject='Super user access granted!'
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            permission_key = hashlib.sha1((salt+superuser_email).encode('utf-8')).hexdigest()            
            message = "Dear Superuser, \
                 \n\nYou have superuser permissions. \
                 \n\nPlease click this link to access page to send email to everyone on the registered list. http://127.0.0.1:8000/mass_email/%s \
                 \n\nWarm Regards, \
                 \n\nWebmaster, \
                 \nBrain MRI Maps. \
                 \nwww.brainmrimaps.org" % (permission_key)
            from_email=settings.EMAIL_HOST_USER
            to_list=[save_it.email]
            send_mail(subject,message,from_email,to_list,fail_silently=False)
            
        
        
            
        
        
        
        
        return render_to_response("downloads.html")

        
        
    return render_to_response("login.html",
                              locals(),
                              context_instance=RequestContext(request))

def signup(request):
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        
        save_it = form.save()
        
        save_it.password = make_password(password=save_it.password,
                                   salt=None,
                                   hasher='pbkdf2_sha256')
        
        save_it.password_conf = save_it.password
        
        user_firstname = save_it.first_name
        user_lastname = save_it.last_name
        user_email = save_it.email
        user_organization = save_it.Organization
        user_password = save_it.password
        
        save_it.save()
        
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]            
        activation_key = hashlib.sha1((salt+user_email).encode('utf-8')).hexdigest()            
        key_expires = datetime.datetime.today() + datetime.timedelta(2)
        #key_expires = datetime.datetime.now() + datetime.timedelta()
        
        #Get user by username
        user = SignUp.objects.get(first_name=user_firstname)


        # Create and save user profile                                                                                                                                  
        

        new_profile = SignUp(first_name=user.first_name,
                             last_name=user.last_name,
                             email=user.email,
                             password=user.password,
                             position=user.position,
                             password_conf=user.password_conf,
                             Organization=user.Organization,
                             activation_key=activation_key,key_expires=key_expires)
        new_profile.save()
        
        # Send email with activation key
        email_subject = 'Account confirmation'
        email_body = "Dear %s, \
                     \n\nThank you for signing up. \
                     \n\nTo activate your account, please click this link within 48 hours http://127.0.0.1:8000/register_confirm/%s \
                     \n\nWarm Regards, \
                     \n\nWebmaster, \
                     \nBrain MRI Maps. \
                     \nwww.brainmrimaps.org" % (user_firstname, activation_key)
                     
        
        from_email=settings.EMAIL_HOST_USER
        to_list=[user_email]
            
            
        send_mail(email_subject,email_body,from_email,to_list,fail_silently=True)
            
        return render_to_response("verify_user.html")    
        
        
    else:
        return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))
    
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

