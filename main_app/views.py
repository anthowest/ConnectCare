from pipes import Template
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Provider, Patient
from django.contrib.auth import login
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"
    

@method_decorator(login_required, name='dispatch')
class PatientList(TemplateView):
    template_name = "patient_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["patients"] = Patient.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["patients"] = Patient.objects.all()
            context["header"] = f"Searching for {name}"
        return context


class PatientCreate(CreateView):
    model = Patient
    fields = ['name', 'dob', 'diagnosis']
    template_name = "patient_create.html"

    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.pk})


class PatientUpdate(UpdateView):
    model = Patient
    fields = ['name', 'dob', 'diagnosis']
    template_name = "patient_update.html"
    
    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.pk})


class PatientDetail(DetailView):
    model = Patient
    template_name = "patient_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class PatientDelete(DeleteView):
    model = Patient
    template_name = "patient_delete_confirmation.html"
    success_url = "/patients/"


class ProviderList(TemplateView):
    template_name = "provider_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["providers"] = Provider.objects.all()
        return context

    
# class PatientRecord(TemplateView):
#     template_name = "patient_record.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["records"] = Record.objects.all()


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("patient_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
