from django import forms
from . import models

class CreateNewPatient(forms.ModelForm):
    class Meta:
        model = models.PatientInfo
        fields = ['first_name', 'nickname','last_name',
            'date_of_birth', 'school_grade', 'sex', 'school']
