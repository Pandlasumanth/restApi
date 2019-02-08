from django.core.mail import EmailMessage
from django.shortcuts import render
from  .models import diseases
from .models import nongenric_medicines,genric_medicines,patients_register,doctor,diseases,Chat,Feedback,PatientFeedback

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
            doctor.objects.filter(email=cp.email).update(doctor_status=1)
            return render(request, "doctor_home.html", {"ddetails": cp})
        else:
            return render(request, "index.html", {"type": "H_Doctor", "message1": "Invalid Details Please Register.."})
    except:
        return render(request, "index.html", {"type": "H_Doctor", "message1": "Invalid Details Please Register.."})
def patientregisterpage(request):
    type=request.GET.get("type")
    try:
        res=patients_register.objects.all()
        if res == None:
            id=1
            return render(request,"index.html",{"type":type,"id":id})
        else:
            for x in res:
                idno=int(x.Id)
                id=idno+1
            return render(request,"index.html",{"type":type,"id":id})
    except:
        id=1
        return render(request, "index.html", {"type": type, "id": id})


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


            request.session['pemail']=email
            patients_register.objects.filter(Email=email).update(patient_status=1)
            return render(request,"patient_home.html",{"pdetails":cp})
        else:
            return render(request,"index.html",{"type":"H_patient","message1":"Invalid Details Please Register.."})
    except:
        return render(request, "index.html", {"type": "H_patient", "message1": "Invalid Details Please Register.."})
# def diseaseslogin(request):
#     type=request.GET.get("type")
#     doctorinfo=doctor.objects.all()
#
#     return render(request,"index.html",{"type":type,'doctorsInfo':doctorinfo})
#
#
#
#     ngeneric=nongenric_medicines.objects.all()
#     if ngeneric.count()>0:
#         return render(request,"patient_home.html",{"ngeneric":ngeneric,"pdetails":pdetails})
#     else:
#         return render(request,"patient_home.html",{"pdetails":pdetails})
def PLogout(request):
    try:
        session=request.session['pemail']
        patients_register.objects.filter(Email=session).update(patient_status=0)
        request.session['pemail']=''
        doctorinfo=doctor.objects.all()
        return render(request,"index.html",{'doctorsInfo':doctorinfo})
    except:
        request.session['pemail'] = ''
        doctorinfo = doctor.objects.all()
        return render(request, "index.html", {'doctorsInfo': doctorinfo})
def DLogout(request):
    try:
        session=request.session['demail']
        dr=doctor.objects.get(email=session)
        doctor.objects.filter(email=session).update(doctor_status=0,doctor_image=dr.doctor_image)

        request.session['demail']=''
        doctorinfo=doctor.objects.all()
        return render(request,"index.html",{'doctorsInfo':doctorinfo})
    except:
        request.session['demail'] = ''
        doctorinfo = doctor.objects.all()
        return render(request, "index.html", {'doctorsInfo': doctorinfo})
def ViewMedicines(request):
    generic=genric_medicines.objects.all()
    print(generic)
    ngeneric=nongenric_medicines.objects.all()
    print(ngeneric)
    return render(request,"medicines.html",{"type":"medicines","generic":generic,"ngeneric":ngeneric})
def ViewDiseases(request):
    disease=diseases.objects.all()
    return render(request,"diseases.html",{"type":"diseases","diseases":disease})
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
        return render(request, "patient_home.html", {"type":"medicines","generic": generic, "ngeneric": ngeneric, 'pdetails': details})
    except:
        generic = genric_medicines.objects.all()
        ngeneric = nongenric_medicines.objects.all()
        return render(request, "medicines.html", {"type":"medicines","generic": generic, "ngeneric": ngeneric})
def ViewDiseasesp(request):
    try:
        email = request.GET.get('id')
        details = patients_register.objects.get(Email=email)
        disease=diseases.objects.all()
        return render(request,"patient_home.html",{"type":"diseases","pdetails":details,"diseases":disease})
    except:
        disease = diseases.objects.all()
        return render(request, "diseases.html", { "diseases": disease})
