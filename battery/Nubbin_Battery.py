from battery.battery import Battery
from datetime import timedelta

class NubbiinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return abs(self.current_date - self.last_service_date) > timedelta(days=4*365)