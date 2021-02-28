from django.urls import path 
from . import views

urlpatterns = [
    path('Agirculture/', views.agriculture, name = 'agriculture'),
    path('architecture/', views.architecture, name = 'architecture'),
    path('technology/', views.technology, name = 'technology'),
    path('sales/', views.sales, name = 'sales'),
    path('business/', views.business, name = 'business'),
    path('education/', views.Education, name = 'education'),
    path('health/', views.Health, name = 'health'),
    path('law/', views.Law, name = 'law'),
    path('transportation/', views.transportation, name = 'transportation'),
    path('it/', views.It, name = 'it'),

    
]