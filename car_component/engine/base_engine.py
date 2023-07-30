from abc import ABC, abstractmethod

class BaseEngine(ABC):
    @abstractmethod
    def service_required(self, current_mileage, last_service_mileage, current_date, last_service_date):
        pass

    @abstractmethod
    def update_last_service_info(self, current_mileage, current_date):
        pass