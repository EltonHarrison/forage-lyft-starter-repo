from engine.base_engine import BaseEngine

class SternmanEngine(BaseEngine):
    def __init__(self):
        self.warning_indicator_on = False
        self.last_service_date = None

    def set_warning_indicator(self, is_on):
        self.warning_indicator_on = is_on

    def service_required(self, current_mileage, last_service_mileage, current_date, last_service_date):
        return self.warning_indicator_on

    def update_last_service_info(self, current_mileage, current_date):
        self.last_service_date = current_date