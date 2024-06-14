from django.shortcuts import render,redirect
from .forms import customerform
from .models import customer
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def contactpage(request):
    return render(request,"contact.html")

def bookingpage(request):
    return render(request,"booking.html")

def aboutpage(request):
    return render(request,"about.html")

def menupage(request):
    return render(request,"menu.html")

def addmenu(req):
    return render(req,"addmenu.html")

def customerreg(request):
    if request.method == "POST":
        customerdata=customerform(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"the username already exists...")
            return redirect(customerreg)
        if customerdata.is_valid():
            customerdata.save()
            user=User.objects.create_user(username=username,password=password)
            user.save()
            return redirect(indexpage)
    else:
        return render(request,"customerRegistration.html")

    
    