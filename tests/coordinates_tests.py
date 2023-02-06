"""Testing the functionality of the coordinates.py file."""
from unittest import TestCase, main

from coordinates import MyCoords, Coordinates


class MyCoordsTest(TestCase):
    def setUp(self):
        self.my_coords = MyCoords()

    def test_get_location(self):
        """
        Checking the get_location() function.

        The function must return coordinates in the Coordinates format.
        """
        self.assertIsInstance(self.my_coords.get_location(), Coordinates)


if __name__ == "__main__":
    main()
