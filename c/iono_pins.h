/*
  Iono RP pins definitions header file

    Copyright (C) 2021 Sfera Labs S.r.l. - All rights reserved.

    For information, see the iono web site:
    http://www.sferalabs.cc/

  This code is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.
  See file LICENSE.txt for further informations on licensing terms.
*/

#ifndef _IONO_PINS_H
#define _IONO_PINS_H

// Digital (relay) outputs

#define IONO_PIN_DO1 13
#define IONO_PIN_DO2 12
#define IONO_PIN_DO3 11
#define IONO_PIN_DO4 10

// Multi-mode inputs

#define IONO_PIN_DI1 26
#define IONO_PIN_AV1 26
#define IONO_PIN_AI1 26
#define IONO_ADC_IN_AV1 0
#define IONO_ADC_IN_AI1 0

#define IONO_PIN_DI2 27
#define IONO_PIN_AV2 27
#define IONO_PIN_AI2 27
#define IONO_ADC_IN_AV2 1
#define IONO_ADC_IN_AI2 1

#define IONO_PIN_DI3 28
#define IONO_PIN_AV3 28
#define IONO_PIN_AI3 28
#define IONO_ADC_IN_AV3 2
#define IONO_ADC_IN_AI3 2

#define IONO_PIN_DI4 29
#define IONO_PIN_AV4 29
#define IONO_PIN_AI4 29
#define IONO_ADC_IN_AV4 3
#define IONO_ADC_IN_AI4 3

// Digital inputs / TTL I/O

#define IONO_PIN_DI5 24
#define IONO_PIN_DI5_BYP 7

#define IONO_PIN_DI6 23
#define IONO_PIN_DI6_BYP 6

// Analog output

#define IONO_PIN_AO1 8

// RS-485 serial interface

#define IONO_PIN_RS485_TX 16
#define IONO_PIN_RS485_RX 17
#define IONO_PIN_RS485_TXEN_N 25 // drive low to enable transmission

#endif
