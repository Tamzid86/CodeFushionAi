from django.http import HttpResponse
from .fetchInfo import fetch_info  
from rest_framework import viewsets
from .models import AllData
from .serializers import AllDataSerializer
from django.db.models import Q 
from rest_framework.decorators import api_view

def fetch_countries(request):
    fetch_info()  
    return HttpResponse("Data has been fetched and stored successfully!")

class AllDataViewSet(viewsets.ModelViewSet):
    queryset= AllData.objects.all()
    serializer_class= AllDataSerializer

@api_view(['GET'])
def same_region_countries(request, country_name):
    try:
        country= AllData.objects.get(country_name__iexact=country_name)
        region=country.full_data.get('region')
        countries=AllData.objects.filter(full_data__region=region).exclude(id=country.id)
        serializer= AllDataSerializer(countries, many=True)
        return Response(serializer.data)
    except AllData.DoesNotExists:
        return Response({'error':'Country not found'}, status=404)

@api_view(['GET'])
def countries_by_language(request, language):
    countries = []
    for c in AllData.objects.all():
        languages= c.full_data.get('languages',{})
        if language.lower() in [v.lower() for v in languages.values()]:
            countries.append(c)
    serializer=AllDataSerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_country(request):
    query = request.GET.get('q', '')
    countries = AllData.objects.filter(country_name__icontains=query)
    serializer = AllDataSerializer(countries, many=True)
    return Response(serializer.data)