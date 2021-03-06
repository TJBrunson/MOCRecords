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

#view for checkup Queue
def CheckupQueue(request):
    pk_list = CheckIn.objects.filter(checkin_complete=False).values_list('patient_id')
    patient_list = PatientInfo.objects.filter(pk__in=pk_list)
    return render(request, 'patientRecords/checkup_queue.html', {'patient_list': patient_list
    })

#view for checkup form
def PatientCheckupForm(request, id):
    patient = get_object_or_404(PatientInfo, pk=id)
    checkin_info = get_object_or_404(CheckIn, patient_id=id, checkin_complete=False)
    form = forms.CheckUpForm()
    return render(request, 'patientRecords/checkup_form.html', {'patient':patient,
        'checkin_info':checkin_info, 'form':form})

#view for submitting checkup to db
def PatientCheckupFormSubmit(request):
    if request.method == 'POST':
        instance = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
        form = forms.CheckUpForm(request.POST or None)
        if form.is_valid():
            CheckIn.objects.filter(patient_id=request.POST.get('patient_id')).update(checkin_complete=True)
            checkupForm = form.save(commit=False)
            checkupForm.patient = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
            checkupForm.check_in = CheckIn.objects.get(pk=request.POST.get('checkin_id'))
            checkupForm.save()
            return render(request, 'patientRecords/index.html')

#view for eye exam queue
def EyeExamQueue(request):
        pk_list = VisitInfo.objects.filter(checkup_complete=False).values_list('patient_id')
        patient_list = PatientInfo.objects.filter(pk__in=pk_list)
        return render(request, 'patientRecords/eye_care_queue.html', {'patient_list': patient_list
        })

#view for eye exam form
def EyeExamForm(request, id):
    patient = get_object_or_404(PatientInfo, pk=id)
    checkup_info = get_object_or_404(VisitInfo, patient_id=id, checkup_complete=False)
    form = forms.EyeForm()
    return render(request, 'patientRecords/eye_care_form.html', {'patient': patient, 'form': form, 'checkup_info':checkup_info})

#view for eye exam submit
def EyeExamFormSubmit(request):
    if request.method == 'POST':
        instance = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
        form = forms.EyeForm(request.POST or None)
        if form.is_valid():
            visit = VisitInfo.objects.get(pk=request.POST.get('checkup_id'))
            VisitInfo.objects.filter(patient_id=request.POST.get('patient_id')).update(checkup_complete=True)
            formSubmit = form.save(commit=False)
            formSubmit.patient = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
            formSubmit.check_in = CheckIn.objects.get(pk=visit.check_in.id)
            formSubmit.save()
            return render(request, 'patientRecords/index.html')

#view for checkout queue
def CheckoutQueue(request):
    pk_list = EyeCare.objects.filter(checkout_complete=False).values_list('patient_id')
    patient_list = PatientInfo.objects.filter(pk__in=pk_list)
    return render(request, 'patientRecords/checkout_queue.html', {'patient_list':patient_list})

#view for checkout form
def checkoutForm(request, id):
    patient = get_object_or_404(PatientInfo, pk=id)
    eye_care = get_object_or_404(EyeCare, patient=id, checkout_complete=False)
    form = forms.CheckoutForm()
    return render(request, 'patientRecords/checkout_form.html', {'patient':patient, 'form':form, 'eye_care':eye_care})

#view for checkout submit
def CheckoutSubmit(request):
    if request.method == 'POST':
        instance = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
        form = forms.CheckoutForm(request.POST or None)
        if form.is_valid():
            eye_care = EyeCare.objects.get(pk=request.POST.get('eye_care_id'))
            EyeCare.objects.filter(patient_id=request.POST.get('patient_id')).update(checkout_complete=True)
            formSubmit = form.save(commit=False)
            formSubmit.patient = PatientInfo.objects.get(pk=request.POST.get('patient_id'))
            formSubmit.check_in = CheckIn.objects.get(pk=eye_care.check_in.id)
            formSubmit.save()
            return render(request, 'patientRecords/index.html')
