from engine.base_engine import BaseEngine
from battery.base_battery import BaseBattery
from datetime import datetime

class Car:
    def __init__(self, model, engine: BaseEngine, battery: BaseBattery):
        self.model = model
        self.engine = engine
        self.battery = battery

    def drive(self, distance):
        self.model.drive(distance)

    def needs_service(self):
        return self.model.needs_service()

    def update_last_service_info(self):
        self.model.update_last_service_info()