from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from .forms import user_login_form
# Create your views here.
# Create your views here.


def  user_create(request):
    create_user_info = user_login_form()
    #username = " "
    
    if request.method == "POST":
        create_user_info = user_login_form(request.POST)
        #creating user details
        
        username    = request.POST['Username']
        password    = request.POST['Password']
        email       = request.POST['Email_ID']
        firstname   = request.POST['FirstName']
        lastname    = request.POST['LastName']        
        if create_user_info.is_valid():
            create = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name = lastname)
            create.save()
            print("User Created")
        else:
            create_user_info.errors
    
      
    context = {
        'reg_form': create_user_info,
    }
    return render(request, "accountRegistration.html", context)


def user_auth(request):
    LoginINFO = user_login_form()
    username ="XXX"
    
    if request.method == "POST":
        LoginINFO = user_login_form(request.POST)
        print("FORM INCOMING")
        
        # if LoginINFO.is_valid():
        #     print("FORM ACCEPTED")
        #     username = LoginINFO.cleaned_data.get('username')  ##FOR TESTING PURPOSE
        #     print(username)
        #     password = LoginINFO.cleaned_data.get('Password')
        #     print(password)
        # else:
        #     print("FORM NOT READ")
        #     LoginINFO.errors
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #print("LOGIN SUCCESSFUL")
            login(request, user)
            context = {
                     'form' : LoginINFO,
                         }
            return render(request, 'Application_Form.html', context)
        else:
            print("LOGIN UNSUCCESSFULL")
            return render(request, "registration.html", {'message':"Incorrect Userid orpassword "})
        # Return an 'invalid login' error message.
    
    
    
def logout_view(request):
    logout(request)
    return render(request, "logout.html")

   