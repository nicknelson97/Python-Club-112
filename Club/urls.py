from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('resources/', views.resources, name='resources'),
    path('meetdetails/<int:id>', views.meetdetails, name='meetdetails'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]