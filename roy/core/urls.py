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
    path('logout/', views.user_logout, name= 'logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('progress/', views.progress, name='myprogress'),
    path('classes/', views.clases, name='myclass'),
    path('reports/', views.admin_main, name = 'reports'),
    path('courses/', views.classes, name = 'courses'),
    path('lesson_one/', views.lesson_one, name = 'lesson_one'),
    path('lesson_two/', views.lesson_two, name = 'lesson_two'),
    path('lesson_three/', views.lesson_three, name = 'lesson_three'),
    path('lesson_four/', views.lesson_four, name = 'lesson_four'),
    path('lesson_five/', views.lesson_five, name = 'lesson_five'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)