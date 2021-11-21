from django import forms

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "your-api-key",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

country_list_choice = []

for num in range(0, int(response['results'])):
    country_name = ((response['response'][num]['country']), (response['response'][num]['country']))
    country_list_choice.append(country_name)
country_list_choice.sort(key=lambda y: y[1])

class SelectCountry(forms.Form):
    country_name = forms.CharField(required = True, widget = forms.Select(choices = country_list_choice))