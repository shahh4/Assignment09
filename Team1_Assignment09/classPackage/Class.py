import requests

def get_current_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extracting relevant information
        location = data['location']['name']
        country = data['location']['country']
        temperature_celsius = data['current']['temp_c']
        condition = data['current']['condition']['text']
        wind_speed = data['current']['wind_kph']
        humidity = data['current']['humidity']

        # Printing weather information
        print(f"Current weather in {location}, {country}:")
        print(f"Temperature: {temperature_celsius}°C")
        print(f"Condition: {condition}")
        print(f"Wind Speed: {wind_speed} kph")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")

if __name__ == "__main__":
    api_key = "d25578a2e46e481fbc311658240304"  # Your WeatherAPI key
    city = "New York"  # Example city

    get_current_weather(api_key, city)