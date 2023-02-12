import unittest
from pickups import getTruckByType


class TestPickupMethods(unittest.TestCase):

    def test_getpickups(self):
        electric_trucks = getTruckByType("electric")
        print(electric_trucks)


unittest.main()