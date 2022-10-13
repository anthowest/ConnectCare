from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('patients/', views.PatientList.as_view(), name="patient_list"),
    path('patients/new/', views.PatientCreate.as_view(), name="patient_create"),
    path('patients/<int:pk>/', views.PatientDetail.as_view(), name="patient_detail"),
    path('patients/<int:pk>/update', views.PatientUpdate.as_view(), name="patient_update"),
    path('patients/<int:pk>/delete', views.PatientDelete.as_view(), name="patient_delete"),
    path('patients/<int:pk>/records/new/', views.RecordCreate.as_view(), name="record_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
    # path('messages/<int:pk>/')
]