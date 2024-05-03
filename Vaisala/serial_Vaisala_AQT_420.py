#!/usr/bin/env python3
#
# read Vaisala AQT-420 air quality and particulate matter sensor
#
# 'minicom -s' works with suggestions here: https://help.ubuntu.com/community/Minicom
# set HW flow control=OFF
#
# exit minicom: ctrl-A, then x
#
# what works: minicom with 115200/8N1, hw flow control=OFF
# then: date
#       meas
#       $ meas                                  
#       NO2 (ppm): 0.012
#       SO2 (ppm): 0.023
#       CO (ppm): 0.310
#       O3 (ppm): -0.002
#       PM2.5 (ug/m3): 0.7
#       PM10 (ug/m3): 1.9
#       TEMP (C): 21.5
#       HUM (%RH): 46.1
#       PRES (mbar): 1016.2
#       Uptime (s): 1802374
#       Validity: TRUE
#       
#       meas --csv
#       0.012,0.023,0.308,0.000,0.000,0.000,0.000,0.000,0.7,1.9,21.5,45.9,1016.3,1802444
#       
#       
#
# ------------------------------------------------------------------------------
# MODBUS example that has not worked because it's unclear how MODBUS on AQT-420 works over usb cable:
# from: https://medium.com/@peterfitch/modbus-and-rs485-a-python-test-rig-1b5014f709ec
#
# Marc Compere, comperem@erau.edu
# created : 04 Jan 2020
# modified: 20 Apr 2023
# modified by David Benning, Erik, Gabe, Leah, Kaleb:  20 Jan 2023
#Thoughts and Prayers
#modified by Kaleb: 20 April 2023

# this got it started:
#   ser.write('meas\r')
#   while True:
#       res=ser.read_until()
#       print(res)

import time # sleep()
from datetime import datetime # datetime.now()
import serial
import os 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import socket

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
ser = serial.Serial('/dev/ttyUSB1', baudrate=115200, bytesize=8, parity='N', stopbits=1)

ser.reset_input_buffer() #  flush input buffer
ser.reset_output_buffer() # flush output buffer, more may be in usb adapter which is separate from linux buffer
ser.timeout=2 # (s) timeout for serial.read_until()

class myDataClass:
    NO2      = -1.0 # (ppm)
    SO2      = -1.0 # (ppm)
    CO       = -1.0 # (ppm)
    O3       = -1.0 # (ppm)
    PM2pt5   = -1.0 # (ug/m3)
    PM10     = -1.0 # (ug/m3)
    TEMP     = -1.0 # (C)
    HUM      = -1.0 # (%RH)
    PRES     = -1.0 # (mbar)
    Uptime   = -1.0 # (s)
    Validity = -1.0 # (True/False)

data = myDataClass()

fname='{0}_vaisala_aqt420.csv'.format( datetime.now().strftime("%Y_%m_%d__%H_%M_%S") )
folder = '1-ZUsOWRls8vGFxDhgCK5cudBqNecKI-d'
file1 = drive.CreateFile({'parents':[{'id':folder}],'title' : fname})

file=open(fname,'w')

dt=10 # (sec) measurement request interval
cnt=0

print('Reading serial device: Vaisala AQT-420...')
print('logging to [{0}] every {1} seconds'.format(fname,dt))
print('\nPress Crtl-C to quit...')

