import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class PatientInfo(models.Model):
    #first name, last name,nickname, and date of birth
    first_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    school_grade = models.CharField(max_length=15, blank=True)

    #choice for sex
    MALE = 'Male'
    FEMALE = 'Female'
    NEITHER = 'Neither'
    SEX_CHOICES =(
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NEITHER,'Neither'),
    )
    sex = models.CharField(max_length=7, choices=SEX_CHOICES, default=NEITHER)

    #choice for school
    SANTA_MARIA = 'Santa Maria'
    SAN_JOSE = 'San Jose'
    PREPA = 'Prepa'
    NONE = 'None'
    SCHOOL_CHOICES=(
        (SANTA_MARIA, 'Santa Maria'),
        (SAN_JOSE, 'San Jose'),
        (PREPA, 'Prepa'),
        (NONE, 'None')
    )
    school = models.CharField(max_length=20, choices=SCHOOL_CHOICES, default=NONE)

    def __str__(self):
        return self.first_name

#class for checkin information
class CheckIn(models.Model):
    patient_id = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    checkin_complete = models.BooleanField(default=False)
    height = models.IntegerField()
    weight = models.IntegerField()
    bmi = models.IntegerField()
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    heart_rate = models.IntegerField()
    current_meds = models.CharField(max_length=250, default="None")
    past_history = models.CharField(max_length=250, default="None")
    current_complaints = models.CharField(max_length=250, default="None")

#class for doctor visit
class VisitInfo(models.Model):
    #Choice setup
    NORMAL = 'Normal'
    ABNORMAL = 'Abnormal'
    normal_abnormal_choice = (
        (NORMAL,'Normal'),
        (ABNORMAL, 'Abnormal'),
    )

    #yes/no choice setup
    YES = 'Yes'
    NO = 'No'
    yes_no_choice = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    #db table fields
    patient = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    checkup_complete = models.BooleanField(default=False)
    heent = models.CharField(max_length=8, choices=normal_abnormal_choice)
    neck_nodes = models.CharField(max_length=8, choices=normal_abnormal_choice)
    chest_heart = models.CharField(max_length=8, choices=normal_abnormal_choice)
    abdomen = models.CharField(max_length=8, choices=normal_abnormal_choice)
    exterior = models.CharField(max_length=8, choices=normal_abnormal_choice)
    spine = models.CharField(max_length=8, choices=normal_abnormal_choice)
    skin = models.CharField(max_length=8, choices=normal_abnormal_choice)
    neuro = models.CharField(max_length=8, choices=normal_abnormal_choice)
    teeth = models.CharField(max_length=8, choices=normal_abnormal_choice)
    visit_notes = models.CharField(max_length=500)
    meds_perscribed = models.CharField(max_length=100, blank=True, default="None")
    follow_up_required = models.CharField(max_length=3, choices=yes_no_choice, default='No')

#class for Eyes
class EyeCare(models.Model):
    patient = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    date_time_of_eye_exam = models.DateTimeField('Time of Eye Exam')
    od = models.IntegerField(blank=True)
    os = models.IntegerField(blank=True)
    near = models.CharField(max_length=100, blank=True)
    pinhole = models.CharField(max_length=100, blank=True)
    exam_notes = models.CharField(max_length=250, blank=True)
    assessment = models.CharField(max_length=250, blank=True)
    plan = models.CharField(max_length=250, blank=True)

#class for Checkout
class Checkout(models.Model):
    #choice setup
    YES = 'Yes'
    NO = 'No'
    yes_no_choice = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    #db table fields
    patient = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    date_time_of_checkout = models.DateTimeField('Time of checkout')
    albendazol = models.CharField(max_length=3, choices=yes_no_choice, default='No')
    fluoride_varnish = models.CharField(max_length=3, choices=yes_no_choice, default='No')
    meds_administered = models.CharField(max_length=100, default='N/A')
    followup = models.CharField(max_length=100, default='N/A')
