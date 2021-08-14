from django.shortcuts import render


from .forms import  PureApplicationForm

from .models import Application_Form_Model
# Create your views here.


def Application_create_View(request):
    my_form = PureApplicationForm()
    
    if request.method=="POST":
        #print("FORM INCOMING")
        my_form = PureApplicationForm(request.POST)
        
        if my_form.is_valid(): 
            #print("FORM LOOKS GOOD ")
            #CHECKING WETHER DATA IS GOOD
            Application_Form_Model.objects.create(**my_form.cleaned_data)
            my_form = PureApplicationForm()
    else:
        #print("FORM ERROR")
        my_form.errors
            
    context = {
           'form' : my_form,
    }
    #return render(request, "create.html", context)
    return render(request, "room.html", context)
