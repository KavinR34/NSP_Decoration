from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Datas

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
"""

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

"""
def contact(request):
    mydata = Datas.objects.all()
    if (mydata!=""):
        return render(request,"contact.html",{"datas":mydata})
    else:
        return render(request,"contact.html")

def addData(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        eventdate = request.POST["eventdate"]
        venue = request.POST["venue"]
        typeofevent = request.POST["typeofevent"]
        messege = request.POST["messege"]

        obj = Datas()
        obj.Name = name
        obj.Phone = phone
        obj.Email = email
        obj.EventDate = eventdate
        obj.Venue = venue
        obj.TypeofEvent = typeofevent
        obj.Messege = messege
        obj.save()
        mydata = Datas.objects.all()
        return redirect("contact")
    return render(request,"contact.html")

def service(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())

def gallary(request):
    template = loader.get_template('gallary.html')
    return HttpResponse(template.render())