from django.http import HttpResponse
from .fetchInfo import fetch_info  
from rest_framework import viewsets
from .models import AllData
from .serializers import AllDataSerializer
from django.db.models import Q 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt



def fetch_countries(request):
    fetch_info()  
    return HttpResponse("Data has been fetched and stored successfully!")

class AllDataViewSet(viewsets.ModelViewSet):
    queryset= AllData.objects.all()
    serializer_class= AllDataSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def same_region_countries(request, country_name):
    try:
        country= AllData.objects.get(country_name__iexact=country_name)
        region=country.full_data.get('region')
        countries=AllData.objects.filter(full_data__region=region).exclude(id=country.id)
        serializer= AllDataSerializer(countries, many=True)
        return Response(serializer.data)
    except AllData.DoesNotExist:
        return Response({'error':'Country not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def countries_by_language(request, language):
    countries = []
    for c in AllData.objects.all():
        languages= c.full_data.get('languages',{})
        if language.lower() in [v.lower() for v in languages.values()]:
            countries.append(c)
    serializer=AllDataSerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_country(request):
    query = request.GET.get('q', '')
    countries = AllData.objects.filter(country_name__icontains=query)
    serializer = AllDataSerializer(countries, many=True)
    return Response(serializer.data)


