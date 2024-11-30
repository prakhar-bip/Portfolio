from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth .decorators import login_required
from .models import *

def register(request):
    if (request.method == 'POST'):
        fname = request.POST.get('first_name')
        email = request.POST.get('email')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cnf_password = request.POST.get('confirm_password')
        
        if (password != cnf_password):
            print("Passwords not match")
            return redirect('register')
        print("Worked")
        user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=(password))
        user.save()
        return render(request , 'Home.html')
    return render(request , 'Register.html')


def user_login(request):
    if (request.method == 'POST'):
        usename = request.POST.get('usename')
        pasword = request.POST.get('pasword')

        user = authenticate(username = usename , password = pasword)
        if user is not None:
            login(request, user)
            messages.success(request , f"{usename} logged in successfully")
            return render(request , 'Home.html')
        else:
            return redirect('Site_home')
    
    return redirect('register')

@login_required
def home_page(request):
    return render(request, 'Home.html')


def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully")
    return redirect('login_user')

@login_required
def portfolio(request):
    return render(request , "portfolio.html")

@login_required
def Save_contact(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        contact = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']

        detail = contact_details(Name = name , Email = email , Contact_number = contact , Messages = message)
        detail.save()
    
    return redirect("portfolio")

@login_required
def show_pp(request):
    projects = python_projects.objects.all()
    return render(request , "projects.html" , {'projects':projects})
    

@login_required
def resume(request):
    return render(request , "resume.html")

