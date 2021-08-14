from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class user_accounts(models.Model):
    Registration_Number     = models.IntegerField(unique=True, null=False, primary_key=True)
    password                = models.CharField(max_length=20,blank=False, null=False)
    
    def __str__(self) -> str:
        return self.Registration_Number
    
