import unittest
from datetime import date, timedelta
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_service_required_after_three_years(self):
        # Create a Spindler battery
        spindler_battery = SpindlerBattery()

        # Set the last service date to three years ago
        three_years_ago = date.today() - timedelta(days=365 * 3)
        spindler_battery.update_last_service_info(three_years_ago)

        # The battery should require service after three years
        self.assertTrue(spindler_battery.service_required(date.today()))