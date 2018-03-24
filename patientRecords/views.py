from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
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
    if request.method == 'POST':
        #form = forms.PatientCheckinForm(request.POST, request.FILES)
        #if form.is_valid():
            #instance = form.save(commit=False)
            return redirect('patientRecords/index.html')
    else:
        patient = get_object_or_404(PatientInfo, pk=patient_id)
        form = forms.PatientCheckinForm()
        return render(request, 'patientRecords/checkin.html', {'form':form, 'patient': patient})
