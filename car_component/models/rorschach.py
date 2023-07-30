from models.car_model import CarModel

class Rorschach(CarModel):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)

    def needs_service(self):
        return self.engine.service_required(
            self.current_mileage, self.last_service_date,
            self.last_service_mileage, self.last_service_date
        ) or self.battery.service_required(self.last_service_date)