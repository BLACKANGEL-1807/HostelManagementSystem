from django import forms
from .models import admission

class admission_form(forms.Form):
    room_no     = forms.CharField(max_length=5)
    
class admission_form_Model(forms.ModelForm):
    class Meta:
        model = admission
        fields = [
            'student',
            #'room_no',
        ]