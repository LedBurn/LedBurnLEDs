
from Sensors.RFID import RFID
from Sensors.Temperature import Temperature
from Sensors.Motion import Motion

class Decisions:

    def __init__(self):
        self.rfid = RFID()
        self.temperature = Temperature()
        self.motion = Motion()

    def process(self):
        sachiMeter, illusionsFlag = self.rfid.process()
        curr_temperature = self.temperature.get_temperature()
