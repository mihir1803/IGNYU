
# from django.contrib import admin
from django.urls import path
from first_app import views
from first_app import models

urlpatterns = [
    path('',views.index,name='index'),
    path('image/',views.Image,name='image'),
    path('voice/',views.Voice,name='voice'),
    path('registar',views.Registar_user,name='registar'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('index',views.index,name='index'),
    path('whatsapp',views.WhatsApp,name='whatsapp'),
    path('answer',views.Show_Ans,name='answer'),
    
    
   
]
