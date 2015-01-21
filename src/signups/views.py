from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

from .forms import SignUpForm

def home(request):
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        messages.success(request,'Thank You! You can download the file now!')
        return HttpResponseRedirect('/download')
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def download(request):
    
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