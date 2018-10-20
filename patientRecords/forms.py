from django import forms
from django.forms import ModelForm, Textarea
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
        fields = ['height', 'current_date', 'weight', 'bmi', 'systolic', 'diastolic',
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
        fields=['heent','neck_nodes','chest_heart','abdomen','extremities','spine',
            'skin','neuro','teeth','assessment','meds_perscribed','follow_up_required',]

#form for eye exam
class EyeForm(forms.ModelForm):
    class Meta:
        model= models.EyeCare
        fields=['od','os','near_left','near_right','exam_notes','assessment','plan']
        widgets={'assessment' : Textarea(attrs={'rows':5}),
                'exam_notes' : Textarea(attrs={'rows':5}),
                'plan' : Textarea(attrs={'rows':5})
                }

#form for checkout
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = models.Checkout
        fields = ['albendazole','fluoride_varnish','meds_administered','followup',]
