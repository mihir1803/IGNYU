from django.db import models
from django.contrib.auth.models import User
# from first_app.models import ImageUpload

# Create your models here.
class Show_Image(models.Model):
    Student_Name = models.CharField(max_length=200)
    Student_Disc =  models.TextField()
    Attechment  = models.ImageField(upload_to="attachments")
    # imageURL = models.URLField(null=True , blank= True)
    Answer =models.TextField(default="")