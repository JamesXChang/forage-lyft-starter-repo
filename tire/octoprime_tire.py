from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        tire_sum = 0
        for tire in self.tire_wear:
            tire_sum += tire
        
        if tire_sum >= 3:
            return True
        else:
            return False
