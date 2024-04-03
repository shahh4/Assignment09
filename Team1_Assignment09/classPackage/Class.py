import requests

class WeatherAPI:
    def __init__(self):
        self.api_key = "d25578a2e46e481fbc311658240304"
        self.base_url = "http://api.weatherapi.com/v1"

    def get_current_weather(self, location):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={location}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    def extract_interesting_data(self, data):
        if data is None:
            return
        # Extracting interesting data, for example, let's print current temperature and condition
        current = data.get("current", {})
        location = data.get("location", {})
        print(f"Weather for {location.get('name', '')}, {location.get('region', '')}, {location.get('country', '')}:")
        print(f"Temperature: {current.get('temp_c', '')}°C")
        print(f"Condition: {current.get('condition', {}).get('text', '')}")

    def API_Weatherlocation(self):
        location = "New York"  # Change this to any location you want
        weather_data = self.get_current_weather(location)
        self.extract_interesting_data(weather_data)
