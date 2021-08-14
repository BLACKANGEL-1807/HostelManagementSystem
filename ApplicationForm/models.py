from django.db import models


# Create your models here.

class Application_Form_Model(models.Model):
    Name                    = models.CharField(max_length=60)
    Registration_Number     = models.IntegerField(unique=True, null=False, primary_key=True)
    Date_of_Birth           = models.DateField(auto_now=False, auto_now_add=False)
    Age                     = models.IntegerField()
    Gender                  = models.CharField(max_length=10)
    Blood_group             = models.CharField(max_length=10)
    Academic_year           = models.IntegerField(default="0000")
    Degree                  = models.CharField(max_length=5,default="B.E.")
    Course                  = models.CharField(max_length=100)
    Temporary_Address       = models.TextField()
    Permanent_Address       = models.TextField(default=Temporary_Address)
    Email_ID                = models.EmailField()
    Contact_Number          = models.IntegerField()
    Father_Name             = models.CharField(max_length=100)
    Father_occupation       = models.CharField(max_length=100, null=True)
    F_AnnualIncome          = models.DecimalField(max_digits=9999999, decimal_places=2, blank=True, null=True)
    Mother_Name             = models.CharField(max_length=100)
    Mother_occupation       = models.CharField(max_length=100, null=True)
    M_AnnualIncome          = models.DecimalField(max_digits=9999999, decimal_places=2, blank=True, null=True)
    Nationality             = models.CharField(max_length=100)
    Caste                   = models.CharField(max_length=100)
    Sub_caste               = models.CharField(max_length=100)
    
    def str(self):
        return self.Registration_Number
    