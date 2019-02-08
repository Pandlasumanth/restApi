from django.shortcuts import render
from  .models import diseases
from .models import nongenric_medicines,genric_medicines,patients_register,doctor,diseases,Chat

# Create your views here.
def homelogin(request):
    type="homepage"
    doctorinfo=doctor.objects.all()

    return render(request,"index.html",{"type":type,'doctorsInfo':doctorinfo})
def patientlogin(request):
    try:
        session=request.session['pemail']
        if session != '':

            pdetails=patients_register.objects.get(Email=session)
            return render(request,"patient_home.html",{"pdetails":pdetails})
        else:
            type = request.GET.get("type")
            return render(request,"index.html",{"type":type})
    except:
        type=request.GET.get("type")
        return render(request,"index.html",{"type":type})

def DoctorLogin(request):
    try:
        session=request.session['demail']
        if session != '':

            ddetails=doctor.objects.get(email=session)

            return render(request,"doctor_home.html",{"ddetails":ddetails})
        else:
            type = request.GET.get("type")
            return render(request,"index.html",{"type":type})
    except:
        type=request.GET.get("type")
        return render(request,"index.html",{"type":type})
def CheckDoctorLogin(request):
    email = request.POST.get('demail')
    password = request.POST.get('dpassword')
    try:
        cp = doctor.objects.get(email=email, password=password)
        if cp:


            request.session['demail'] = email
            dr=doctor(id=cp.id,name=cp.name,contact=cp.contact,designation=cp.designation,email=cp.email,password=cp.password,doctor_status=1)
            dr.save()
            return render(request, "doctor_home.html", {"ddetails": cp})
        else:
            return render(request, "index.html", {"type": "H_Doctor", "message1": "Invalid Details Please Register.."})
    except:
        return render(request, "index.html", {"type": "H_Doctor", "message1": "Invalid Details Please Register.."})


def patientregisterpage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def patientregister(request):
    Id=request.POST.get("idno")
    Name=request.POST.get("name")
    # User_id=request.POST.get("userid")
    Contact=request.POST.get("contact")
    Age=request.POST.get("age")
    date_of_birth=request.POST.get('dob')
    Gender=request.POST.get("gender")
    Occupation=request.POST.get("occupation")
    Height=request.POST.get("height")
    Weight=request.POST.get("weight")
    Email=request.POST.get("email")
    Password=request.POST.get("password")
    Address=request.POST.get("address")
    from .models import patients_register
    ps=patients_register(Id=Id,Name=Name,Contact=Contact,Age=Age,Date_of_birth=date_of_birth,Gender=Gender,Occupation=Occupation,Height=Height,Weight=Weight,Email=Email,Password=Password,Address=Address)
    ps.save()
    return render(request,"index.html",{"type":'H_patient',"message":'registered successfully'})
def CheckLogin(request):
    email=request.POST.get('pemail')
    password=request.POST.get('ppassword')
    from  .models import patients_register
    try:
        cp=patients_register.objects.get(Email=email,Password=password)
        if cp:

            doctorinfo=doctor.objects.all()
            request.session['pemail']=email
            return render(request,"patient_home.html",{"pdetails":cp,"doctor":doctorinfo})
        else:
            return render(request,"index.html",{"type":"H_patient","message1":"Invalid Details Please Register.."})
    except:
        return render(request, "index.html", {"type": "H_patient", "message1": "Invalid Details Please Register.."})


def diseaseslogin(request):
    type=request.GET.get("type")
    doctorinfo=doctor.objects.all()

    return render(request,"index.html",{"type":type,'doctorsInfo':doctorinfo})



    ngeneric=nongenric_medicines.objects.all()
    if ngeneric.count()>0:
        return render(request,"patient_home.html",{"ngeneric":ngeneric,"pdetails":pdetails})
    else:
        return render(request,"patient_home.html",{"pdetails":pdetails})
def PLogout(request):
    request.session['pemail']=''
    doctorinfo=doctor.objects.all()
    return render(request,"index.html",{'doctorsInfo':doctorinfo})
def DLogout(request):
    try:

        session=request.session['demail']
        cp=doctor.objects.get(email=session)

        dr = doctor(id=cp.id,name=cp.name, contact=cp.contact, designation=cp.designation, email=cp.email, password=cp.password,doctor_status=0)
        dr.save()
        request.session['demail']=''
        doctorinfo=doctor.objects.all()
        return render(request,"index.html",{'doctorsInfo':doctorinfo})
    except:
        request.session['demail'] = ''
        doctorinfo = doctor.objects.all()
        return render(request, "index.html", {'doctorsInfo': doctorinfo})

