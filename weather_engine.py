import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

class WeatherEngine:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, lat, lon):
        """Mengecek cuaca berdasarkan koordinat pesawat atau bandara"""
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'metric' # Agar suhu dalam Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Kita ambil data penting: kondisi cuaca dan kecepatan angin
            weather_desc = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            
            return {
                "condition": weather_desc,
                "wind_speed": wind_speed
            }
        except Exception as e:
            logging.error(f"Gagal mengambil data cuaca: {e}")
            return None

if __name__ == "__main__":
    engine = WeatherEngine()
    # Tes cuaca Jakarta
    jakarta_weather = engine.get_weather(-6.2, 106.8)
    print(f"Cuaca Jakarta: {jakarta_weather}")