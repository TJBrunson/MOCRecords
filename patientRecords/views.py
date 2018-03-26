from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import datetime as dt
from .models import *
from . import forms

# Create your views here.
#view for index page
def IndexView(request):
    return render(request, 'patientRecords/index.html')

#view for patient creation
def NewPatientView(request):
    if request.method == 'POST':
        form = forms.CreateNewPatient(request.POST, request.FILES)
        if form.is_valid():
            #save created patient to datavase
            instance = form.save(commit=False)
            instance.save()
            return redirect('patientRecords:checkin', instance.pk)
    else:
        form = forms.CreateNewPatient()
        return render(request, 'patientRecords/new_patient.html', {'form':form})

#view for Checkin
def Checkin(request, patient_id):
        patient = get_object_or_404(PatientInfo, pk=patient_id)
        form = forms.PatientCheckinForm()
        return render(request, 'patientRecords/checkin.html', {'patient': patient, 'form':form})

def CheckinSubmit(request):
    if request.method == 'POST':
        form = forms.PatientCheckinForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date_time_of_checkin = dt.now()
            instance.patient_id = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
            instance.save()
            return redirect('patientRecords:index')
