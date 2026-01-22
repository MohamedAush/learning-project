# Python program to find current weather details of any city using openweathermap api 
import requests 
  
# Enter your API key here 
api_key = "cbc69fddbaa9e5d44aa05c28c6696722"
  
# Step 1: Get user input
city_name = input("Enter city name: ")
state_code = input("Enter state code (optional, press Enter to skip): ")
country_code = input("Enter country code (e.g., US, JP): ")

# Step 2: Get coordinates using Geocoding API
limit = 1
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_key}"

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

print("Geocoding response:", geo_data)  # DEBUG LINE

if len(geo_data) == 0:
    print("Location not found. Please check your city or country code.")
    exit()

location = geo_data[0]
lat = location.get("lat")
lon = location.get("lon")

print(f"Found location: {location.get('name')} ({lat}, {lon})")

# Step 3: Get weather using coordinates
weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

print("Weather response:", weather_data)  # DEBUG LINE

if weather_data.get("cod") != 200:
    print("Weather API error:", weather_data)
    exit()

main_data = weather_data.get("main")
weather_list = weather_data.get("weather")

if not main_data or not weather_list:
    print("Weather data missing in response.")
    exit()

temp_kelvin = main_data.get("temp")
pressure = main_data.get("pressure")
humidity = main_data.get("humidity")
description = weather_list[0].get("description")

temp_celsius = temp_kelvin - 273.15

print("\n===== Weather Result =====")
print(f"Temperature: {temp_celsius:.2f} °C")
print(f"Pressure: {pressure} hPa")
print(f"Humidity: {humidity} %")
print(f"Description: {description}")