def ViewMedicines(request):
    generic=genric_medicines.objects.all()
    ngeneric=nongenric_medicines.objects.all()
    return render(request,"medicines.html",{"generic":generic,"ngeneric":ngeneric})

def ViewDiseases(request):
    disease=diseases.objects.all()
    return render(request,"diseases.html",{"diseases":disease})
def OpenAbout(request):
    return render(request,"about_us.html")
def SendMessage(request):
    doctorname=request.GET.get('id')
    # data=dname.split('-')
    dname=doctor.objects.get(email=doctorname)
    patientname=request.GET.get('pemail')
    patient_name=patients_register.objects.get(Email=patientname)
    doctorinfo = doctor.objects.filter(doctor_status=1)
    requestw='patientreq'
    try:
        chathistory = Chat.objects.filter(doctor_email=dname.email, patient_email=patient_name.Email)

        return render(request, "patient_home.html", {"pdetails":patient_name,"pname":patient_name.Name,"patientreq":requestw,"dname":dname.name,"demail":dname.email ,"doctor": doctorinfo,'chathistory':chathistory})
    except:
        return render(request, "patient_home.html", {"pdetails":patient_name,"pname":patient_name.Name,"patientreq":requestw,"dname":dname.name,"demail":dname.email ,"doctor": doctorinfo})









def PatientProfile(request):
    email=request.GET.get('id')
    profile=patients_register.objects.get(Email=email)
    return render(request,"patient_home.html",{"profile":profile,"pdetails":profile})
def ViewMedicinesp(request):
    email = request.GET.get('id')
    try:
        details = patients_register.objects.get(Email=email)
        generic = genric_medicines.objects.all()
        ngeneric = nongenric_medicines.objects.all()
        return render(request, "patient_home.html", {"generic": generic, "ngeneric": ngeneric, 'pdetails': details})
    except:
        generic = genric_medicines.objects.all()
        ngeneric = nongenric_medicines.objects.all()
        return render(request, "medicines.html", {"generic": generic, "ngeneric": ngeneric})

def ViewDiseasesp(request):
    try:
        email = request.GET.get('id')
        details = patients_register.objects.get(Email=email)
        disease=diseases.objects.all()
        return render(request,"patient_home.html",{"pdetails":details,"diseases":disease})
    except:
        disease = diseases.objects.all()
        return render(request, "diseases.html", { "diseases": disease})

def ViewDoctorsp(request):
    email = request.GET.get('id')
    details = patients_register.objects.get(Email=email)
    doctors=doctor.objects.all()
    return render(request,"patient_home.html",{"pdetails":details,"doctors":doctors})
def DoctorProfile(request):
    email = request.GET.get('id')
    profile = doctor.objects.get(email=email)
    return render(request, "doctor_home.html", {"profile": profile, "ddetails": profile})


def ViewMedicinesd(request):
    email = request.GET.get('id')
    details = doctor.objects.get(email=email)
    generic = genric_medicines.objects.all()
    ngeneric = nongenric_medicines.objects.all()
    return render(request, "doctor_home.html", {"generic": generic, "ngeneric": ngeneric, 'ddetails': details})


def ViewDiseasesd(request):
    email = request.GET.get('id')
    details = doctor.objects.get(email=email)
    disease = diseases.objects.all()
    return render(request, "doctor_home.html", {"ddetails": details, "diseases": disease})


def ViewPatients(request):
    email = request.GET.get('id')
    details = doctor.objects.get(email=email)
    patients = patients_register.objects.all()
    return render(request, "doctor_home.html", {"ddetails": details, "patients": patients})


def PatientRequest(request):
    pemail=request.GET.get('email')
    demail=request.GET.get('demail')
    sender=request.POST.get('pname')
    reciever=request.POST.get('dname')
    message=request.POST.get('chat')

    import datetime

    date =datetime.datetime.now()
    cha=Chat(sender=sender,doctor_email=demail,patient_email=pemail,recevier=reciever,message=message,submitted_time=date)
    cha.save()
    doctors=doctor.objects.filter(doctor_status=1)
    pdetails=patients_register.objects.get(Email=pemail)
    try:
        chathistory=Chat.objects.filter(doctor_email=demail,patient_email=pemail)
        return render(request,"patient_home.html",{"dname":reciever,"pname":sender,'pdetails':pdetails,"doctor":doctors,"sendmessage":'send','message':'request sent','chathistory':chathistory})
    except:
        return render(request,"patient_home.html",{"dname":reciever,"pname":sender,'pdetails':pdetails,"doctor":doctors,"sendmessage":'send','message':'request sent'})


