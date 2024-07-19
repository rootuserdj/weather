from django.shortcuts import render
import requests
from django.contrib import messages

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kathmandu'
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978'
    param = {'units':'metric'}
    data = requests.get(url,param).json()
    try:

        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        wind = data['wind']['speed']
        icon = data['weather'][0]['icon']
        humidity = data['main']['humidity']

        contex = {
            'temp':temp,
            'city':city,
            'desc':desc,
            'wind':wind,
            'icon':icon,
            'humidity':humidity,

        }

        return render(request,'index.html',contex)
    except:
        temp = 0
        wind = 0
        humidity = 0

        desc = "City Not Found"
        messages.error(request,"City Not Found !!")
        data = {
            'temp':temp,
            'desc':desc,
            'wind':wind,
            'humidity':humidity
        }
        return render(request,'index.html',data)
    
