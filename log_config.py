from loguru import logger

from config import LOG_LEVEL


logger.remove()
logger.add(
    "logs/my_weather_debug.log",
    format="{time} {level} {message}",
    level=f"{LOG_LEVEL}",
    rotation="1 day",
    compression="zip",
)
