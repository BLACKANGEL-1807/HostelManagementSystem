from django import forms



from .models import Application_Form_Model


class ApplicationModelForm(forms.ModelForm):
    class Meta:
        model = Application_Form_Model
        fields = [
            'Name',
            'Registration_Number',
            'Date_of_Birth',
        ]
    

class PureApplicationForm(forms.Form):
    Name                    = forms.CharField(label="Name",max_length=60, required=True)
    Registration_Number     = forms.IntegerField(label="Registration Number",)
    Date_of_Birth           = forms.DateField(label="Date Of Birth",)
    Age                     = forms.IntegerField(label="Age",)
    Gender                  = forms.CharField(label="Gender",max_length=10)
    Blood_group             = forms.CharField(label="Blood Group",max_length=10)
    Academic_year           = forms.IntegerField(label="Academic Year",)
    Degree                  = forms.CharField(label="Degree",initial="B.E.",max_length=5)
    Course                  = forms.CharField(label="Course",max_length=100)
    Temporary_Address       = forms.CharField(label="Temporary Address",widget=forms.Textarea(attrs={'rows':5}))
    Permanent_Address       = forms.CharField(label="Permanent Address",widget=forms.Textarea(attrs={'rows':5}))
    Email_ID                = forms.EmailField(label="EmailID",)
    Contact_Number          = forms.IntegerField(label="Contact Nuumber",)
    Father_Name             = forms.CharField(label="Father's Name",max_length=100)
    Father_occupation       = forms.CharField(label="Father's Occupation",max_length=100,required=False)
    F_AnnualIncome          = forms.DecimalField(label="Father's AnnualIncome",max_digits=9999999, decimal_places=2,required=False)
    Mother_Name             = forms.CharField(label="Mother's Name",max_length=100)
    Mother_occupation       = forms.CharField(label="Mother's Occupation",max_length=100,required=False)
    M_AnnualIncome          = forms.DecimalField(label="Mother's AnuualIncome",max_digits=9999999, decimal_places=2, required=False)
    Nationality             = forms.CharField(label="Nationality",max_length=100)
    Caste                   = forms.CharField(label="Caste",max_length=100)
    Sub_caste               = forms.CharField(label="Sub-Caste",max_length=100)