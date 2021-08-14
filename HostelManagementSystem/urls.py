"""HostelManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from ApplicationForm import views as AF_views
from Useraccounts import views as user_views

#temporary Testing
from Admission import views as ad_views


urlpatterns = [
    
    # User Login and Regsitration Behaviour
    path('',TemplateView.as_view(template_name = 'registration.html'), name="Reg"),
    path('login/', user_views.user_auth, name="Login"),
    path('user_create/', user_views.user_create , name="user"),
    path('logout/', user_views.logout_view, name="Logout"),
    
    # Student Application-Form
    path('create/', AF_views.Application_create_View, name="Create"),
    path('form/',TemplateView.as_view(template_name = 'Application_Form.html')),
    
    #admin-site
    path('admin/', admin.site.urls),
    
    #temporary_Testing
    path('room/', ad_views.admission_view, name="Room"),
]
