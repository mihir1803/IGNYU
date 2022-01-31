from django.db import models
from django.contrib.auth.models import User


class ImageUpload(models.Model):
    Student_name = models.ForeignKey(User, on_delete = models.CASCADE)
    Disc = models.TextField()
    attechment  = models.ImageField(upload_to="attachments")

