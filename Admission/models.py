from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from ApplicationForm.models import Application_Form_Model

class admission(models.Model):
    
    student         =  models.ForeignKey(
                         Application_Form_Model,
                         on_delete=CASCADE,
                         #verbose_name="Register Name",
                         primary_key=True,
                         default=None,
                        )   
    
    room_no         = models.CharField(max_length=5, unique=True)