from datetime import datetime
from pathlib import Path
from typing import Protocol

from weather_api_service import Weather
from weather_formatter import format_weather


class WeatherStorage(Protocol):
    """Interface for any storage saving weather."""

    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage:
    """Store weather in plane text file."""

    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        datetime_now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._file, "a") as f:
            f.write(f"{datetime_now}\n{formatted_weather}\n")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Save weather in the storage."""
    storage.save(weather)
