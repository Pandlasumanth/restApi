from django.shortcuts import render
from testapp.models import User_Details
# Create your views here.
def ShowIndex(request):
    return render(request,"index.html")
def ShowRegister(request):
    return render(request,"newregister.html")


def SaveUser(request):
    name=request.POST['name']
    cno=request.POST['ucontact']
    uname=request.POST['uname']
    upass=request.POST['upass']
    uimg=request.FILES['uimg']
    User_Details(name=name,contact_no=cno,username=uname,password=upass,image=uimg).save()
    return render(request,"newregister.html",{"msg":"Registered Successfully"})


def ValidateUser(request):
    uname = request.POST['uname']
    upass = request.POST['upass']
    qs=User_Details.objects.get(username=uname,password=upass)
    if qs:
        return render(request,"dashboard.html",{"data":qs,'type':"dashboard"})
    else:
        return render(request,"index.html",{"msg":"Invalid User"})


def UpdateProfile(request):
    cno=request.GET['id']
    qs=User_Details.objects.get(contact_no=cno)
    return render(request,"dashboard.html",{"type":"updateprofile","data":qs})
def DeleteProfile(request):
    cno=request.GET['id']
    qs=User_Details.objects.get(contact_no=cno)
    return render(request,"dashboard.html",{"type":"deleteprofile","data":qs})


def UDashboard(request):
    cno=request.GET['id']
    qs=User_Details.objects.get(contact_no=cno)
    return render(request,"dashboard.html",{"data":qs,'type':"dashboard"})


def UpdateUser(request):
    type=request.GET['id']
    name = request.POST['name']
    cno = request.POST['ucno']
    uname = request.POST['uname']
    upass = request.POST['upass']
    if type != cno:
        data_avilable=User_Details.objects.filter(contact_no=cno)
        if data_avilable:
            qs = User_Details.objects.get(contact_no=type)
            return render(request,"dashboard.html",{"type":"updateprofile","data":qs,"msg":"the contact number is already avialable"})
    else:
        try:
            uimg = request.FILES['uimg']
            User_Details.objects.filter(contact_no=type).update(name=name, contact_no=cno, username=uname, password=upass,image=uimg)
        except:
            User_Details.objects.filter(contact_no=type).update(name=name, contact_no=cno, username=uname, password=upass)
        finally:
            qs=User_Details.objects.get(contact_no=cno)
            return render(request,"dashboard.html",{"type":"updateprofile","data":qs,"msg":"updated successfully"})


def DeleteUser(request):
    cno=request.POST['cno']
    User_Details.objects.filter(contact_no=cno).delete()

    return render(request,"index.html",{"msg":"deleted Successfully"})