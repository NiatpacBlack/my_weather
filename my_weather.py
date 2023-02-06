"""Executable file to run the application."""
import os
import sys
from pathlib import Path

from config import OPENWEATHER_API_KEY
from coordinates import MyCoordsWin
from exceptions import GettingWindowsLocationError, CantGetWeather
from history import PlainFileWeatherStorage, save_weather
from log_config import logger
from weather_api_service import get_weather_by_coords
from weather_formatter import format_weather


@logger.catch()
def main():
    """The function to launch the application."""
    try:
        my_location = MyCoordsWin().get_location() if os.name == "nt" else None
    except GettingWindowsLocationError:
        logger.exception(
            "Программа не смогла получить данные геолокации из вашей системы.")
        print(
            "Программа не смогла получить данные геолокации из вашей системы.")
        sys.exit(1)
    try:
        weather = get_weather_by_coords(
            my_location,
            os.getenv("OPENWEATHER_API_KEY") or OPENWEATHER_API_KEY,
        )
    except CantGetWeather:
        logger.exception(
            "Программа не смогла получить данные о погоде в сервисе "
            "OpenWeatherMap."
        )
        print(
            "Программа не смогла получить данные о погоде в сервисе " 
            "OpenWeatherMap."
        )
        sys.exit(1)
    save_weather(weather,
                 PlainFileWeatherStorage(file=Path.cwd() / "history.txt"))
    print(format_weather(weather))


if __name__ == "__main__":
    main()
