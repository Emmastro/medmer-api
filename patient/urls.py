from django.urls import path 
#from django.views.generic import 
from patient import views

urlpatterns = [


path('', views.PatientRegistration.as_view(), name='patient_registration'),
 ]