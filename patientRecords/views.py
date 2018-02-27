from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
# Create your views here.
def IndexView(request):
    return render(request, 'patientRecords/index.html')

def NewPatientView(request):
    return render(request, 'patientRecords/new_patient.html')
