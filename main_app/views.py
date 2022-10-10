from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Provider

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Patient:
    def __init__(self, name, age, dob, diagnosis):
        self.name = name
        self.age = age
        self.dob = dob
        self.diagnosis = diagnosis


patients = [
    Patient("John Doe", 12, "11/02/2010", "ADHD"),
    Patient("Jane Doe", 28, "11/02/1993", "COVID")
]


class PatientList(TemplateView):
    template_name = "patient_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patients"] = patients
        return context


class ProviderList(TemplateView):
    template_name = "provider_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["providers"] = Provider.objects.all()
        return context