from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('patients/', views.PatientList.as_view(), name="patient_list"),
    path('providers/', views.ProviderList.as_view(), name="provider_list"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]