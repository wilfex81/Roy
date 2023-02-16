from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.views import LoginView

'''HomePage'''
def home(request):
    return render(request, 'index.html')

'''Events'''
def events(request):
    return render(request, 'events.html')

'''camps'''
def camps(request):
    return render(request, 'camps.html')

'''contact'''
def contact(request):
    return render(request, 'contact.html')

'''Dasboard'''
def dashboard(request):
    return render(request, 'dashboard.html')

'''progress'''
def progress(request):
    return render(request, 'progress.html')

'''classes'''
def clases(request):
    return render(request, 'classes.html')

'''signup'''
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("core:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form= NewUserForm()
    return render(request, 'signup.html', context={"form":form})

'''login'''
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "dashboard.html")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', context={"login_form":form})


