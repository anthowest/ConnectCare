from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app_urls')),
    path('patients/', views.Patient_List.as_view(), name="patient_list"),
    path('', views.Home.as_view(), name="home"),
]