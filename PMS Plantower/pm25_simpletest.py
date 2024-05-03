# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#
# Adafruit PM2.5 device, which is Plantower PMS5003 PM sensor:
#   https://learn.adafruit.com/pm25-air-quality-sensor/python-and-circuitpython
#   https://docs.circuitpython.org/projects/pm25/en/latest/api.html#adafruit-pm25-uart
# Original pm25_simpletest.py:
#   https://github.com/adafruit/Adafruit_CircuitPython_PM25/blob/main/examples/pm25_simpletest.py
#
# Adafruit product: https://www.adafruit.com/product/3686
# Plantower PMS5003 Datasheet: https://cdn-shop.adafruit.com/product-files/3686/plantower-pms5003-manual_v2-3.pdf
#
# Erik Liebergall, lieberg@my.erau.edu
# Leah Smith, smithl73@my.erau.edu
# Kaleb Nails, nailsk@my.erau.edu
# Marc Compere, comperem@erau.edu
# created : 10 Feb 2023
# modified: 11 Oct 2023

"""
Example sketch to connect to PM2.5 sensor with either I2C or UART.
"""

# pylint: disable=unused-import


import time
import board
import busio #pip3 install adafruit-blinka
import os
import sys
from datetime import datetime # datetime.now()
from digitalio import DigitalInOut, Direction, Pull
#from adafruit_pm25.i2c import PM25_I2C

# For use with USB-to-serial cable:
import serial

# go back 2 directories to store CSV's
os.chdir("..")
os.chdir("..")

reset_pin = None
# If you have a GPIO, its not a bad idea to connect it to the RESET pin
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direction = Direction.OUTPUT
# reset_pin.value = False


# For use with a computer running Windows:
# import serial
# uart = serial.Serial("COM30", baudrate=9600, timeout=1)

# For use with microcontroller board:
# (Connect the sensor TX pin to the board/computer RX pin)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
# import serial
# uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)


dev1='/dev/ttyUSB0'
devLabel = 'unlabeled'
# dev2='/dev/ttyUSB2'


if len(sys.argv)==1:
    #print('sys.argv[0]={0}'.format(sys.argv[0]))
    print('provide a device name to read, like:')
    print('    python3 pm25_simpletest.py /dev/ttyUSB0' +"\n")
    print('\033[91mWARNING: DEFAULT PORT WILL BE USB0\033[0m' +"\n")
    print('this default setting was left for developement' + "\n" + "\n")
    time.sleep(2.5)


if len(sys.argv)>1:
    print('using command line arg, and provided device!')
    dev1=sys.argv[1]

# Plantower does not report unique serial number, so must label reporting device on the command line
if len(sys.argv)>2:
    devLabel=sys.argv[2]
    print('using command line arg 2, device label: {}'.format(devLabel)) # make this match the handwritten label using the cmd line arg #2

devName=os.path.basename(dev1) # get device name for logfile name
print('using devName=[{0}]'.format(devName))


uart = serial.Serial(dev1, baudrate=9600, timeout=0.25)
# uart2 = serial.Serial(dev2, baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART #pip3 install adafruit-circuitpython-pm25
pm25 = PM25_UART(uart, reset_pin)
# pm25_2 = PM25_UART(uart2, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)
#fname = '{0}_pm25_simplest_plantower_CSV.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S") )
fname = '{0}_pm25_simplest_plantower_{1}_CSV.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S"),devLabel ) # <-- handwritten label (not usb device)

file = open(fname,'w')

print("Found PM2.5 sensor, reading data...")

#adds heading columns
#Add Labels to the top of the file TEST this works
titleStr = 'Date Label, Dates (YMD), Sensor 1, pm1.0 standard ug/m3, pm2.5 standard ug/m3, pm10.0 standard ug/m3, pm1.0 env ug/m3, pm2.5 env ug/m3, pm10.0 env ug/m3,particles 0.3um, particles 0.5um, particles 1.0um, particles 2.5um, particles 5.0um, particles 10.0um'#, Dates (YMD), Sensor 2, pm10 standard, pm25 standard, pm100 standard, pm10 env, pm25 env, pm100 env,particles 03um, particles 05um, particles 10um, particles 25um, particles 50um, particles 100um'
file.write(titleStr  +"\n")
file.flush()



