from django.urls import path, re_path

from . import views

app_name = 'patientRecords'
urlpatterns = [
    path('', views.IndexView),
    path('patientRecords/', views.NewPatientView),
]
