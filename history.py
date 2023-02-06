"""Functionality for adding weather query data to a file."""
from datetime import datetime
from pathlib import Path
from typing import Protocol

from weather_api_service import Weather
from weather_formatter import format_weather


class WeatherStorage(Protocol):
    """Interface for any storage saving weather."""

    def save(self, weather: Weather) -> None:
        """The method should deal with saving data to a file."""
        raise NotImplementedError


class PlainFileWeatherStorage:
    """Store weather in plane text file."""

    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        """Save weather to storage."""
        datetime_now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._file, "a", encoding="windows-1251") as open_file:
            open_file.write(f"{datetime_now}\n{formatted_weather}\n")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Save weather in the storage."""
    storage.save(weather)
