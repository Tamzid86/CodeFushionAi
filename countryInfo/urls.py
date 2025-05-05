from django.urls import path 
from . import views

urlpatterns= [
    path('fetch-countries/', views.fetch_countries, name='fetch_countries'),
]