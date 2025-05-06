from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllDataViewSet 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router= DefaultRouter()
router.register(r'countries', AllDataViewSet)

urlpatterns= [
    path('api/auth/', include('dj_rest_auth.urls')),  # Handles login and logout
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Handles signup
 

    path('api/',include(router.urls)),
    path('fetch-countries/', views.fetch_countries, name='fetch_countries'),
    path('same-region/<str:country_name>/', views.same_region_countries),
    path('by-language/<str:language>/', views.countries_by_language),
    path('search/', views.search_country),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    

]

urlpatterns += router.urls