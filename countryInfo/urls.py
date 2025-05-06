from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllDataViewSet 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupPageView,LoginPageView,country_list_view

router= DefaultRouter()
router.register(r'countries', AllDataViewSet)

urlpatterns= [
    path('api/auth/', include('dj_rest_auth.urls')),  # Handles login and logout
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  
 

    path('api/',include(router.urls)),
    path('fetch-countries/', views.fetch_countries, name='fetch_countries'),
    path('same-region/<str:country_name>/', views.same_region_countries),
    path('by-language/<str:language>/', views.countries_by_language),
    path('search/', views.search_country),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('login/',LoginPageView.as_view(), name='login-page'),
    path('signup/', SignupPageView.as_view(), name='signup-page'), 
    path('api/auth/signup/', views.SignupView.as_view(), name='signup'),
    path('countries', country_list_view, name='country-list')
]

urlpatterns += router.urls