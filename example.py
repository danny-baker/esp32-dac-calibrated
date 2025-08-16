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


# *** WARNING ***
# Don't forget to power cycle device if you need to rerun or do a machine.reset()
# This is a problem as DAC channel can't be reinitialised presently in Micropython code 


