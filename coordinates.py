import asyncio
from dataclasses import dataclass

import winsdk.windows.devices.geolocation as wdg

from exceptions import GettingWindowsLocationError


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


class MyCoords:
    """A class that allows you to find out the current location (latitude, longitude) from Windows OS gps data."""

    def __init__(self):
        self.locator = None
        self.my_position = None

    def get_location(self) -> Coordinates:
        return asyncio.run(self._get_coords())

    async def _get_coords(self) -> Coordinates:
        self.locator = wdg.Geolocator()
        try:
            self.my_position = await self.locator.get_geoposition_async()
        except PermissionError:
            raise GettingWindowsLocationError(
                "ERROR: You need to allow applications to access you location in Windows settings"
            )
        else:
            return Coordinates(
                self.my_position.coordinate.latitude, self.my_position.coordinate.longitude
            )


if __name__ == '__main__':
    my_location = MyCoords().get_location()
