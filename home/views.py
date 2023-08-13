from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
#user Pragya Hello007

#makemigrations - create changes and store in a file
#migrate - apply the pending changes xreatwd by makemigrations
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return Httpresponse("this is home page")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")