while True:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print(f"TIME: {time.strftime('%H:%M:%S', time.localtime())}")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
    dateStr1 =', Date:, {0}'.format(datetime.now())

# while False:
    #time.sleep(1)

    # try:
    #     aqdata2 = pm25_2.read()
    #     # print(aqdata)
    # except RuntimeError:
    #     print("Unable to read from sensor, retrying...")
    #     continue

    # print()
    # print("Concentration Units (standard)")
    # print("---------------------------------------")
    # print(
    #     "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
    #     % (aqdata2["pm10 standard"], aqdata2["pm25 standard"], aqdata2["pm100 standard"])
    # )
    # print("Concentration Units (environmental)")
    # print("---------------------------------------")
    # print(
    #     "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
    #     % (aqdata2["pm10 env"], aqdata2["pm25 env"], aqdata2["pm100 env"])
    # )
    # print("---------------------------------------")
    # print("Particles2 > 0.3um / 0.1L air:", aqdata2["particles 03um"])
    # print("Particles2 > 0.5um / 0.1L air:", aqdata2["particles 05um"])
    # print("Particles2 > 1.0um / 0.1L air:", aqdata2["particles 10um"])
    # print("Particles2 > 2.5um / 0.1L air:", aqdata2["particles 25um"])
    # print("Particles2 > 5.0um / 0.1L air:", aqdata2["particles 50um"])
    # print("Particles2 > 10 um / 0.1L air:", aqdata2["particles 100um"])
    # print("---------------------------------------")

    # dateStr2 =', Date:, {0}'.format(datetime.now())
    #dataStr1 = ', Data1:, {0}, {1}, {2}, {3}, {4}, {5}'.format(aqdata["particles 03um"],aqdata["particles 05um"],aqdata["particles 10um"],aqdata["particles 25um"],aqdata["particles 50um"],aqdata["particles 100um"])
    #dataStr2 = ', Data2:, {0}, {1}, {2}, {3}, {4}, {5}'.format(aqdata2["particles 03um"],aqdata2["particles 05um"],aqdata2["particles 10um"],aqdata2["particles 25um"],aqdata2["particles 50um"],aqdata2["particles 100um"])

    dataStr1 = ' Data1:, {0}, {1}, {2},    {3}, {4}, {5},    {6}, {7}, {8}, {9}, {10}, {11}'.format( \
                    aqdata["pm10 standard"],       \
                    aqdata["pm25 standard"],       \
                    aqdata["pm100 standard"],      \

                    aqdata["pm10 env"],            \
                    aqdata["pm25 env"],            \
                    aqdata["pm100 env"],           \

                    aqdata["particles 03um"],      \
                    aqdata["particles 05um"],      \
                    aqdata["particles 10um"],      \
                    aqdata["particles 25um"],      \
                    aqdata["particles 50um"],      \
                    aqdata["particles 100um"])

    # dataStr2 = ', Data2:, {0}, {1}, {2},    {3}, {4}, {5},    {6}, {7}, {8}, {9}, {10}, {11}'.format( \
    #                 aqdata2["pm10 standard"],      \
    #                 aqdata2["pm25 standard"],      \
    #                 aqdata2["pm100 standard"],     \

    #                 aqdata2["pm10 env"],           \
    #                 aqdata2["pm25 env"],           \
    #                 aqdata2["pm100 env"],          \

    #                 aqdata2["particles 03um"],     \
    #                 aqdata2["particles 05um"],     \
    #                 aqdata2["particles 10um"],     \
    #                 aqdata2["particles 25um"],     \
    #                 aqdata2["particles 50um"],     \
    #                 aqdata2["particles 100um"])
    # file.write(dateStr1 + dataStr1 + dateStr2 + dataStr2  +"\n")

    file.write(dateStr1 + dataStr1 + "\n")
    file.flush()
