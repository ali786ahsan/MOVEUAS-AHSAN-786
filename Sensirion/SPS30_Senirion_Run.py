#Kaleb Nails
# Moral Support: Erik Liebergall
#10/11/2023
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
# Erik Liebergall
# Marc Compere
# Kaleb Nails
# created : 13 Oct 2023

from sps30 import get_usb
from sps30 import SPS30
import time
from datetime import datetime
import os
import sys


device='/dev/ttyUSB0'
#device='/dev/ttyUSB1'



if len(sys.argv)==1:
    #print('sys.argv[0]={0}'.format(sys.argv[0]))
    print('provide a device name to read, like:')
    print('    python3 pm25_SPS30_Senirion_Run.py /dev/ttyUSB0' +"\n")
    print('\033[91mWARNING: DEFAULT PORT WILL BE USB0\033[0m' +"\n")
    print('this default setting was left for developement' + "\n" + "\n")
    time.sleep(2.5)



if len(sys.argv)>1:
    print('using command line arg, and provided device!')
    device=sys.argv[1]

devName=os.path.basename(device) # get device name for logfile name
print('using devName=[{0}]'.format(devName)+"\n")

p = SPS30(port=device, push_mqtt=False)

SerialNumberStr = p.read_serial_number()
print(SerialNumberStr)



#This exits one directory at a time so its on the local computer so you dont get csvs on your repository
os.chdir("..")
os.chdir("..")

#This creates the file and the first row and and the labels
fname = '{0}_Sensirion_sps30_{1}.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S"), SerialNumberStr)
file = open(fname,'w')
titleStr = 'Serial Number,Date Label, Dates (YMD), Mass Concentration PM1.0 (µg/m³),Mass Concentration PM2.5 (µg/m³),Mass Concentration PM4.0 (µg/m³),Mass Concentration PM10.0 (µg/m³),Number Concentration PM0.5 (µg/m³),Number Concentration PM1.0 (#/cm³),Number Concentration PM2.5 (#/cm³),Number Concentration PM4.0(#/cm³),Number Concentration PM10.0 (#/cm³),Typical Particle Size [µm]'
file.write(titleStr  +"\n")
file.flush()



p.start()
#p.stop()

#This sleep is very important
print(' \n LOADING... \n')
time.sleep(5)



while True:

    #read values
    out=p.read_values()
    print(out)
    #data_struct = {'Mass Concentration PM1.0 (µg/m³)',out[0],'Mass Concentration PM2.5 (µg/m³)',out[1],'Mass Concentration PM4.0 (µg/m³)',out[2],'Mass Concentration PM10.0 (µg/m³)',out[3],'Number Concentration PM0.5 (µg/m³)',out[4],'Number Concentration PM1.0 (µg/m³)',out[5],'Number Concentration PM2.5 (µg/m³)',out[6],'Number Concentration PM4.0(µg/m³)',out[7],'Number Concentration PM10.0 (µg/m³)',out[8],'Typical Particle Size [µm]',out[9]}
    #dataStr = '{0}, {1}, {2}, {3}, {4},{5},{6},{7},{7},{8},{9}'.format(data_struct.get('Mass Concentration PM1.0 (µg/m³)',''),data_struct.get('Mass Concentration PM2.5 (µg/m³)',''),data_struct.get('Mass Concentration PM10.0 (µg/m³)',''),data_struct.get('Mass Concentration PM1.0 (µg/m³)',''),
    dataStr = ', {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7},{8},{9}'.format(out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7],out[8],out[9])
    dateStr =', Date:, {0}'.format(datetime.now())


    print("\n" + SerialNumberStr + dateStr + dataStr + "\n")
    file.write(SerialNumberStr + dateStr + dataStr + "\n")
    file.flush()
    time.sleep(1)


# docStr.append('Mass Concentration PM1.0 (µg/m³)')
# docStr.append('Mass Concentration PM2.5 (µg/m³)')
# docStr.append('Mass Concentration PM4.0 (µg/m³)')
# docStr.append('Mass Concentration PM10.0 (µg/m³)')
# docStr.append('Number Concentration PM0.5 [#/cm³]')
# docStr.append('Number Concentration PM1.0 [#/cm³]')
# docStr.append('Number Concentration PM2.5 [#/cm³]')
# docStr.append('Number Concentration PM4.0 [#/cm³]')
# docStr.append('Number Concentration PM10.0 [#/cm³]')
# docStr.append('Typical Particle Size [µm]')
