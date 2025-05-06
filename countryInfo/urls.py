from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllDataViewSet 
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router= DefaultRouter()
router.register(r'countries', AllDataViewSet)

urlpatterns= [
    path('api/',include(router.urls)),
    path('fetch-countries/', views.fetch_countries, name='fetch_countries'),
    path('same-region/<str:country_name>/', views.same_region_countries),
    path('by-language/<str:language>/', views.countries_by_language),
    path('search/', views.search_country),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', views.register_user),
]