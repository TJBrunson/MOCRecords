from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'patientRecords'
urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^new_patient/$', views.NewPatientView, name = "new_patient"),
    path('checkin/<int:patient_id>/', views.Checkin, name="checkin"),
    path('existing_checkin/<int:patient_id>/', views.ExistingCheckin, name="existing_checkin"),
    path('existing_checkin/existing_checkin_submit', views.ExistingCheckinSubmit, name="existing_checkin_submit"),
    path('checkin/checkinsubmit', views.CheckinSubmit, name="checkinsubmit"),
    path('patient_search', views.PatientSearch, name="patient_search"),
    path('checkup_queue', views.CheckupQueue, name='checkup_queue'),
    path('checkup/<int:id>/', views.PatientCheckupForm, name="checkup_form"),
    path('checkup/checkup_submit', views.PatientCheckupFormSubmit, name="checkup_submit"),
    path('eye_care_queue', views.EyeExamQueue, name='eye_care_queue'),
    path('eye_care_queue/<int:id>', views.EyeExamForm, name='eye_care_form'),
    path('checkup/eye_exam_submit', views.EyeExamFormSubmit, name="eye_exam_submit"),
]
