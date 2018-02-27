from django.urls import path

from . import views

app_name = 'patientRecords'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('/new_patient', views.NewPatientView, name='new_patient'),
]
