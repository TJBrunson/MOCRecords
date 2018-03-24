from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'patientRecords'
urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^new_patient/$', views.NewPatientView, name = "new_patient"),
    path('checkin/<int:patient_id>/', views.Checkin, name="checkin"),
]
