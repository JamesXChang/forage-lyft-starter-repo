import unittest

from tire.octoprime_tire import OctoprimeTire

class UnitTestOctoprimeTire(unittest.TestCase):
    def test1(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())

    def test2(self):
        tire_wear = [1, 1, 1, 0]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())