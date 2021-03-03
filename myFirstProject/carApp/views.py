from django.shortcuts import render
from carApp.models import User,Contact,BoldLinks
from . import forms
# Create your views here.

def index(request):
    return render(request,'carApp/index.html')

def cars(request):
    return render(request,'carApp/cars.html')

def service(request):
    user_details = User.objects.all()
    context = {'users': user_details }
    return render(request,'carApp/service.html',context)

def blog(request):
    return render(request,'carApp/blog.html')

def contact(request): 
    saveFlag = False
    newform = forms.ContactForm()
    if request.method == "POST":
        #print(request.POST)
        newform = forms.ContactForm(request.POST)
        # name = mail = mess = ""
            # if request.POST['fullname'] != "" and request.POST['email'] != "" and request.POST['message']:
        if newform.is_valid():
            # name      = request.POST['fullname']
            # mail      = request.POST.get("email")
            # mess      = request.POST['message']

            # newform = Contact(fullname=name,email=mail,message=mess)
            newform.save()
            saveFlag = True

        if saveFlag:
            message = {
                        "response":"Thank you for contacting us, We will revert back shortly",
                        "fullname":request.POST["fullname"]
                      }
        else:
            message = {
                       'form':newform
                      }
    else:
        message = {'form':newform}

    return render(request,'carApp/contact.html',context=message)


def about(request):
    return render(request,'carApp/about.html')

def students(request):
    saveFlag = False
    stdform = forms.StudentForm()
    if request.method == "POST":
        stdform = forms.StudentForm(request.POST)
        name = mail = phone = address = state = crs = enr = grad = ""
        if stdform.is_valid():
            name      = request.POST['student']
            mail      = request.POST['email']
            phone     = request.POST['phone']
            address   = request.POST['address']
            state     = request.POST['state']
            crs       = request.POST['course']
            enr       = request.POST['enrollment_date']
            grad      = request.POST['graduation_date']

            stdform = BoldLinks(StudentName=name,
                            StudentEmail=mail,
                            Phonenumber=phone,
                            Address=address,
                            State=state,
                            Course=crs,
                            Date_Enrolled=enr,
                            Graduation_Date=grad
                            )
            stdform.save()
            saveFlag = True

        if saveFlag:
            message = {
                        "reply":"Thank you for registering, We will revert back shortly",
                        "student": name
                      }
        else:
            message = {
                       'regs':stdform
                      }
    else:
        message = {'regs':stdform}

    return render(request,'carApp/regform.html',context=message)


