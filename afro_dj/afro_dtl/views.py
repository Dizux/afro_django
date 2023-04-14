from django.shortcuts import render
#this auth module helps us authenticate on any model of ours.
#i.e username and password. so we dont have to recreate djangos authentication methods
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    username = 'Desire'
    gender = 'Male'
    return render(
        request,
        'index.html', 
        {'pr_title': pr_title, 'username':username, 'gender':gender}
    )

def register(request):
    return render(request, 'register.html')

def registration(request):
    print(request)
    user_name = request.POST['username']
    email = request.POST['user_email']
    password = request.POST['password']
    gender = request.POST['gender']
    userdetails = [user_name, email, password, gender]
    print(userdetails)
    if User.objects.filter(username=user_name).first():
        print("Username already exists")
        #returning to index for now, we havsent created a login page yet
        return render(request, 'index.html')
    else:
        user = User.objects.create_user(user_name, email, password)
        return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')