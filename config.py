"""Application configuration."""
import os


# The variable stores the api key for connecting to openweathermap.org
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY") or \
                      "your_api_key"

# The variable stores the logging level
LOG_LEVEL = "DEBUG"
