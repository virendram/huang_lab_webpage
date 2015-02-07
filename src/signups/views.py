
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from huang_webpage.settings import MEDIA_ROOT
import os
import hashlib
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

# Create your views here.

from .forms import SignUpForm
#from .forms import LoginForm

def home(request):
    
    #return render_to_response("index.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))
    
    return render_to_response("index.html")

def research(request):
    
    #return render_to_response("research.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))
    return render_to_response("research.html")

def publications(request):
    
    #return render_to_response("publications.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))
    return render_to_response("publications.html")

def contact_us(request):
    
    #return render_to_response("contact_us.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))
    return render_to_response("contact_us.html")

   
def download(request):
    
    form = SignUpForm(request.POST or None)
  #  login_form = LoginForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        
        save_it.password = make_password(password=save_it.password,
                                   salt=None,
                                   hasher='pbkdf2_sha256')
        
        user_firstname = save_it.first_name
        user_lastname = save_it.last_name
        user_email = save_it.email
        user_organization = save_it.Organization
        
        save_it.save()
        
        subject='Thank you for your interest'
        
        file=open(MEDIA_ROOT+os.path.sep+'email_message.txt','r')
        message=file.read()
        file.close()
        
        
        from_email=settings.EMAIL_HOST_USER
        to_list=[save_it.email]
        
        #send_mail(subject,message,from_email,to_list,fail_silently=True)
        #messages.success(request,'Thank You! You can download the file now!')
        #return HttpResponseRedirect('/download')
        return render_to_response("downloads.html")
    else:
        return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))
    
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))
    


    #form = SignUpForm(request.POST or None)
    #
    #
    
    #    #else:
    #    #    return render_to_response("signup.html",
    #    #                              locals(),
    #    #                              context_instance=RequestContext(request))
    ##else:
    #return render_to_response("downloads.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))
    #
    
    
    #return render_to_response("downloads.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))
    #






