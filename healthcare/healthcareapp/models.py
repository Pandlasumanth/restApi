from django.db import models
class doctor(models.Model):
    id=models.IntegerField()
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    designation=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50)
    doctor_status=models.IntegerField(default=0)
    doctor_image=models.ImageField()
    def __str__(self):
        return self.name


class diseases(models.Model):
    diseases_id=models.IntegerField(primary_key=True)
    diseases_name=models.CharField(max_length=50)
    diseases_type=models.CharField(max_length=50)
    diseases_syptom=models.CharField(max_length=200)
    # pricicription=models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.diseases_name

class genric_medicines(models.Model):
    medicine_id=models.IntegerField(primary_key=True)
    medicine_name=models.CharField(max_length=50)
    medicine_price=models.DecimalField(max_digits=10,decimal_places=2)
    medicine_prescription=models.CharField(max_length=200)

    def __str__(self):
        return self.medicine_name
class nongenric_medicines(models.Model):
    medicine_id=models.IntegerField(primary_key=True)
    medicine_name=models.CharField(max_length=50)
    medicine_price=models.DecimalField(max_digits=10,decimal_places=2)
    medicine_prescription = models.CharField(max_length=200)

    def __str__(self):
        return self.medicine_name

class patients_register(models.Model):
    Id = models.IntegerField()
    Name = models.CharField(max_length=50)
    # User_id= models.IntegerField()
    Contact = models.IntegerField()
    Age = models.IntegerField()
    Date_of_birth=models.DateField()
    Gender = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=100)
    Height=models.DecimalField(max_digits=10,decimal_places=2)
    Weight=models.DecimalField(max_digits=10,decimal_places=2)
    Email = models.EmailField(max_length=50,primary_key=True)
    Password = models.CharField(max_length=50)
    Address=models.CharField(max_length=200)
    patient_status=models.IntegerField(default=0)
    patient_Image=models.ImageField()
    def __str__(self):
            return self.Name

class Chat(models.Model):
    sender=models.CharField(max_length=50)
    recevier=models.CharField(max_length=50)
    doctor_email=models.EmailField()
    patient_email=models.EmailField()
    message=models.CharField(max_length=500)
    submitted_time=models.DateTimeField(auto_now_add=True)
class Feedback(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200)
    Message=models.CharField(max_length=500)
class PatientFeedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Message = models.CharField(max_length=500)