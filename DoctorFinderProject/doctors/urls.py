from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.doctor_list,
        name='doctor_list'
    ),

    path(
        'create-profile/',
        views.create_doctor_profile,
        name='doctor_profile'
    ),

    path(
        'dashboard/',
        views.doctor_dashboard,
        name='doctor_dashboard'
    ),

    path(
        '<int:pk>/',
        views.doctor_detail,
        name='doctor_detail'
    ),


    path(
    'availability/add/',
    views.add_availability,
    name='add_availability'
    ),


    path(
    'availability/',
    views.availability_list,
    name='availability_list'
    ),


    path(
    'availability/edit/<int:pk>/',
    views.edit_availability,
    name='edit_availability'
    ),

    path(
    'availability/delete/<int:pk>/',
    views.delete_availability,
    name='delete_availability'
    ),
    
]