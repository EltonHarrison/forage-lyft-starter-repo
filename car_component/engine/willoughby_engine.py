from engine.base_engine import BaseEngine

class WilloughbyEngine(BaseEngine):
    def __init__(self):
        self.last_service_mileage = 0
        self.last_service_date = None

    def service_required(self, current_mileage, last_service_mileage, current_date, last_service_date):
        return current_mileage - last_service_mileage >= 60000

    def update_last_service_info(self, current_mileage, current_date):
        self.last_service_mileage = current_mileage
        self.last_service_date = current_date