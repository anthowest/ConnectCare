from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('patients/', views.Patient_List.as_view(), name="patient_list"),

]