"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from healthcareapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homelogin),
    path('home/', views.homelogin),
    path('patientlogin/', views.patientlogin),
    path('doctorlogin/', views.DoctorLogin),
    path('CheckDoctorLogin/', views.CheckDoctorLogin),
    path('patientregister/', views.patientregisterpage),
    path('patientreg/', views.patientregister),
    path('CheckLogin/', views.CheckLogin),

    path('plogout/', views.PLogout),
    path('dlogout/', views.DLogout),
    path('medicines/', views.ViewMedicines),
    path('diseases/', views.ViewDiseases),
    path('about_us/', views.OpenAbout),
    path('sendprequest/', views.SendMessage),
    path('sendmessage/', views.PatientRequest),





    path('PatientProfile/', views.PatientProfile),
    path('viewmedicines/', views.ViewMedicinesp),
    path('viewdiseases/', views.ViewDiseasesp),
    path('viewdoctors/', views.ViewDoctorsp),
    path('DoctorProfile/', views.DoctorProfile),
    path('viewmedicinesd/', views.ViewMedicinesd),
    path('viewdiseasesd/', views.ViewDiseasesd),
    path('viewpatients/', views.ViewPatients),
    path('viewrequests/', views.ViewRequests),
    path('sendresponse/', views.SendResponse),
    path('sendresmessage/', views.SendResponseMsg),
    path('openupdatepprofile/', views.UpdatePatientProfile),
    path('openupdatedprofile/', views.UpdateDoctorProfile),
    path('UpdateProfilePatient/', views.UpdateProfilePatientSave),
    path('UpdateProfileDoctor/', views.UpdateProfileDoctorSave),
    path('ChangePasswordP/', views.ChangePasswordP),
    path('ChangepasswordD/', views.ChangePasswordD),
    path('patient_change_password/', views.patient_change_password),
    path('doctor_change_password/', views.doctor_change_password),
    path('pforgotpassword/', views.pforgotpassword),
    path('SendPasswordP/', views.SendPasswordP),
    path('dforgotpassword/', views.dforgotpassword),
    path('SendPasswordD/', views.SendPasswordD),
    path('feedback/', views.FeedBackFrom),
    path('pfeedback/', views.PatientFeedBackFrom),

]
