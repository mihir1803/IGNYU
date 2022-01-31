
from Admin_app import views
from Admin_app import models
from django.urls import path

urlpatterns = [
   path('imageshow/',views.Image_Show,name='imageshow'),
]