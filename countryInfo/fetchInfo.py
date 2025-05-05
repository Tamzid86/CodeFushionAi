from django.shortcuts import render
import requests
from countryInfo.models import AllData

def fetch_info():
    res = requests.get('https://restcountries.com/v3.1/all')
    if res.status_code==200:
        countries = res.json()
        for c in countries:
            AllData.objects.create(
                country_code=c.get('cca2', ''),
                country_name=c.get('name',{}).get('common','Unknown'),
                full_data=c
            )
            