class CantGetWeather(Exception):
    """Can't get weather from openweathermap."""

    pass


class ApiServiceError(Exception):
    """OpenWeatherMap returned incorrect api response data."""

    pass


class GettingWindowsLocationError(Exception):
    """The error appears when there is no access to the location in the Windows settings."""

    pass