def ViewDoctorsp(request):
    email = request.GET.get('id')
    details = patients_register.objects.get(Email=email)
    doctors=doctor.objects.all()
    return render(request,"patient_home.html",{"type":"doctors","pdetails":details,"doctors":doctors})
def DoctorProfile(request):
    email = request.GET.get('id')
    profile = doctor.objects.get(email=email)
    return render(request, "doctor_home.html", {"type":"d_profile","profile": profile, "ddetails": profile})
def ViewMedicinesd(request):
    email = request.GET.get('id')
    details = doctor.objects.get(email=email)
    generic = genric_medicines.objects.all()
    ngeneric = nongenric_medicines.objects.all()
    return render(request, "doctor_home.html", {"type":"medicines","generic": generic, "ngeneric": ngeneric, 'ddetails': details})
def ViewDiseasesd(request):
    email = request.GET.get('id')
    details = doctor.objects.get(email=email)
    disease = diseases.objects.all()
    return render(request, "doctor_home.html", {"type":"diseases","ddetails": details, "diseases": disease})
def ViewPatients(request):
    email = request.GET.get('id')
    details = doctor.objects.get(email=email)
    patients = patients_register.objects.all()
    return render(request, "doctor_home.html", {"type":"patients","ddetails": details, "patients": patients})
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
        return render(request,"patient_home.html",{"dname":reciever,"pname":sender,'pdetails':pdetails,"demail":demail,"doctor":doctors,"sendmessage":'send','message':'request sent','chathistory':chathistory})
    except:
        return render(request,"patient_home.html",{"dname":reciever,"pname":sender,'pdetails':pdetails,"doctor":doctors,"demail":demail,"sendmessage":'send','message':'request sent'})
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
        return render(request,"doctor_home.html",{"type":"requests","ddetails":ddetails,'demails':dmsg,'requests':'requests'})
    except:
        return render(request,"doctor_home.html",{"type":"requests","ddetails":ddetails,'demails':'No Requests Are Found'})
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
                      {"dname": sender, "pname": reciever,"pemail":pemail,"demail":demail, 'ddetails': pdetails,
                       "sendresmessage": 'send', 'message': 'response sent', 'chathistory': chathistory})
    except:
        return render(request, "doctor_home.html",
                      {"dname": reciever, "pname": sender, 'pdetails': pdetails,
                       "sendresmessage": 'send',"pemail":pemail,"demail":demail, 'message': 'response sent'})
def UpdatePatientProfile(request):
    email=request.GET['email']
    pdetails=patients_register.objects.get(Email=email)
    return render(request,"patient_home.html",{"pdetails":pdetails,"type":'patientupdate'})
def UpdateDoctorProfile(request):
    email=request.GET['email']
    ddetails=doctor.objects.get(email=email)
    return render(request,"doctor_home.html",{"ddetails":ddetails,"profile":ddetails,"type":'doctorupdate'})
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
    try:

        image=request.FILES['pimage']

        with open("healthcareapp/static/images/patients/" + image.name, "wb+") as des:
            for x in image.chunks():
                des.write(x)
        patients_register.objects.filter(Email=email).update(patient_Image=image,Id=id, Name=name, Age=age, Contact=contact, Date_of_birth=dob, Gender=gender,Occupation=occupation, Height=height, Weight=weight, Address=address, Email=email)


        pdetails = patients_register.objects.get(Email=email)
        return render(request, "patient_home.html", {"type":"patientupdate","pdetails": pdetails,"message":"Updated Successfully "})
    except:
            patients_register.objects.filter(Email=email).update(Id=id, Name=name, Age=age,Contact=contact, Date_of_birth=dob, Gender=gender,Occupation=occupation, Height=height, Weight=weight,Address=address, Email=email)
            pdetails = patients_register.objects.get(Email=email)
            return render(request, "patient_home.html", {"type":"patientupdate","pdetails": pdetails,"message":"Updated Successfully "})
