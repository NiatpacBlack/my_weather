"""Description of custom exceptions."""


class CantGetWeather(Exception):
    """Can't get weather from openweathermap."""


class ApiServiceError(Exception):
    """OpenWeatherMap returned incorrect api response data."""


class GettingWindowsLocationError(Exception):
    """The error appears when there is no access to the location in the Windows settings."""
