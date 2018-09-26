from django import forms
from . import models
from django.contrib.admin import widgets

#form for creating new patient
class CreateNewPatient(forms.ModelForm):
    class Meta:
        model = models.PatientInfo
        fields = ['first_name', 'nickname','last_name',
            'date_of_birth', 'school_grade', 'sex', 'school']
        widgets = {
            'date_of_birth' : forms.DateInput(attrs={'class':'datepicker'}),
        }

#form for new patient checkin
class CheckinForm(forms.ModelForm):
    class Meta:
        model = models.CheckIn
        fields = ['height', 'weight', 'bmi', 'systolic', 'diastolic',
            'heart_rate', 'current_meds', 'past_history', 'current_complaints']

#form for existing patient checkin
class ExistingCheckinUpdate(forms.ModelForm):
    class Meta:
        model = models.PatientInfo
        fields = ['school_grade', 'school']

##form for doctor checkup_queue
class CheckUpForm(forms.ModelForm):
    class Meta:
        model = models.VisitInfo
        fields=['heent','neck_nodes','chest_heart','abdomen','exterior','spine',
            'skin','neuro','teeth','visit_notes','meds_perscribed','follow_up_required',]

#form for eye exam
class EyeForm(forms.ModelForm):
    class Meta:
        model= models.EyeCare
        fields=['od','os','near','pinhole','exam_notes','assessment','plan']

#form for checkout
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = models.Checkout
        fields = ['albendazol','fluoride_varnish','meds_administered','followup',]
