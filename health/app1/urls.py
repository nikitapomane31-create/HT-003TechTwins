from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medi/', views.medi, name='medi'),

    path('em/', views.em, name='em'),
    
    path('symptom_checker/', views.symptom_checker, name='symptom_checker'),
    path('symptom_result/', views.symptom_result, name='symptom_result'),


    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('medicine_list/', views.medicine_list, name='medicine_list'),

    path('reminder/', views.reminder, name='reminder'),
    path('delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('edit/<int:pk>/', views.edit_medicine, name='edit_medicine'),



    

    path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('medicine-list/', views.medicine_list, name='medicine_list'),
    path('edit-medicine/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('delete-medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),

]
