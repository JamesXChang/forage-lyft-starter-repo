from abc import ABC, abstractmethod
import re
from Serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        if self.engine.needs_service():
            return True
        elif self.battery.needs_service():
            return True
        else: 
            return False
