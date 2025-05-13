from crewai.tools import tool, BaseTool
from langchain_community.tools import DuckDuckGoSearchResults
import requests
from typing import Optional, Tuple
from pydantic import PrivateAttr

@tool
def search_web_tool(query: str):
    """
    Searches the web and returns results.
    """
    search_tool = DuckDuckGoSearchResults(num_results=10, verbose=True)
    return search_tool.run(query)


class WeatherTool(BaseTool):
    name: str = "OpenWeatherTool"
    description: str = "Returns current weather info for given city, state, and country."
    _api_key: str = PrivateAttr()

    def __init__(self, api_key: str):
        super().__init__()
        self._api_key = api_key

    def get_coordinates(self, city: str, state: Optional[str], country: Optional[str]) -> Tuple[float, float]:
        query = city
        if state:
            query += f",{state}"
        if country:
            query += f",{country}"

        url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            "q": query,
            "limit": 1,
            "appid": self._api_key
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            raise ValueError("No coordinates found for the specified location.")
        
        return data[0]['lat'], data[0]['lon']

    def _run(self, city: str, state: Optional[str] = None, country: Optional[str] = None) -> str:
        try:
            lat, lon = self.get_coordinates(city, state, country)
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={self._api_key}"
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                return f"Error fetching weather data: {data.get('message', 'Unknown error')}"

            weather = data.get("weather", [{}])[0]
            main = data.get("main", {})
            wind = data.get("wind", {})
            clouds = data.get("clouds", {})
            sys = data.get("sys", {})

            summary = (
                f"{data.get('name', 'Unknown Location')}, {sys.get('country', '')}\n"
                f"Temperature: {main.get('temp')}°C (Feels like {main.get('feels_like')}°C)\n"
                f"Condition: {weather.get('main')} - {weather.get('description')}\n"
                f"Humidity: {main.get('humidity')}%\n"
                f"Wind: {wind.get('speed')} m/s at {wind.get('deg')}°\n"
                f"Cloudiness: {clouds.get('all')}%\n"
                f"Pressure: {main.get('pressure')} hPa\n"
            )
            return summary

        except Exception as e:
            return f"Invalid input or error occurred: {str(e)}"