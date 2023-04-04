from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import SignUpForm
from .models import Event

'''HomePage'''
def home(request):
    return render(request, 'index.html')

'''Events'''
def events(request):
    events = Event.objects.all()
    print(events)
    return render(request, 'events.html', {'events': events})

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
@csrf_exempt 
def signup(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You have successfully regstered! Welcome")
            return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', context={"form":form})
    return render(request, 'signup.html', context={"form":form})

'''login'''
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in succesfully")
            return redirect('dashboard')
        else:
            messages.success(request, "There was an error loggin in, please try again...")
            return redirect('home')       
    else:
        return render(request, 'login.html', context={})
    
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect('home')