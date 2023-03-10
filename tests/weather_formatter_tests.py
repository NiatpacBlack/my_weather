"""Testing the functionality of the weather_formatter.py file."""
from unittest import TestCase, main

from config import OPENWEATHER_API_KEY
from coordinates import MyCoordsWin
from weather_api_service import get_weather_by_coords
from weather_formatter import format_weather


class WeatherFormatterTest(TestCase):
    def setUp(self):
        self.my_location = MyCoordsWin().get_location()
        self.weather = get_weather_by_coords(
            coordinates=self.my_location,
            api_key=OPENWEATHER_API_KEY,
        )

    def test_format_weather(self):
        """
        Checking the format_weather() function.

        The test checks that the function returns a string.
        """
        self.assertIsInstance(format_weather(self.weather), str)


if __name__ == "__main__":
    main()
