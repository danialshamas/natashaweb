from django.shortcuts import render
from . forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'web/index.html',{})

def company_profile(request):
    return render(request,'web/companyprofile.html',{})

def products(request):
    return render(request,'web/products.html',{})

def quality(request):
    return render(request,'web/qualitystand.html',{})

def design(request):
    return render(request,'web/designstd.html',{})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            send_mail(your_name, message, your_email,['daniyalshamas6@gmail.com'], fail_silently=False)
        
    return render(request, "web/contact.html", {'form': form})


    
