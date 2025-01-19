import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            url = f"https://goweather.herokuapp.com/weather/{city.lower()}"
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
                print(f"Weather Data: {weather_data}")  # Debugging: Print raw data
                
                if "temperature" in weather_data:
                    weather_data["city"] = city  # Add city name to the data for display
                else:
                    error_message = f"No weather data found for '{city}'."
            else:
                error_message = f"Could not fetch weather for '{city}'. Please try again."

    return render(request, 'index.html', {
        'weather_data': weather_data,
        'error_message': error_message,
    })
