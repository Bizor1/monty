from .forms import UserContactsForm
# from mysite.jonathan.models import UserContacts
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import UserContacts

# Create your views here.
from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
# from .forms import ContactForm

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
    
    
    


class ContactPageView(TemplateView):
    template_name = "contact.html"
    def post(self, request, *args, **kwargs):
            usercontacts=UserContacts()
            form= UserContactsForm(request.POST or None)
            if form.is_valid():
                usercontacts.name= form.cleaned_data.get("name")
                usercontacts.email= form.cleaned_data.get("email")
                usercontacts.subject= form.cleaned_data.get("subject")
                usercontacts.message= form.cleaned_data.get("message")
                usercontacts.save()
                print('yes')
                

               
               
               
        
        
         
            return render(request, 'contact.html')



        

class GalleryPageView(TemplateView):
    template_name = "gallery.html"

class OurHistoryPageView(TemplateView):
    template_name = "our-history.html"

class OurServicesPageView(TemplateView):
    template_name = "our-services.html"

class PremiumPageView(TemplateView):
    template_name = "premium.html"

class NotFoundPageView(TemplateView):
    
    template_name = "404.html"
    


def error_404_exception(request, exception):
    return render(request, '404.html')


def index(request):
    if request.method == "POST":
        print("yes")
    return render(request,"index.html")

def contact(request):
    if request.method =="POST":
        print('COOL')
    return render(request, "contact.html")
