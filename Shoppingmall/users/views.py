from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create.create_user(username=request.POST["username"],password=request.POST["password1"])
            print("here")
            return render(request,'home.html')

          #  auth.login(request,user)

    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            return render(request , 'login.html',{'error' : 'username or password is incorrect'})
    else:
        return render(request,'login.html')