from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('person/', views.person_details),
    path('person/parcel', views.parcel_details),

    
]