while True:
    #print('[{0}] --- requesting measurement ---'.format(datetime.now()))
    nBytes = ser.write(b'meas\r') # write these bytes to the AQT-420, note: the \r does the trick (it's the return)
    done=False # not done yet
    while done==False:
        res=ser.read_until() # returns byte arrays upto newline:
        #print(res)
        # b'NO2 (ppm): 0.011\r\n'
        # b'SO2 (ppm): 0.020\r\n'
        # b'CO (ppm): 0.248\r\n'
        # b'O3 (ppm): 0.000\r\n'
        # b'PM2.5 (ug/m3): 1.9\r\n'
        # b'PM10 (ug/m3): 2.8\r\n'
        # b'TEMP (C): 22.1\r\n'
        # b'HUM (%RH): 43.6\r\n'
        # b'PRES (mbar): 1015.6\r\n'
        # b'Uptime (s): 1806282\r\n'
        # b'Validity: TRUE\r\n'
        # b'\r\n'
        myStr=res.decode('utf-8')
        if len(myStr)>5:
            if myStr.find('NO2')>=0: # myStr='NO2 (ppm): 0.011\r\n'
                (desc,val) = myStr.strip().split(':')
                data.NO2 = float(val)
                
            if myStr.find('SO2')>=0: # myStr='SO2 (ppm): 0.020\r\n'
                (desc,val) = myStr.strip().split(':')
                data.SO2 = float(val)
                
            if myStr.find('CO')>=0: # myStr='CO (ppm): 0.248\r\n'
                (desc,val) = myStr.strip().split(':')
                data.CO = float(val)
                
            if myStr.find('O3')>=0: # myStr='O3 (ppm): 0.000\r\n'
                (desc,val) = myStr.strip().split(':')
                data.O3 = float(val)
                
            if myStr.find('PM2.5')>=0: # myStr='PM2.5 (ug/m3): 2.3\r\n'
                (desc,val) = myStr.strip().split(':')
                data.PM2pt5 = float(val)
                
            if myStr.find('PM10')>=0: # myStr='PM10 (ug/m3): 2.8\r\n'
                (desc,val) = myStr.strip().split(':')
                data.PM10 = float(val)
                
            if myStr.find('TEMP')>=0: # myStr='TEMP (C): 22.1\r\n'
                (desc,val) = myStr.strip().split(':')
                data.TEMP = float(val)
                
            if myStr.find('HUM')>=0: # myStr='HUM (%RH): 43.6\r\n'
                (desc,val) = myStr.strip().split(':')
                data.HUM = float(val)
                
            if myStr.find('PRES')>=0: # myStr='PRES (mbar): 1015.6\r\n'
                (desc,val) = myStr.strip().split(':')
                data.PRES = float(val)
                
            if myStr.find('Uptime')>=0: # myStr='Uptime (s): 1806282\r\n'
                (desc,val) = myStr.strip().split(':')
                data.Uptime = float(val)
                
            if myStr.find('Validity')>=0: # myStr='Validity: TRUE\r\n'
                (desc,val) = myStr.strip().split(':')
                data.Validity = bool(val)
                done=True # exit this measurement string parsing loop
                #print('done={0}'.format(done))
    
    # print 1 complete line composed of all values just decoded
    dateStr='{0},  cnt=,{1},  '.format(datetime.now(),cnt)
    dataStr='NO2 (ppm),{0:>12.3f},  SO2 (ppm),{1:>12.3f},  CO (ppm),{2:>12.3f},  O3 (ppm),{3:>12.3f},  PM2.5 (ug/m3),{4:>12.3f},  PM10 (ug/m3),{5:>12.2f},  TEMP (C),{6:>8.2f},  HUM (%),{7:>8.1f},  PRES (mbar),{8:>10.2f},  Uptime (s),{9:>12.2f},  Validity,{10}' \
            .format(data.NO2,data.SO2,data.CO,data.O3,data.PM2pt5,data.PM10,data.TEMP,data.HUM,data.PRES,data.Uptime,data.Validity)
    print(dateStr + dataStr)
    
    # just in case these formatting choices delete information, tack on the identical but raw floating point values as a long string at the end in the file only
    file.write(dateStr + dataStr + ',raw values,' + ','.join([ str(elem) for elem in [data.NO2,data.SO2,data.CO,data.O3,data.PM2pt5,data.PM10,data.TEMP,data.HUM,data.PRES,data.Uptime,data.Validity] ]) + '\n' )
    file.flush()

    file1.SetContentFile(fname)

    try:
        #Try to send data to bokeh table over sockets
        ServerAddress = ('169.254.26.44',2222)
        bufferSize = 1024
        #This is fine for now, change if there are multiple vaisalas
        devName = 'Vaisala0'
        UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Msg_to_bokeh_str ='"Sensors":"' + devName + '","NO2 (ppm)":"{0:>12.3f}",  "SO2 (ppm)":"{1:>12.3f}",  "CO (ppm)":"{2:>12.3f}",  "O3 (ppm)":"{3:>12.3f}",  "PM2.5 (ug/m3)":"{4:>12.3f}",  "PM10 (ug/m3)":"{5:>12.2f}",  "TEMP (C)":"{6:>8.2f}",  "HUM (%)":"{7:>8.1f}",  "PRES (mbar)":"{8:>10.2f}",  "Uptime (s)":"{9:>12.2f}",  "Validity":"{10}"'.format(data.NO2,data.SO2,data.CO,data.O3,data.PM2pt5,data.PM10,data.TEMP,data.HUM,data.PRES,data.Uptime,data.Validity)
        Msg_to_bokeh_str = '{' + Msg_to_bokeh_str + '}'
        Msg_to_bokeh_bytes = Msg_to_bokeh_str.encode('utf-8')
        UDPClient.sendto(Msg_to_bokeh_bytes,ServerAddress)




    except Exception as e:
        print(e)
        pass

    
    try:
        #upload to Google Drive
        file1.Upload()
    except:
        print('No internet connection. Drive upload Failed')
        pass


    time.sleep(dt)
    cnt=cnt+1

    #file1.Upload()

