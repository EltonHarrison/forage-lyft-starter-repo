from battery.base_battery import BaseBattery
from datetime import date

class NubbinBattery(BaseBattery):
    def __init__(self):
        self.last_service_date = None

    def service_required(self, last_service_date):
        if not last_service_date:
            return True

        time_difference = date.today().year - last_service_date.year
        return time_difference >= 4

    def update_last_service_info(self, current_date):
        self.last_service_date = current_date