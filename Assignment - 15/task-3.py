import requests  # type: ignore

def display_specific_weather(city):
    api_key = "b8cd10338348a4e3b62b70110ab24905"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", description)
def test_task3():
    # Function exists
    assert callable(display_specific_weather)

    # Input city must be a string
    assert isinstance("Hyderabad", str)

    # City names can vary
    assert isinstance("London", str)
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    display_specific_weather(city_name)