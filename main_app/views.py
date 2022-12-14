from pipes import Template
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Patient, Record, Provider
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


class ProviderList(TemplateView):
    template_name = "provider_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["providers"] = Provider.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["providers"] = Provider.objects.all()
            context["header"] = f"Searching for {name}"
        return context

# Provider Create - make sure to add self.request.user.pk after form is valid

@method_decorator(login_required, name='dispatch')
class PatientCreate(CreateView):
    model = Patient
    fields = ['name', 'dob', 'diagnosis']
    template_name = "patient_create.html"

    def form_valid(self, form):
        provider = Provider.objects.get(user_id=self.request.user.pk)
        print(provider)
        form.instance.provider = provider
        return super(PatientCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProviderCreate(CreateView):
    model = Provider
    fields = ['name', 'speciality', 'phone_number', 'email', 'bio']
    template_name = "provider_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProviderCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('provider_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class PatientUpdate(UpdateView):
    model = Patient
    fields = ['name', 'dob', 'diagnosis', 'active','address', 'phone_number']
    template_name = "patient_update.html"
    
    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class PatientDetail(DetailView):
    model = Patient
    template_name = "patient_detail.html"


class ProviderDetail(DetailView):
    model = Provider
    template_name = "provider_detail.html"


# class ProviderDashboard(TemplateView):
#     model = Provider
#     template_name = "dashboard.html"


@method_decorator(login_required, name='dispatch')
class PatientDelete(DeleteView):
    model = Patient
    template_name = "patient_delete_confirmation.html"
    success_url = "/patients/"


@method_decorator(login_required, name='dispatch')
class RecordCreate(View):

    def post(self, request, pk):
        visit_reason = request.POST.get("visit_reason")
        vital_signs = request.POST.get("vital_signs")
        treatment = request.POST.get("treatment")
        patient = Patient.objects.get(pk=pk)
        Record.objects.create(visit_reason=visit_reason, vital_signs=vital_signs, treatment=treatment, patient=patient)
        return redirect('patient_detail', pk=pk)


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
            return redirect("provider_create")
            # provider_create
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
