import os
from pathlib import Path

from config import OPENWEATHER_API_KEY
from coordinates import MyCoords
from exceptions import GettingWindowsLocationError, CantGetWeather
from history import PlainFileWeatherStorage, save_weather
from weather_api_service import get_weather_by_coords
from weather_formatter import format_weather


def main():
    try:
        my_location = MyCoords().get_location()
    except GettingWindowsLocationError:
        print("Программа не смогла получить данные геолокации из вашей системы.")
        exit(1)
    try:
        weather = get_weather_by_coords(my_location, os.getenv("OPENWEATHER_API_KEY") or OPENWEATHER_API_KEY)
    except CantGetWeather:
        print("Программа не смогла получить данные о погоде в сервисе OpenWeatherMap.")
        exit(1)
    save_weather(weather, PlainFileWeatherStorage(file=Path.cwd() / "history.txt"))
    print(format_weather(weather))


if __name__ == "__main__":
    main()
