from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medi/', views.medi, name='medi'),
    path('symptom_checker/', views.symptom_checker, name='symptom_checker'),
    path('symptom_result/', views.symptom_result, name='symptom_result'),

     path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('medicine-list/', views.medicine_list, name='medicine_list'),
    path('edit-medicine/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('delete-medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),
]
