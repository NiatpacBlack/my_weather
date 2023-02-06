"""Description of custom exceptions."""


class CantGetWeather(Exception):
    """Can't get weather from openweathermap."""


class ApiServiceError(Exception):
    """OpenWeatherMap returned incorrect api response data."""


class GettingWindowsLocationError(Exception):
    """Ошибка доступа к геолокации в Windows OS."""
