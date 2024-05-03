#!/usr/bin/env python3
#
# UART interface to Sparkfun SPS-30: sparkfun.com/products/15103
# documented here:  https://binh-bk.github.io/Sensirion_SPS30/
#                   https://github.com/binh-bk/Sensirion_SPS30
#
# output format (is probably) documented in 4.3 Measurement Output Formats
# at datasheet: https://cdn.sparkfun.com/assets/4/e/e/f/8/Sensirion_PM_Sensors_Datasheet_SPS30.pdf
#
# needs paho-mqtt:
# install with:     pip3 install paho-mqtt
#
# Erik Liebergall, lieberge@my.erau.edu
# Marc Compere, comperem@erau.edu
# Kaleb Nails
# created : 02 Feb 2023
# modified: 02 Feb 2023

from sps30 import get_usb
from sps30 import SPS30
import time

device='/dev/ttyUSB0'
#device='/dev/ttyUSB1'

p = SPS30(port=device, push_mqtt=False)
print(p.read_serial_number())

docStr=[]
docStr.append('Mass Concentration PM1.0 (µg/m³)')
docStr.append('Mass Concentration PM2.5 (µg/m³)')
docStr.append('Mass Concentration PM4.0 (µg/m³)')
docStr.append('Mass Concentration PM10.0 (µg/m³)')
docStr.append('Number Concentration PM0.5 [#/cm³]')
docStr.append('Number Concentration PM1.0 [#/cm³]')
docStr.append('Number Concentration PM2.5 [#/cm³]')
docStr.append('Number Concentration PM4.0 [#/cm³]')
docStr.append('Number Concentration PM10.0 [#/cm³]')
docStr.append('Typical Particle Size [µm]')

for i in range(len(docStr)):
    print('{0}, '.format(docStr[i]), end='')

p.start()
#p.stop()

#This sleep is very important
print(' \n LOADING... \n')
time.sleep(5)
while True:

    out=p.read_values()
    for i in range(len(out)):
       print('{0}, '.format(out[i]), end='')
    print('')
    time.sleep(1)
