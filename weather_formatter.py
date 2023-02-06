"""String formatting functionality for outputting to the console."""
from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formats weather data in string."""
    return (
        f"Погода рядом с {weather.city}: {weather.weather_type}. \n"
        f"Температура {weather.temperature} С, "
        f"ощущается как {weather.feels_like} С. \n"
        f"Восход: {weather.sunrise.strftime('%H:%M')} \n"
        f"Закат: {weather.sunset.strftime('%H:%M')} \n"
    )
