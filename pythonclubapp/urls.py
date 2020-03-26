from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='types'),
    path('getmeetings/', views.getmeetings, name='meeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingid'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]