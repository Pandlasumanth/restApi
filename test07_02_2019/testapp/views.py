from django.shortcuts import render

# Create your views here.
def ShowIndex(request):
    return render(request,"index.html")
def ShowRegister(request):
    return render(request,"newregister.html")


def SaveUser(request):
    return render(request,"newregister.html",{"msg":"Registered Successfully"})


def ValidateUser(request):
    return render(request,"dashboard.html",{"data":'qs','type':"dashboard"})


def UpdateProfile(request):
    return render(request,"dashboard.html",{"type":"upadteprofile","data":"qs"})
def DeleteProfile(request):
    return render(request,"dashboard.html",{"type":"deleteprofile","data":"qs"})


def UDashboard(request):
    return render(request,"dashboard.html",{"data":'qs','type':"dashboard"})