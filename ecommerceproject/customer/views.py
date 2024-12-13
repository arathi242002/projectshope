from django.shortcuts import render,redirect


from .models import Customermodel
from django.contrib import  messages
from .forms import Customerform
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(request):
    if (request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        if (password==cpassword):
            user=Customermodel.objects.create_user(username=username,password=password,email=email,address=address,cpassword=cpassword,phone=phone)
            user.save()
            return redirect('index')
        else:
            return HttpResponse("password not matching")


    return render(request, "register_account.html")


def login_account(request):
    if (request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password) 
        if user:
            login(request,user)
            return redirect('product_list')
        else:
             messages.error(request,"Invalid user")
    return render(request,'login_account.html')