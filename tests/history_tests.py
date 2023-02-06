"""Testing the functionality of the history.py file."""
import os
from datetime import datetime
from pathlib import Path
from unittest import TestCase, main

from config import OPENWEATHER_API_KEY
from coordinates import MyCoordsWin
from history import save_weather, PlainFileWeatherStorage
from weather_api_service import get_weather_by_coords
from weather_formatter import format_weather


class WeatherFormatterTest(TestCase):
    def setUp(self):
        self.my_location = MyCoordsWin().get_location()
        self.weather = get_weather_by_coords(
            coordinates=self.my_location,
            api_key=os.getenv("OPENWEATHER_API_KEY") or OPENWEATHER_API_KEY,
        )

    def test_save_weather(self):
        """
        Checking the save_weather() function.

        The test checks the function's ability to write data to a file.
        """
        test_text = f"{datetime.now()}\n{format_weather(self.weather)}\n"
        file_path = Path.cwd() / "tests/history_test.txt"
        save_weather(self.weather, PlainFileWeatherStorage(file=file_path))
        with open(file_path, "r", encoding="windows-1251") as open_file:
            history_text = open_file.read()
        self.assertIn(test_text, history_text)


if __name__ == "__main__":
    main()
