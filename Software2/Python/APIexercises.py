import requests
import json

# First exercise
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])


# Second exercise
municipality = input("Enter municipality: ")
request = f"http://api.openweathermap.org/geo/1.0/direct?q={municipality}&limit=1&appid=89e7f1f0e964596a0c36f5f222d9d2b9"
response = requests.get(request).json()
latitude = response[0]["lat"]
longitude = response[0]["lon"]

request = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=89e7f1f0e964596a0c36f5f222d9d2b9"
response = requests.get(request).json()
weatherDescription = response["weather"][0]["description"]
temperatureKelvin = response["main"]["temp"]
temperatureCelsius = temperatureKelvin - 273.15
print(f"Weather in {municipality}: {weatherDescription}\nTemperature in Celsius: {temperatureCelsius:.2f}")
