from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)