"""Executable file to run the application."""
import os
import sys
from pathlib import Path

from config import OPENWEATHER_API_KEY
from coordinates import MyCoordsWin, Coordinates
from exceptions import GettingWindowsLocationError, CantGetWeather
from history import PlainFileWeatherStorage, save_weather
from log_config import logger
from weather_api_service import get_weather_by_coords
from weather_formatter import format_weather


@logger.catch()
def main():
    """The function to launch the application."""
    try:
        if os.name == 'nt':
            my_location = MyCoordsWin().get_location()
        else:
            my_location = Coordinates(latitude=51.505, longitude=-0.09)
    except GettingWindowsLocationError:
        error_message = "Программа не смогла получить данные геолокации " \
                        "из вашей системы."
        logger.exception(error_message)
        print(error_message)
        sys.exit(1)
    try:
        weather = get_weather_by_coords(
            my_location,
            OPENWEATHER_API_KEY,
        )
    except CantGetWeather:
        error_message = "Программа не смогла получить данные " \
                        "о погоде в сервисе OpenWeatherMap."
        logger.exception(error_message)
        print(error_message)
        sys.exit(1)
    save_weather(
        weather,
        PlainFileWeatherStorage(file=Path.cwd() / "history.txt"),
    )
    print(format_weather(weather))


if __name__ == "__main__":
    main()