def UpdateProfileDoctorSave(request):
    id=request.POST['did']
    name=request.POST['dname']
    contact=request.POST['dcontact']

    email=request.POST['demail']
    designation=request.POST['ddesignation']
    try:

        image=request.FILES['dimage']

        with open("healthcareapp/static/images/doctor/" + image.name, "wb+") as des:
            for x in image.chunks():
                des.write(x)
        doctor.objects.filter(email=email).update(name=name,id=id,contact=contact,designation=designation,email=email,doctor_image=image)
        ddetails = doctor.objects.get(email=email)

        return render(request, "doctor_home.html", {"type":"doctorupdate","ddetails": ddetails,"profile":ddetails,"message":"updated successfully"})
    except:
        doctor.objects.filter(email=email).update(name=name,id=id,contact=contact,designation=designation,email=email)
        ddetails=doctor.objects.get(email=email)
        return render(request,"doctor_home.html",{"type":"doctorupdate","ddetails":ddetails,"profile":ddetails,"message":'updated details without image'})
def ChangePasswordP(request):
    email=request.GET.get('id')
    pdetails=patients_register.objects.get(Email=email)
    return render(request,"patient_home.html",{"pdetails":pdetails,"type":'patient_change_password'})
def ChangePasswordD(request):
    email=request.GET.get('id')
    pdetails=doctor.objects.get(email=email)
    return render(request,"doctor_home.html",{"ddetails":pdetails,"type":'doctor_change_password'})
def patient_change_password(request):
    p_password=request.POST['password1']
    p_email=request.POST['email']
    patients_register.objects.filter(Email=p_email).update(Password=p_password)
    pdetails = patients_register.objects.get(Email=p_email)

    return render(request,"patient_home.html",{"pdetails":pdetails,"type":'patient_change_password',"message":'Password Changed Successfullly'})
def doctor_change_password(request):
    d_password=request.POST['password1']
    d_email=request.POST['email']
    doctor.objects.filter(email=d_email).update(password=d_password)
    ddetails = doctor.objects.get(email=d_email)

    return render(request,"doctor_home.html",{"ddetails":ddetails,"type":'doctor_change_password',"message":'Password Changed Successfullly'})


def pforgotpassword(request):
    type=request.GET.get('type')
    return render(request,"index.html",{"type":type})


def SendPasswordP(request):
    email=request.POST['pemail']
    try:
        res=patients_register.objects.get(Email=email)
        if res:
            Message = 'Your Password Is'
            Subject = 'Forgot Password Details..'
            pemail=res.Email
            ppassword=res.Password

            from healthcare import settings as se
            sendemail=EmailMessage(Subject,Message+ppassword,se.EMAIL_HOST_USER,list(pemail,))
            sendemail.send(True)
            return render(request,"index.html",{"type":"H_Patient_Forgot","message":"Your Password Will Sent To Your Mail Please Check Your Mail.."})
        else:
            return render(request,"index.html",{"type":'H_Patient_Forgot',"message1":"Invalid Email Credentialnn"})
    except:
        return render(request, "index.html", {"type": 'H_Patient_Forgot', "message1": "Invalid Email Credential"})
def dforgotpassword(request):
    type=request.GET.get('type')
    return render(request,"index.html",{"type":type})


def SendPasswordD(request):
    email=request.POST['demail']
    try:
        res=doctor.objects.get(email=email)
        if res:
            Message = 'Your Password Is'
            Subject = 'Forgot Password Details..'
            demail=res.email
            dpassword=res.password

            from healthcare import settings as se
            sendemail=EmailMessage(Subject,Message+dpassword,se.EMAIL_HOST_USER,list(demail,))
            sendemail.send(True)
            return render(request,"index.html",{"type":"H_Doctor_Forgot","message":"Your Password Will Sent To Your Mail Please Check Your Mail.."})
        else:
            return render(request,"index.html",{"type":'H_Doctor_Forgot',"message1":"Invalid Email Credentialnn"})
    except:
        return render(request, "index.html", {"type": 'H_Doctor_Forgot', "message1": "Invalid Email Credential"})


def FeedBackFrom(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    Feedback(Name=name,Email=email,Message=message).save()
    return render(request,"index.html",{"fmessage":"Your Feedback is sended... "})
def PatientFeedBackFrom(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    PatientFeedback(Name=name,Email=email,Message=message).save()
    return render(request,"patient_home.html",{"fmessage":"Your Feedback is sended... "})
