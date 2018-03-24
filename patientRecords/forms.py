from django import forms
from . import models
from django.contrib.admin import widgets

#form for creating new patient
class CreateNewPatient(forms.ModelForm):
    class Meta:
        model = models.PatientInfo
        fields = ['first_name', 'nickname','last_name',
            'date_of_birth', 'school_grade', 'sex', 'school']

#form for CheckIn
class PatientCheckinForm(forms.ModelForm):
    class Meta:
        model = models.CheckIn
        fields = ['height', 'weight', 'bmi', 'systolic', 'diastolic',
            'heart_rate', 'current_meds', 'past_history', 'current_complaints']
