import requests
from .config import API_KEY


def get_weather_data(query, forecast_days=1, lang="en"):
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/forecast.json"
    
    params = {
        "key": API_KEY,
        "q": query,
        "days": forecast_days, 
        "alerts": "yes",
        "lang": lang
    }

    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à WeatherAPI.com: {e}")
        return None
    
def get_historical_data(query, date, lang):
    base_url = "http://api.weatherapi.com/v1"
    endpoint = "/history.json"
    
    params = {
        "key": API_KEY,
        "q": query,
        "dt": date, 
        "lang": lang
    }

    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição à WeatherAPI.com: {e}")
        return None