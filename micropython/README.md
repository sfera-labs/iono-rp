# Iono RP MicroPython

Here you find a utility library and examples to program your Iono RP with MicroPython.

For details on how to set up the MicroPython environment, refer to the [Raspberry Pi Pico Python SDK documentation](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf).

## Quick start

Follow these steps to run the MicroPython examples using the Thonny IDE from your host computer connected to Iono RP via USB.

- Download and install [Thonny](https://thonny.org/)
- Download the content of this repository to your computer
- Open Thonny and from the Files view (menu *View* > *Files*) navigate to the downloaded "micropython" folder
- Click on the bottom-right corner of the Thonny window to select "MicroPython (Raspberry Pi Pico)" as interpreter
- Unplug Iono RP from any power source (main power supply and USB cable)
- Connect the USB cable to Iono RP while holding the BOOTSEL button, then release the BOOTSEL button
- Click on the Stop sign button in the top bar of Thonny
- A pop-up will ask you to install MicroPython, go ahead and proceed with the installation
- In the Files view you will now see a "Raspberry Pi Pico" section showing the files uploaded to Iono RP
- From the Files view right-click on the "lib" folder, select "Upload to /" and wait for the upload to finish
- Double-click on one of the example files to open it in the main editor
- Press on the "Play" (&#9658;) button in the top bar of Thonny to run the example on your Iono RP

![iono-rp-micropython-thonny](https://user-images.githubusercontent.com/6586434/129718440-782360e6-1c07-43a6-9974-849b64ec1c5f.png)

## Module `iono` documentation

The `iono` module provides for the following:

### Class `IO` - I/O control

Instantiate an `IO` object to initialize and control Iono's input and ouput pins.

`IO(i1=IO.MODE_D, i2=IO.MODE_D, i3=IO.MODE_D, i4=IO.MODE_D)`

The `i1` ... `i4` parameters define how to initialize the multimode inputs, allowed values are:
- `IO.MODE_D`: digital mode (DIn)
- `IO.MODE_V`: analog voltage mode (AVn)
- `IO.MODE_I`: analog current mode (AIn)

The `IO` instance has the following attributes representing the available I/O pins:

- `DO1`, `DO2`, `DO3`, `DO4`: digital (relay) outputs
- `DI1`, `DI2`, `DI3`, `DI4`, `DI5`, `DI6`: digital inputs
- `DI5_BYP`, `DI6_BYP`: digital TTL level I/O lines
- `AV1`, `AV2`, `AV3`, `AV4`: analog voltage inputs
- `AI1`, `AI2`, `AI3`, `AI4`: analog current inputs
- `AO1`: analog voltage output

For multimode inputs, depending on the initialization parameters passed to the `IO` constructor, only the attributes corresponding to the selected modes will be available.

The method `all()` returns a list with all available pins.

All pin attributes have the `name()` method returning the name of the pin as string.

#### Digital (relay) outputs - DOn
The `DO1` - `DO4` attributes are instances of the [`machine.Pin`](https://docs.micropython.org/en/latest/library/machine.Pin.html) class, initialized in output mode.

#### Digital inputs - DIn
The `DI1` - `DI6` attributes are instances of the [`machine.Pin`](https://docs.micropython.org/en/latest/library/machine.Pin.html) class, initialized in input mode.

#### Digital TTL I/O lines - DIn_BYP
The `DI5_BYP` and `DI6_BYP` attributes are instances of the [`Pin`](https://docs.micropython.org/en/latest/library/machine.Pin.html). Must be initialized as input or output, calling their `init(mode)` method.

#### Analog voltage inputs - AVn
The `AV1` - `AV4` attributes are instances of the [`machine.ADC`](https://docs.micropython.org/en/latest/library/machine.ADC.html) class, extended with the `read_V()` (or equivalent `__call__()`) method, which returns the ADC value converted to voltage (V).

#### Analog current inputs - AIn
The `AI1` - `AI4` attributes are instances of the [`machine.ADC`](https://docs.micropython.org/en/latest/library/machine.ADC.html) class, extended with the `read_mA()` (or equivalent `__call__()`) method, which returns the ADC value converted to current (mA).

#### Analog voltage output - AO1
The `AO1` attribute is an instance of the [`machine.PWM`](https://docs.micropython.org/en/latest/library/machine.PWM.html) class, extended with the `duty_V([value])` (or equivalent `__call__([value])`) method, which sets (`value` argument specified) or gets (no `value` argument) the voltage value (V) on AO1, by setting or reading the corresponding duty cycle of the PWM.

### RS-485 serial interface

The `iono` module defines the `RS485` object, which is a wrapper of the [UART](https://docs.micropython.org/en/latest/library/machine.UART.html) instance connected to Iono's RS-485 interface.

The available methods are those of the [UART class](https://docs.micropython.org/en/latest/library/machine.UART.html#methods), plus the `txen(enable)` method which controls the TX-enable line. Call `RS485.txen(True)` before writing data and call `RS485.txen(False)` before incoming data is expected.
