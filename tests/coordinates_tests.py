from unittest import TestCase, main

from coordinates import MyCoords, Coordinates


class MyCoordsTest(TestCase):
    def setUp(self):
        self.my_coords = MyCoords()

    def test_get_location(self):
        self.assertIsInstance(self.my_coords.get_location(), Coordinates)


if __name__ == "__main__":
    main()
