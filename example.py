#Tested on ESP32-WROOM-32D running ESP32_GENERIC-20250809-v1.26.0.bin

import utime
import random
from machine import Pin, DAC
from esp32_dac import esp32_dac # dictionary {step:volt} {int:float}

DAC_CHAN1 = Pin(26)
#DAC_CHAN2 = Pin(25)

# Initialise the DAC
dac = DAC(DAC_CHAN1)

# Cycle output voltage from min to max
for step in range(0,256):
    print(f"DAC output step: {step}")
    dac.write(step)
    utime.sleep(0.02)

# Verify step voltages
print("Running random DAC step checks, verify with instrument")
step = 0
while (step<=255):       
    print(f"DAC step {step} expects {esp32_dac[step]:.3f}V")
    dac.write(step)
    utime.sleep(5)
    step += random.randint(1,25)

# Hit a target voltage with DAC
target_voltage = 1.45

# Invert the dictionary so we can search voltages for the step needed
esp32_dac_inverted = {value: key for key, value in esp32_dac.items()} # type {voltage:step}

# Find the closest voltage match in available DAC voltages
closest_key = min(esp32_dac_inverted.keys(), key=lambda key: abs(key - target_voltage))

# Equate this to the step
step = esp32_dac_inverted[closest_key]

# Set the DAC
dac.write(step)
print(f"Target voltage: {target_voltage}V DAC step: {step} DAC volt: {esp32_dac[step]}V ABS Error: {abs(target_voltage - esp32_dac[step])}")

# *** WARNING ***
# Don't forget to power cycle device if you need to rerun or do a machine.reset()
# This is a problem as DAC channel can't be reinitialised presently in Micropython code 


