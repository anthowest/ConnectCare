from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('patients/', views.PatientList.as_view(), name="patient_list"),
    path('patients/new/', views.PatientCreate.as_view(), name="patient_create"),
    path('patients/<int:pk>/', views.PatientDetail.as_view(), name="patient_detail"),
    path('patients/<int:pk>/update', views.PatientUpdate.as_view(), name="patient_update"),
    path('patients/<int:pk>/delete', views.PatientDetele.as_view(), name="patient_delete"),
    path('providers/', views.ProviderList.as_view(), name="provider_list"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]