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
        patient = get_object_or_404(PatientInfo, pk=patient_id)
        form = forms.CheckinForm()
        return render(request, 'patientRecords/checkin.html', {'patient': patient, 'form':form})

#view for submitting Checkin
def CheckinSubmit(request):
    if request.method == 'POST':
        form = forms.CheckinForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.checkin_complete = False
            instance.patient_id = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
            instance.save()
            return redirect('patientRecords:index')

#display list of patients already created for checkin
def PatientSearch(request):
    patient_list = PatientInfo.objects.order_by('first_name', 'last_name')
    return render(request, 'patientRecords/patient_search.html', {'patient_list': patient_list })

#display for existing patient CheckIn
def ExistingCheckin(request, patient_id):
    patient = get_object_or_404(PatientInfo, pk=patient_id)
    updateForm = forms.ExistingCheckinUpdate()
    form = forms.CheckinForm()
    return render(request, 'patientRecords/existing_checkin.html', {'patient':patient,
        'updateForm':updateForm, 'form':form })

#view for submitting checking when patient already exists
def ExistingCheckinSubmit(request):
    if request.method == 'POST':
        instance = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
        update = forms.ExistingCheckinUpdate(request.POST or None, instance=instance)
        checkin = forms.CheckinForm(request.POST or None)
        if update.is_valid() and checkin.is_valid():
            checkinForm = checkin.save(commit=False)
            checkinForm.checkin_complete = False
            checkinForm.patient_id = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
            update.save()
            checkinForm.save()
            return redirect('patientRecords:index')

#view for checkin Queue
def CheckupQueue(request):
    pk_list = CheckIn.objects.filter(checkin_complete=False).values_list('patient_id')
    patient_list = PatientInfo.objects.filter(pk__in=pk_list)
    return render(request, 'patientRecords/checkup_queue.html', {'patient_list': patient_list,  'pk_list':pk_list})
