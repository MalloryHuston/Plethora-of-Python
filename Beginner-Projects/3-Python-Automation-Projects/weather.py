import requests

API_KEY = "3bc0440e9ddec9796ad7c5de5c0b414b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature_celsius = round(data["main"]["temp"] - 273.15, 2)
    # Fahrenheit = (9/5)Celsius + 32
    temperature_fahrenheit = round((temperature_celsius + 9/5) + 32, 2)

    print("Weather:", weather)
    print("Temperature:", temperature_celsius, "degrees celsius")
    print("Temperature:", temperature_fahrenheit, "degrees fahrenheit")
else:
    print("An error occurred.")
