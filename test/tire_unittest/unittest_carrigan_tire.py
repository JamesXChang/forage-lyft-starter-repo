import unittest

from tire.carrigan_tire import CarriganTire

class UnitTestCarriganTire(unittest.TestCase):
    def test1(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())

    def test2(self):
        tire_wear = [0.9, 0.1, 0.1, 0.1]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())