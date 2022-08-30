import unittest
import datetime

from battery.Spindler_Battery import SpindlerBattery

class UnitTestSpindlerBattery(unittest.TestCase):
    def test_1(self):
        current_date = datetime.date(2022,8,31)
        last_service_date = datetime.date(2022,7,31)
        Battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(Battery.needs_service())

    def test_2(self):
        current_date = datetime.date(2022,8,31)
        last_service_date = datetime.date(2020,7,31)
        Battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(Battery.needs_service())