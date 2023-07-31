import unittest
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from models.calliope import Calliope
from models.glissade import Glissade
from models.palindrome import Palindrome
from models.rorschach import Rorschach
from models.thovex import Thovex
from car_component.car import Car

class TestCarComponent(unittest.TestCase):
    def setUp(self):
        self.capulet_engine = CapuletEngine()
        self.willoughby_engine = WilloughbyEngine()
        self.sternman_engine = SternmanEngine()
        self.spindler_battery = SpindlerBattery()
        self.nubbin_battery = NubbinBattery()

        self.calliope_car = Calliope(self.capulet_engine, self.spindler_battery)
        self.glissade_car = Glissade(self.willoughby_engine, self.spindler_battery)
        self.palindrome_car = Palindrome(self.sternman_engine, self.spindler_battery)
        self.rorschach_car = Rorschach(self.willoughby_engine, self.nubbin_battery)
        self.thovex_car = Thovex(self.capulet_engine, self.nubbin_battery)

        self.car1 = Car(self.calliope_car)
        self.car2 = Car(self.glissade_car)
        self.car3 = Car(self.palindrome_car)
        self.car4 = Car(self.rorschach_car)
        self.car5 = Car(self.thovex_car)

    def test_drive(self):
        self.car1.drive(25000)
        self.car2.drive(45000)
        self.car3.drive(10000)
        self.car4.drive(80000)
        self.car5.drive(30000)

        self.assertEqual(self.car1.model.current_mileage, 25000)
        self.assertEqual(self.car2.model.current_mileage, 45000)
        self.assertEqual(self.car3.model.current_mileage, 10000)
        self.assertEqual(self.car4.model.current_mileage, 80000)
        self.assertEqual(self.car5.model.current_mileage, 30000)

    def test_needs_service(self):
        self.car1.drive(30000)
        self.car2.drive(50000)
        self.car3.drive(20000)
        self.car4.drive(90000)
        self.car5.drive(40000)

        today = date.today()

        # Set last service date for car1 and car2 to more than 2 years ago
        self.car1.model.update_last_service_info()
        self.car2.model.update_last_service_info()

        # Set last service date for car3, car4, and car5 to less than 2 years ago
        self.car3.model.update_last_service_info(today)
        self.car4.model.update_last_service_info(today)
        self.car5.model.update_last_service_info(today)

        # car1 and car2 should need service
        self.assertTrue(self.car1.needs_service())
        self.assertTrue(self.car2.needs_service())

        # car3, car4, and car5 should not need service
        self.assertFalse(self.car3.needs_service())
        self.assertFalse(self.car4.needs_service())
        self.assertFalse(self.car5.needs_service())

    def test_update_last_service_info(self):
        today = date.today()

        # Update last service info for car1
        self.car1.update_last_service_info()
        self.assertEqual(self.car1.model.last_service_date, today)
        self.assertEqual(self.car1.engine.last_service_date, today)
        self.assertEqual(self.car1.battery.last_service_date, today)

        # Update last service info for car2
        self.car2.update_last_service_info()
        self.assertEqual(self.car2.model.last_service_date, today)
        self.assertEqual(self.car2.engine.last_service_date, today)
        self.assertEqual(self.car2.battery.last_service_date, today)

        # Update last service info for car3
        self.car3.update_last_service_info()
        self.assertEqual(self.car3.model.last_service_date, today)
        self.assertEqual(self.car3.engine.last_service_date, today)
        self.assertEqual(self.car3.battery.last_service_date, today)

if __name__ == "__main__":
    unittest.main()