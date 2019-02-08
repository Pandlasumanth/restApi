from django.db import models
class doctor(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    designation=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    doctor_status=models.IntegerField(default=0)
    doctor_image=models.ImageField(default='noimage.jpg')

class patients(models.Model):
    patient_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    disease_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
class diseases(models.Model):
    diseases_id=models.IntegerField(primary_key=True)
    diseases_name=models.CharField(max_length=50)
    diseases_type=models.CharField(max_length=50)
    diseases_syptom=models.CharField(max_length=200)
class genric_medicines(models.Model):
    medicine_id=models.IntegerField(primary_key=True)
    medicine_name=models.CharField(max_length=50)
    medicine_price=models.DecimalField(max_digits=10,decimal_places=2)
class nongenric_medicines(models.Model):
    medicine_id=models.IntegerField(primary_key=True)
    medicine_name=models.CharField(max_length=50)
    medicine_price=models.DecimalField(max_digits=10,decimal_places=2)

class patients_register(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    # User_id= models.IntegerField()
    Contact = models.IntegerField()
    Age = models.IntegerField()
    Date_of_birth=models.DateField()
    Gender = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=100)
    Height=models.DecimalField(max_digits=10,decimal_places=2)
    Weight=models.DecimalField(max_digits=10,decimal_places=2)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Address=models.CharField(max_length=200)
    patient_status=models.IntegerField(default=0)
    patient_Image=models.ImageField()

class Prescription(models.Model):
    Prescription_id=models.IntegerField(primary_key=True)
    Genric_medicine=models.CharField(max_length=120)
    Nongenric_medicines=models.CharField(max_length=20)
    Test=models.CharField(max_length=200)

class Report(models.Model):
    patients_id=models.ForeignKey(patients,on_delete=models.CASCADE)
    Results=models.CharField(max_length=500)
class Chat(models.Model):
    sender=models.CharField(max_length=50)
    recevier=models.CharField(max_length=50)
    doctor_email=models.EmailField()
    patient_email=models.EmailField()
    message=models.CharField(max_length=500)
    submitted_time=models.DateTimeField(auto_now_add=True)
