# Iono RP C/C++

The [Raspberry Pi Pico SDK](https://github.com/raspberrypi/pico-sdk) provides all the resources needed to program Iono RP in C, C++.     With low level API as well as higher level utilities, the SDK can be used to build anything from simple applications, to fully fledged runtime environments.

The "iono_pins.h" file you find here is a simple header file you can include in your code, containing the #defines to easily map Iono's I/Os to the corresponding RP2040 GPIOs and ADC channels, to be used as parameters for the standard SDK functions, e.g.:

```
...
gpio_init(IONO_PIN_DO1);
gpio_set_dir(IONO_PIN_DO1, GPIO_OUT);
gpio_put(IONO_PIN_DO1, 1);
...
```

```
...
adc_gpio_init(IONO_PIN_AV1);
adc_select_input(IONO_ADC_IN_AV1);
...
```
