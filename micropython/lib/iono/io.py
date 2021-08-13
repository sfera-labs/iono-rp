from machine import Pin
from machine import ADC
from machine import PWM

class DigitalPin(Pin):
    def __init__(self, name, pin, mode=None):
        super().__init__(pin, mode, None)
        self._name = name

    def name(self):
        return self._name

class AnalogIn(ADC):
    def __init__(self, name, pin, max_val):
        super().__init__(pin)
        self._name = name
        self._max_val = max_val

    def name(self):
        return self._name

    def __call__(self):
        return self._read_convert()

    def _read_convert(self):
        return self.read_u16() * self._max_val / 65535
    
class AV(AnalogIn):
    def __init__(self, name, pin):
        super().__init__(name, pin, max_val=30)
        
    def read_V(self):
        return self._read_convert()

class AI(AnalogIn):
    def __init__(self, name, pin):
        super().__init__(name, pin, max_val=20)
        
    def read_mA(self):
        return self._read_convert()

class AO(PWM):
    def __init__(self, name, pin):
        super().__init__(Pin(pin))
        self._name = name
        
    def name(self):
        return self._name

    def __call__(self, val=None):
        return self.duty_V(val)

    def duty_V(self, val=None):
        if val is None:
            return self.duty_u16() * 10 / 65535
        self.duty_u16(round(val * 65535 / 10))
