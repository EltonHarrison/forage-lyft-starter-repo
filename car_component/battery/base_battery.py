from abc import ABC, abstractmethod

class BaseBattery(ABC):
    @abstractmethod
    def service_required(self, last_service_date):
        pass

    @abstractmethod
    def update_last_service_info(self, current_date):
        pass