from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255, blank = False, null = True)
    photo = models.ImageField(upload_to='user_photos/')  # Assuming you have set up media file handling.
    email = models.EmailField()
    password = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=10)  
    age = models.IntegerField()
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10) 

    def __str__(self) -> str:
        return self.name