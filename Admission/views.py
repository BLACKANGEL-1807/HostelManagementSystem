from django.shortcuts import render

from .models import admission
from ApplicationForm.models import Application_Form_Model
# Create your views here.
from .forms import admission_form, admission_form_Model


def admission_view(request):
    ad_form         = admission_form()
    if request.method =="POST":
        print(" admission POST method Form")
        ad_form     = admission_form(request.POST)
        #model_ad_form   = admission_form_Model(request.POST)
        if ad_form.is_valid():
            print("admission FORM INCOMING")
            print("Username")
            print(request.user)
            print("All Objects")
            r = request.POST["Register Name"]
            roomnumber = request.POST["room_no"]
            admission.objects.create(student_id=r, room_no=roomnumber)
            ad_form         = admission_form()
        else:
            print(" admission FORM ERROR")
            ad_form.errors
    
    context = {
        'form': ad_form,
    }
    return render(request, "room.html", context)
