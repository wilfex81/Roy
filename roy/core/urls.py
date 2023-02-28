from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name= 'home'),
    path('events/', views.events, name= 'events'),
    path('camps/', views.camps, name= 'camps'),
    path('contact/', views.contact, name= 'contacts'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.user_login, name= 'login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('progress/', views.progress, name='myprogress'),
    path('classes/', views.clases, name='myclass')
]