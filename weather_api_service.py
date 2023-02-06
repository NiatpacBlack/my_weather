"""Functionality for getting weather data from openweathermap.org."""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias, Literal

import requests

from coordinates import Coordinates
from exceptions import CantGetWeather, ApiServiceError


Celsius: TypeAlias = int


class WeatherType(Enum):
    """The data type with options for describing weather conditions."""

    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

    def __str__(self):
        return self.value


@dataclass(slots=True, frozen=True)
class Weather:
    """Description of data types for general weather information."""

    temperature: Celsius
    feels_like: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather_by_coords(coordinates: Coordinates, api_key: str) -> Weather:
    """Returns weather data at a specific latitude and longitude point."""
    openweather_response = _get_openweather_response(
        latitude=coordinates.latitude,
        longitude=coordinates.longitude,
        api_key=api_key,
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(
    latitude: float, longitude: float, api_key: str
) -> dict[str, object]:
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    url_parameters = {
        "lat": latitude,
        "lon": longitude,
        "units": "metric",
        "lang": "ru",
        "appid": api_key,
    }
    all_weather_by_coords = requests.get(
        api_url, params=url_parameters, timeout=10
    ).json()
    if all_weather_by_coords["cod"] != 200:
        raise CantGetWeather()
    return all_weather_by_coords


def _parse_openweather_response(openweather_response: dict) -> Weather:
    try:
        weather = Weather(
            temperature=_parse_temperature(openweather_response),
            feels_like=_parse_feels_like_temperature(openweather_response),
            weather_type=_parse_weather_type(openweather_response),
            sunrise=_parse_sun_time(openweather_response, "sunrise"),
            sunset=_parse_sun_time(openweather_response, "sunset"),
            city=_parse_city(openweather_response),
        )
    except (IndexError, KeyError) as exc:
        raise ApiServiceError from exc
    return weather


def _parse_temperature(openweather_response: dict) -> Celsius:
    return round(openweather_response["main"]["temp"])


def _parse_feels_like_temperature(openweather_response: dict) -> Celsius:
    return round(openweather_response["main"]["feels_like"])


def _parse_weather_type(openweather_response: dict) -> WeatherType:
    weather_type_id = str(openweather_response["weather"][0]["id"])
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS,
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_sun_time(
    openweather_response: dict, time: Literal["sunrise"] | Literal["sunset"]
) -> datetime:
    timestamp = openweather_response["sys"][time]
    return datetime.fromtimestamp(timestamp)


def _parse_city(openweather_response: dict) -> str:
    return openweather_response["name"]
