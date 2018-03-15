from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from . import forms
# Create your views here.
def IndexView(request):
    return render(request, 'patientRecords/index.html')

def NewPatientView(request):
    if request.method == 'POST':
        form = forms.CreateNewPatient(request.POST, request.FILES)
        if form.is_valid():
            #save created patient to datavase
            instance = form.save(commit=False)
            instance.save()
            return redirect('patientRecords:index')
    else:
        form = forms.CreateNewPatient()
    return render(request, 'patientRecords/new_patient.html', {'form':form})
