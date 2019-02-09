from django.db import models
class User_Details(models.Model):
    name=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100,primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    image=models.ImageField(upload_to='User_Images')