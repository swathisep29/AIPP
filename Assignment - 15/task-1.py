#b8cd10338348a4e3b62b70110ab24905 
import json
import urllib.request  # Use standard library to make HTTP requests to the weather API
def get_weather_details(city_name):
    api_key = "b8cd10338348a4e3b62b70110ab24905"  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    with urllib.request.urlopen(complete_url) as response:
        data = response.read().decode("utf-8")
        weather_data = json.loads(data)
    print(json.dumps(weather_data, indent=4))

# Example usage
city = input("Enter city name: ") 
get_weather_details(city)   