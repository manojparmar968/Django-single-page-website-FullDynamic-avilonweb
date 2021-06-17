from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .models import *
from django.contrib import messages

# Create your views here.
class Index(View):
    template_name = 'webapp/index.html'
    def get(self, request, *args, **kwargs):
        team = Team.objects.all()
        gallery = Gallery.objects.all()
        frquently = FrequentlyAskedQuestions.objects.all()
        client = Client.objects.all()
        about_us = AboutUs.objects.filter().last()
        about_us_points = AboutUsPoints.objects.filter(aboutus=about_us)
        context = {
            "team":team,
            "gallery":gallery,
            "frquently":frquently,
            "client": client,
            "about_us":about_us,
            "about_us_points": about_us_points,
            
        }
        return render(request, self.template_name, context)

    def post(self,request):
        contact = ContactForm()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request, 'Thanks for contacting us. We have received your message, and will be in contact with you shortly!')
        # return render(request,self.template_name,{})
        return redirect('/')