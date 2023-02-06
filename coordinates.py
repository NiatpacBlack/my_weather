"""Functionality for getting coordinates from Windows OS."""
import asyncio
from dataclasses import dataclass

import winsdk.windows.devices.geolocation as wdg

from exceptions import GettingWindowsLocationError


@dataclass(slots=True, frozen=True)
class Coordinates:
    """Data type descriptions for coordinates."""

    latitude: float
    longitude: float


class MyCoordsWin:
    """
    A class that allows you to find out the current geolocation gps data.
    Designed for Windows OS.
    """

    def __init__(self) -> None:
        self.locator = None
        self.my_position = None

    def get_location(self) -> Coordinates:
        """Get the current location."""
        return asyncio.run(self._get_coords())

    async def _get_coords(self) -> Coordinates:
        self.locator = wdg.Geolocator()
        try:
            self.my_position = await self.locator.get_geoposition_async()
        except PermissionError as exc:
            raise GettingWindowsLocationError(
                "ERROR: You need to allow applications "
                "to access you location in Windows settings"
            ) from exc
        return Coordinates(
            self.my_position.coordinate.latitude,
            self.my_position.coordinate.longitude,
        )


class MyCoordsLinux:
    """
    A class that allows you to find out the current geolocation gps data.
    Designed for Linux OS.
    """

    pass


if __name__ == "__main__":
    my_location = MyCoordsWin().get_location()
