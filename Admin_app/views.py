from ast import For
from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.views import Image
from .models import Show_Image
from first_app.models import ImageUpload

# Create your views here.
def Image_Show(request):
    if request.method == "POST" :
        Sname = request.POST.get('stud_name')
        Sdisc = request.POST.get('img_disc')
        Simage = request.FILES.get('image_attechment')
        Sans = request.POST.get('answer')

        print(Sname)
        print(Sdisc)
        print(Simage)
        print(Sans)
        
        return HttpResponse(" thank you")
        ImageShow = Show_Image(Student_Name=Sname,Student_Disc=Sdisc,Attechment=Simage,Answer=Sans)
        # ImageShow.save()
    else:    
        images = ImageUpload.objects.all()
        for count,i in enumerate(images):
            print(count , '  |  ', i.Student_name, '  |  ', i.Disc, '  |  ', i.attechment)
            print("\n\n")
        return render(request, 'Admin/Image/Image.html',{'images':images})

    