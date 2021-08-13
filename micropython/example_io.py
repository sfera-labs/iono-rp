from iono import IO
from machine import Pin
import time

# initialize Iono's IO, multimode inputs used as: DI1, DI2, AV3, AI4
io = IO(i1=IO.MODE_D, i2=IO.MODE_D, i3=IO.MODE_V, i4=IO.MODE_I)
ao1V = 0;

# configure DI5_BYP as input and DI6_BYP as output
io.DI5_BYP.init(mode=Pin.IN)
io.DI6_BYP.init(mode=Pin.OUT)

# handler for DI1 interrupt (see below)
def on_di1_change(di):
    global io
    # set DO3 to follow DI1
    io.DO3(di())

# configure interrupt on DI1 to call on_di1_change() when its state changes
io.DI1.irq(handler=on_di1_change, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)

while True:
    print("------------")

    # print all IOs names and value
    for pin in io.all():
        print("{} = {}".format(pin.name(), pin()))
        
    # print voltage and raw ADC value read from AV3 
    print("AV3 = {}V ({})".format(io.AV3(), io.AV3.read_u16()))
    
    # ramp up AO1 from 0V to 10V
    ao1V += 0.5
    if (ao1V > 10):
        ao1V = 0
    io.AO1(ao1V)
    
    # toggle DO1
    io.DO1.toggle()
    
    # if AI4 reads higher than 10mA close DO2, open otherwise
    if io.AI4() > 10:
        io.DO2(1)
    else:
        io.DO2.off()

    time.sleep(1)
