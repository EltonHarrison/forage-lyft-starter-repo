from engine.base_engine import BaseEngine
from battery.base_battery import BaseBattery
from datetime import datetime
from abc import ABC, abstractmethod

class CarModel(ABC):
    def __init__(self, engine: BaseEngine, battery: BaseBattery):
        self.engine = engine
        self.battery = battery
        self.current_mileage = 0
        self.last_service_date = None

    def drive(self, distance):
        self.current_mileage += distance

    @abstractmethod
    def needs_service(self):
        pass

    def update_last_service_info(self):
        self.engine.update_last_service_info(
            self.current_mileage, datetime.today()
        )
        self.battery.update_last_service_info(datetime.today())
        self.last_service_date = datetime.today()