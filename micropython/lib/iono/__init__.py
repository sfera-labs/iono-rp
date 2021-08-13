from micropython import const
from machine import UART
from iono.io import *

__version__ = '1.0.0'

class IO:
    PIN_DO1 = const(13)
    PIN_DO2 = const(12)
    PIN_DO3 = const(11)
    PIN_DO4 = const(10)

    PIN_DI1 = const(26)
    PIN_AV1 = const(26)
    PIN_AI1 = const(26)

    PIN_DI2 = const(27)
    PIN_AV2 = const(27)
    PIN_AI2 = const(27)

    PIN_DI3 = const(28)
    PIN_AV3 = const(28)
    PIN_AI3 = const(28)

    PIN_DI4 = const(29)
    PIN_AV4 = const(29)
    PIN_AI4 = const(29)

    PIN_DI5 = const(24)
    PIN_DI6 = const(23)
    PIN_DI5_BYP = const(7)
    PIN_DI6_BYP = const(6)

    PIN_AO1 = const(8)
    
    MODE_D = const(0)
    MODE_V = const(1)
    MODE_I = const(2)
    
    def __init__(self, i1=MODE_D, i2=MODE_D, i3=MODE_D, i4=MODE_D):
        self.DO1 = DigitalPin('DO1', PIN_DO1, mode=Pin.OUT)
        self.DO2 = DigitalPin('DO2', PIN_DO2, mode=Pin.OUT)
        self.DO3 = DigitalPin('DO3', PIN_DO3, mode=Pin.OUT)
        self.DO4 = DigitalPin('DO4', PIN_DO4, mode=Pin.OUT)
        
        self._all = [self.DO1, self.DO2, self.DO3, self.DO4]
        
        if i1 is MODE_V:
            self.AV1 = AV('AV1', PIN_AV1)
            self.AI1 = None
            self.DI1 = None
            self._all.append(self.AV1)
        elif i1 is MODE_I:
            self.AI1 = AI('AI1', PIN_AI1)
            self.AV1 = None
            self.DI1 = None
            self._all.append(self.AI1)
        else:
            self.DI1 = DigitalPin('DI1', PIN_DI1, mode=Pin.IN)
            self.AV1 = None
            self.AI1 = None
            self._all.append(self.DI1)

        if i2 is MODE_V:
            self.AV2 = AV('AV2', PIN_AV2)
            self.AI2 = None
            self.DI2 = None
            self._all.append(self.AV2)
        elif i2 is MODE_I:
            self.AI2 = AI('AI2', PIN_AI2)
            self.AV2 = None
            self.DI2 = None
            self._all.append(self.AI2)
        else:
            self.DI2 = DigitalPin('DI2', PIN_DI2, mode=Pin.IN)
            self.AV2 = None
            self.AI2 = None
            self._all.append(self.DI2)

        if i3 is MODE_V:
            self.AV3 = AV('AV3', PIN_AV3)
            self.AI3 = None
            self.DI3 = None
            self._all.append(self.AV3)
        elif i3 is MODE_I:
            self.AI3 = AI('AI3', PIN_AI3)
            self.AV3 = None
            self.DI3 = None
            self._all.append(self.AI3)
        else:
            self.DI3 = DigitalPin('DI3', PIN_DI3, mode=Pin.IN)
            self.AV3 = None
            self.AI3 = None
            self._all.append(self.DI3)

        if i4 is MODE_V:
            self.AV4 = AV('AV4', PIN_AV4)
            self.AI4 = None
            self.DI4 = None
            self._all.append(self.AV4)
        elif i4 is MODE_I:
            self.AI4 = AI('AI4', PIN_AI4)
            self.AV4 = None
            self.DI4 = None
            self._all.append(self.AI4)
        else:
            self.DI4 = DigitalPin('DI4', PIN_DI4, mode=Pin.IN)
            self.AV4 = None
            self.AI4 = None
            self._all.append(self.DI4)

        self.DI5 = DigitalPin('DI5', PIN_DI5, mode=Pin.IN)
        self._all.append(self.DI5)
        self.DI5_BYP = DigitalPin('DI5_BYP', PIN_DI5_BYP)
        self._all.append(self.DI5_BYP)
        
        self.DI6 = DigitalPin('DI6', PIN_DI6, mode=Pin.IN)
        self._all.append(self.DI6)
        self.DI6_BYP = DigitalPin('DI6_BYP', PIN_DI6_BYP)
        self._all.append(self.DI6_BYP)
        
        self.AO1 = AO('AO1', PIN_AO1)
        self._all.append(self.AO1)
        
    def all(self):
        return self._all

class _RS485:
    def __init__(self):
        self._txen_n = Pin(25, mode=Pin.OUT)
        self.init()
        
    def init(self, baudrate=9600, bits=8, parity=None, stop=1, timeout=-1, timeout_char=-1):
        self._uart = UART(0, baudrate=baudrate, bits=bits, parity=parity, stop=stop, tx=Pin(16), rx=Pin(17), timeout=timeout, timeout_char=timeout_char)
        
    def __getattr__(self, attr):
        return getattr(self._uart, attr)
    
    def txen(self, enable):
        self._txen_n(not enable)
        
RS485 = _RS485()
