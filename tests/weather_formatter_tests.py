from unittest import TestCase, main

from config import OPENWEATHER_API_KEY
from coordinates import MyCoords
from weather_api_service import get_weather_by_coords
from weather_formatter import format_weather
import os


class WeatherFormatterTest(TestCase):
    def setUp(self):
        self.my_location = MyCoords().get_location()
        self.weather = get_weather_by_coords(
            coordinates=self.my_location,
            api_key=os.getenv("OPENWEATHER_API_KEY") or OPENWEATHER_API_KEY,
        )

    def test_format_weather(self):
        self.assertIsInstance(format_weather(self.weather), str)


if __name__ == "__main__":
    main()
