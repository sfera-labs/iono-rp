'''
Iono RP example: using the RS-485 interface

Simple example that echoes back the received text lines through
Iono RP's RS-485 interface (connected to the RP2040's UART)

Copyright (C) 2021 Sfera Labs S.r.l. - All rights reserved.

For information, see:
http://www.sferalabs.cc/

This code is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
See file LICENSE.txt for further informations on licensing terms.
'''

from iono import RS485

# initialize the port with given baudrate and timeouts
RS485.init(baudrate=9600, timeout=500, timeout_char=100)

# Unset TX-enable line to get ready to receive data
RS485.txen(False)

while True:
    line = RS485.readline()
    if line:
        RS485.txen(True) # Set TX-enable line before sending response 
        RS485.write(line)
        RS485.txen(False)
