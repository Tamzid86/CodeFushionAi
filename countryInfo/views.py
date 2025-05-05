from django.http import HttpResponse
from .fetchInfo import fetch_info  
from rest_framework import viewsets
from .models import AllData
from .serializers import AllDataSerializer

def fetch_countries(request):
    fetch_info()  
    return HttpResponse("Data has been fetched and stored successfully!")

class AllDataViewSet(viewsets.ModelViewSet):
    queryset= AllData.objects.all()
    serializer_class= AllDataSerializer

