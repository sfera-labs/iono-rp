from iono import RS485
import time

RS485.init(baudrate=9600)
RS485.txen(False)

while True:
    line = RS485.readline()
    if line:
        print(line)
        RS485.txen(True)
        RS485.write(line)
        RS485.txen(False)
