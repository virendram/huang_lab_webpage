
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.

from .forms import SignUpForm

def home(request):
    
    return render_to_response("index.html",
                              locals(),
                              context_instance=RequestContext(request))
    

def download(request):
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

    form = SignUpForm(request.POST or None)
    
    
    if request.POST and form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        
        subject='Thank you for your interest'
        message='We will email you as soon as our site is updated'
        from_email=settings.EMAIL_HOST_USER
        to_list=[save_it.email]
        
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request,'Thank You! You can download the file now!')
        return HttpResponseRedirect('/download')
        
    
    return render_to_response("downloads.html",
                              locals(),
                              context_instance=RequestContext(request))
    

def aboutus(request):
    
    return render_to_response("about_us.html",
                              locals(),
                              context_instance=RequestContext(request))

def publications(request):
    
    return render_to_response("publications.html",
                              locals(),
                              context_instance=RequestContext(request))

def research(request):
    
    return render_to_response("research.html",
                              locals(),
                              context_instance=RequestContext(request))

def contactus(request):
    
    return render_to_response("contact_us.html",
                              locals(),
                              context_instance=RequestContext(request))