"""Testing the functionality of the weather_api_service.py file."""
from copy import deepcopy
from unittest import TestCase, main

from config import OPENWEATHER_API_KEY
from coordinates import Coordinates
from exceptions import CantGetWeather, ApiServiceError
from weather_api_service import (
    get_weather_by_coords,
    Weather,
    _get_openweather_response,
    _parse_openweather_response,
    _parse_weather_type,
)


class WeatherApiServiceTest(TestCase):
    def setUp(self) -> None:
        self.my_location = Coordinates(45.23, 125.42)
        self.openweather_response = _get_openweather_response(
            latitude=self.my_location.latitude,
            longitude=self.my_location.longitude,
            api_key=OPENWEATHER_API_KEY,
        )

    def test_get_weather_by_coords(self):
        """
        Checking the get_weather_by_coords() function.

        The test verifies that the data returned by the function matches
        the Weather data type.

        The test verifies that the function returns the desired exception
        under certain conditions.
        """
        self.assertIsInstance(
            get_weather_by_coords(
                self.my_location,
                OPENWEATHER_API_KEY,
            ),
            Weather,
        )
        with self.assertRaises(AttributeError):
            get_weather_by_coords(
                (45.23, 125.52),
                OPENWEATHER_API_KEY,
            )
        with self.assertRaises(CantGetWeather):
            get_weather_by_coords(self.my_location, "123456789")

    def test__parse_openweather_response1(self):
        with self.assertRaises(ApiServiceError):
            openweather_response_copy = deepcopy(self.openweather_response)
            del openweather_response_copy["weather"]
            _parse_openweather_response(openweather_response_copy)

    def test__parse_openweather_response2(self):
        with self.assertRaises(ApiServiceError):
            openweather_response_copy = deepcopy(self.openweather_response)
            del openweather_response_copy["main"]
            _parse_openweather_response(openweather_response_copy)

    def test__parse_openweather_response3(self):
        with self.assertRaises(ApiServiceError):
            openweather_response_copy = deepcopy(self.openweather_response)
            del openweather_response_copy["sys"]
            _parse_openweather_response(openweather_response_copy)

    def test__parse_openweather_response4(self):
        with self.assertRaises(ApiServiceError):
            openweather_response_copy = deepcopy(self.openweather_response)
            del openweather_response_copy["name"]
            _parse_openweather_response(openweather_response_copy)

    def test__parse_weather_type(self):
        with self.assertRaises(ApiServiceError):
            openweather_response_copy = deepcopy(self.openweather_response)
            openweather_response_copy["weather"][0]["id"] = "999"
            _parse_weather_type(openweather_response_copy)


if __name__ == "__main__":
    main()
