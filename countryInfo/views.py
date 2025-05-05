from django.http import HttpResponse
from .fetchInfo import fetch_info  

def fetch_countries(request):
    fetch_info()  
    return HttpResponse("Data has been fetched and stored successfully!")
