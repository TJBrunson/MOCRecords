from django.db import models

# Create your models here.
class PatientInfo(models.Model):
    #first name, last name, and date of birth
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)

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
