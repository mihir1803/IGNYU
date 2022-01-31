from django.shortcuts import render,redirect
from django.http import HttpResponse


# register
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ImageUpload 


# login
from django.contrib.auth import authenticate , login , logout

def index(request):
    # return HttpResponse("hello world !"),
    # return HttpResponse("<em>My Seconde App</em>")
    my_dict = {'insert_me':"I am Views.html" }
    return render(request,'index.html' ,context=my_dict)

def Image(request):
    
    if request.method == "POST":
        text1=request.POST.get('text1')
        attachment = request.FILES.get('attachment')
        image = ImageUpload(Disc=text1,attechment=attachment,Student_name=request.user)
        
        image.save()
        # messages.success(request, 'Registered Successful' )
        return redirect('index')
    else:
        # images = ImageUpload.objects.all()
        # images = Show_Image.objects.all()
        return render(request,'image/image.html')
        # return render(request, 'Admin/Image/Image.html',{'images':images})

def Voice(request):
    return render(request,'voice/voice.html')

def Registar_user(request):
    if request.method == "POST":
        username=request.POST['username']
        fname=request.POST['fname']    
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        psw=request.POST['psw']
        psw1=request.POST['psw1']
        
        
        if psw != psw1:
            messages.error(request,"Password to be not match")
            return redirect('registar')
        
        
        myuser = User.objects.create_user(username,email,psw)
        myuser.first_name=fname
        myuser.last_name = lname
        myuser.save()

        return redirect('index')
    else:
        return render(request, 'registar/registar.html')

def Login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        
        user = authenticate(username = uname, password = pass1)
        
        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            messages.error(request,"user authenticate nathi thyo")
            return redirect('login')
    return render(request, 'login/login.html')

def Logout(request):
    # if request.method == "POST":
        logout(request)
        # messages.error(request,"logout")
        return redirect('index')
def WhatsApp(request):
    return render(request,'whatsapp/whatsapp.html')

def Show_Ans(request):
    return render(request,'answer/answer.html')

# Create your views here.