def ViewRequests(request):
    email=request.GET.get('id')

    ddetails=doctor.objects.get(email=email)

    try:
        demails=Chat.objects.filter(doctor_email=email,recevier=ddetails.name).order_by('submitted_time')
        dmsg=[]
        for x in demails:
            try:
                if dmsg==[]:
                    dmsg.append(x)
                else:
                    for y in dmsg:
                        if y.patient_email == x.patient_email:
                            dmsg.remove(y)
                            dmsg.append(x)
                        else:
                            dmsg.append(x)
            except:
                dmsg.append(x)

        return render(request,"doctor_home.html",{"ddetails":ddetails,'demails':dmsg,'requests':'requests'})
    except:
        return render(request,"doctor_home.html",{"ddetails":ddetails,'requests':'requests','demails':'No Requests Are Found'})





def SendResponse(request):
    doctorname = request.GET.get('id')
    dname = doctor.objects.get(email=doctorname)
    patientname = request.GET.get('pemail')
    patient_name = patients_register.objects.get(Email=patientname)

    response = 'doctorres'
    try:
        chathistory = Chat.objects.filter(doctor_email=dname.email, patient_email=patient_name.Email)

        return render(request, "doctor_home.html",
                      {"ddetails": dname, "pname": patient_name.Name, "patientreq": response,
                       "dname": dname.name, "demail": dname.email, 'chathistory': chathistory,'pemail':patient_name.Email})
    except:
        return render(request, "doctor_home.html",
                      {"ddetails": patient_name, "pname": patient_name.Name, "patientreq": response,
                       "dname": dname.name, "demail": dname.email,"pemail":patient_name.Email})


def SendResponseMsg(request):
    pemail = request.GET.get('email')
    demail = request.GET.get('demail')
    sender = request.POST.get('dname')
    reciever = request.POST.get('pname')
    message = request.POST.get('chat')

    import datetime

    date = datetime.datetime.now()
    cha = Chat(sender=sender, doctor_email=demail, patient_email=pemail, recevier=reciever, message=message,
               submitted_time=date)
    cha.save()

    pdetails = doctor.objects.get(email=demail)
    try:
        chathistory = Chat.objects.filter(doctor_email=demail, patient_email=pemail)
        return render(request, "doctor_home.html",
                      {"dname": sender, "pname": reciever, 'ddetails': pdetails,
                       "sendresmessage": 'send', 'message': 'response sent', 'chathistory': chathistory})
    except:
        return render(request, "doctor_home.html",
                      {"dname": reciever, "pname": sender, 'pdetails': pdetails,
                       "sendresmessage": 'send', 'message': 'response sent'})


def UpdatePatientProfile(request):
    email=request.GET['email']
    pdetails=patients_register.objects.get(Email=email)
    return render(request,"patient_home.html",{"pdetails":pdetails,"type":'patientupdate'})


def UpdateProfilePatientSave(request):
    id=request.POST['pid']
    name=request.POST['pname']
    contact=request.POST['pcontact']
    age=request.POST['page']
    dob=request.POST['pdob']
    gender=request.POST['pgender']
    occupation=request.POST['poccupation']
    height=request.POST['pheight']
    weight=request.POST['pweight']
    address=request.POST['paddress']
    email=request.POST['pemail']
    image=request.FILES['pimage']
    with open("health/static/images/patients/"+ image.name, "wb+") as des:
        for x in image.chunks():
            des.write(x)
    updatep=patients_register(Id=id,Name=name,Age=age,Contact=contact,Date_of_birth=dob,Gender=gender,Occupation=occupation,Height=height,Weight=weight,Address=address,Email=email,patient_Image=image)
    updatep.save()
    pdetails=patients_register.objects.get(Email=email)
    return render(request,"patient_home.html",{"pdetails":pdetails})


def ChangePasswordP(request):
    email=request.GET.get('id')
    pdetails=patients_register.objects.get(Email=email)
    return render(request,"patient_home.html",{"pdetails":pdetails,"type":'patient_change_password'})


def patient_change_password(request):
    p_password=request.POST['password1']
    p_email=request.POST['email']
    pdetails = patients_register.objects.get(Email=p_email)
    change_password=patients_register(Id=pdetails.Id,Email=p_email,Contact=pdetails.Contact,Age=pdetails.Age,Password=p_password,Date_of_birth=pdetails.Date_of_birth,Height=pdetails.Height,Weight=pdetails.Weight,Address=pdetails.Address,Occupation=pdetails.Occupation,Gender=pdetails.Gender)
    change_password.save()

    return render(request,"patient_home.html",{"pdetails":pdetails,"type":'patient_change_password',"message":'Password Changed Successfullly'})
