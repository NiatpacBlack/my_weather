"""Testing the functionality of the coordinates.py file."""
import os
from unittest import TestCase, main, skipIf

from coordinates import MyCoordsWin, MyCoordsLinux, Coordinates


@skipIf(os.name != "nt", "Tests are not running on Linux")
class MyCoordsWinTest(TestCase):
    def setUp(self):
        self.my_coords = MyCoordsWin()

    def test_get_location(self):
        """
        Checking the get_location() function.

        The function must return coordinates in the Coordinates format.
        """
        self.assertIsInstance(self.my_coords.get_location(), Coordinates)


@skipIf(os.name != "posix", "Tests are not running on Windows")
class MyCoordsLinuxTest(TestCase):
    pass


if __name__ == "__main__":
    main()
