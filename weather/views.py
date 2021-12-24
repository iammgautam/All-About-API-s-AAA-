from django.shortcuts import redirect, render
import requests
import pandas as pd
# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {
            'q':city,
        }
        headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': "e0b5fd0052msh54c8b755849dafbp173ad8jsned60be06f217"
        }
        response = requests.request('GET', url, headers=headers, params=querystring).json()

        context = {
            'city_name':str(response['location']['name']),
            'temp': response['current']['temp_c'],
            'country_name':str(response['location']['country']),
            'local_time':str(response['location']['localtime']),
            'humidity': response['current']['humidity'],
            'wind_speed': response['current']['wind_kph'],
            'temp_icon':response['current']['condition']['icon'],
            'temp_text':response['current']['condition']['text'],
            # 'feels_like': response['current']['feelslike_c'],
        }
    else:
        context = {}
    return render(request, 'weather/index.htm', context)