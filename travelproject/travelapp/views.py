from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from travelapp.models import Place,Profile


# Create your views here.
def index(request):
    obj= Place.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'index.html',{'result': obj, 'profile':profiles})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pas = request.POST['pas']
        repas = request.POST['repas']

        if pas == repas:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already exists")
                print("Username is already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already exists")
                print("Email is already exists")
                return redirect('register')
            else:
                user=User.objects.create(username=username,first_name=firstname,last_name=lastname,email=email,password=pas)
                user.save()
                print("Registration is successful")
                return redirect('login')
        else:
            messages.info(request,"Password is not matching")
            return redirect('register')

    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        user_name=request.POST['username']
        passw=request.POST['pas']
        user= auth.authenticate(username=user_name, password=passw)
        # print(user)
        # print(user_name)
        # print(passw)
        if user is not None:
            auth.login(request,user)
            print("Successfully Logged in")
            return redirect('/')

        else:
            messages.info(request,'login credential are not valid')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')