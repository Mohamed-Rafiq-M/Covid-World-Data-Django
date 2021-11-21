from django.shortcuts import render
from .forms import SelectCountry
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "your-api-key",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def covid(request):
    country_form = SelectCountry
    
    if request.method == 'POST':
        country_selected = request.POST['country_name']
        for num in range(0, int(response['results'])):
            if country_selected == response['response'][num]['country']:
                newcases = response['response'][num]['cases']['new']
                activecases = response['response'][num]['cases']['active']
                criticalcases = response['response'][num]['cases']['critical']
                recovered = response['response'][num]['cases']['recovered']
                totalcases = response['response'][num]['cases']['total']
                death = int(totalcases) - int(activecases) - int(recovered)
        
        context = {'form':country_form,'countryselected':country_selected, 'newcases':newcases, 'activecases':activecases, 'criticalcases':criticalcases, 'recovered':recovered, 'death':death, 'totalcases':totalcases}    
        return render(request,'index.html',context)
    
    return render(request, 'index.html', {'form':country_form,'countryselected':'Country Name', 'newcases':'No Record', 'activecases':'No Record', 'criticalcases':'No Record', 'recovered':'No Record', 'death':'No Record', 'totalcases':'No Record'})