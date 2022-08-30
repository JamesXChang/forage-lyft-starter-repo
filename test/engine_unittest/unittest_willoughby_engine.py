import unittest

from engine.willoughby_engine import WilloughbyEngine

class UnitTestWilloughbyEngine(unittest.TestCase):
    def test1(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test2(self):
        current_mileage = 70000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())