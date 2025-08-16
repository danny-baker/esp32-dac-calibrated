# esp32-dac-calibrated
For Micropython applications, here are the measured voltages for the 0-255 range of the ESP32-WROOM-32D 8bit DAC. 

## Background
* The two onboard 8bit DACs are not true linear, especially at the extreme ranges.
* This (known problem) presents a challenge if you want to target an accurate voltage
* The onboard DACs use the 3.3V regulated supply voltage as a ref so in theory you should get 0-3.3V step 0-255
* In reality, it's quite different. 
* I haven't been able to find a datasheet with the actual values so I've painstakingly measured the voltage at each and every step.
* I'm sure there's variation between models and devices, but this is much better than assuming equal voltage steps of 0.012941 throughout the range (i.e. 3.3 volts / 255 steps)
* Measured on an ESP32-WROOM-32D with a Digitech QM1321 Multimeter 

## Usage
Wipe the tears of pain away and use these values in your code rather than assuming a linear relationship between 0-3.3V across the step range.

# Run
* Assume firmware installed on device and interfacing with it via `mpremote` on your PC 
* Ref: https://docs.micropython.org/en/latest/reference/mpremote.html
* Copy file to device `mpremote fs cp esp32_dac.py :esp32_dac.py`
* Run example script from ESP32 memory `mpremote run example.py`

## `esp32_dac.csv`
* A simple comma-separated-values file for general purpose use, language agnostic of type `step,voltage`

## `esp32_dac.py`
* A Python dictionary containing the measured DAC values of type `{step:voltage}` 
* This can easily be imported into your Micropython project, as demonstrated in the example.
* Or of course you could just cut-paste it directly into your code.

## `example.py`
* A simple Micropython script demonstrating usage of the onboard DAC with a few helper operations

## `machine.DAC` class is incomplete (Aug 2025)
* If you're using the onboard DAC on an ESP32 using Micropython, you'll need to use the `machine.DAC` class that ships on the firmware for your device
* Take special note that this is barebones and nowhere near as built out as the `machine.ADC` class
* In fact it's not even listed in the official docs, but it does work, see https://docs.micropython.org/en/v1.10/library/machine.html#module-machine
* Basically you only have the `write()` method and there is no `deinit()` as there is for the ADC class.
* Once the DAC is initialised it will throw an OS error next time you run your code (because internally the DAC channel apparently remains in that state)
* The only way to avoid this is to power cycle the device or do a `machine.reset()`

You're welcome :)







