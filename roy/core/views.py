from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import SignUpForm, ContactForm
from .models import Event, ContactsSaved
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.views.decorators import staff_member_required

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect



@staff_member_required
def admin_main(request,object=Event):
    LogEntry.objects.log_action(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(Event).pk,
        object_repr=str(Event.objects.all()),
        object_id=object.id,
        change_message="Items added",
        action_flag=ADDITION)
    logs = LogEntry.objects.exclude(object_id__icontains='django.db.').exclude(object_id__icontains = 'property object').order_by('-action_time')[:40]

    return render(request,'reports.html', {"logs":logs})

'''HomePage'''
def home(request):
    return render(request, 'index.html')

'''Events'''
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

'''camps'''
def camps(request):
    return render(request, 'camps.html')

'''contact'''
def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            user = ContactsSaved.objects.create(first_name = first_name,  last_name = last_name, email = email, subject = subject,  message = message)
            user.save()
            # try:
            #     send_mail(subject, message, email, ["admin@example.com"])
            # except BadHeaderError:
            #     return HttpResponse("Invalid header found.")
            return redirect("home")
    return render(request, "contact.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

'''Dasboard'''
def dashboard(request):
    return render(request, 'dashboard.html')

'''classes'''
def classes(request):
    return render(request, 'progress.html')

'''lesson 1'''
def lesson_one(request):
    return render(request, 'lesson1.html')

'''lesson 2'''
def lesson_two(request):
    return render(request, 'lesson2.html')

'''lesson 3'''
def lesson_three(request):
    return render(request, 'lesson3.html')

'''lesson 4'''
def lesson_four(request):
    return render(request, 'lesson4.html')

'''lesson 5'''
def lesson_five(request):
    return render(request, 'lesson5.html')

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
