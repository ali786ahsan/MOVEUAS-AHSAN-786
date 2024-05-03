#Created by: Kaleb Nails, Erik Liebergall, Marc Compere
#created : 10/6/2023
#modified: 13 Dec 2023
#from time import sleep
import sys
from usbiss.spi import SPI
import opcng as opc
import os
import time
import signal
import subprocess
from datetime import datetime # datetime.now()


#this is a slightly ugly way to make sure the while loops are killed and the program can exit propperly
global DataLoop
global InitializeLoop
InitializeLoop = True
DataLoop = True

# This is to handle interuptions and turn the alphasense
def handle_interrupt(signal, frame):
    global DataLoop
    global InitializeLoop
    print("Ctrl+C pressed. Performing cleanup or other actions...")

    #exits the while loops
    DataLoop = False
    InitializeLoop = False
    time.sleep(.5)
    dev.off()
    print('sensor off')
    exit(0)  # Terminate the script gracefully

signal.signal(signal.SIGINT, handle_interrupt)


device='/dev/ttyACM0'
#device='/dev/ttyUSB1'



if len(sys.argv)==1:
    #print('sys.argv[0]={0}'.format(sys.argv[0]))
    print('provide a device name to read, like:')
    print('    python3 pm25_SPS30_Senirion_Run.py /dev/ttyACM0' +"\n")
    print('\033[91mWARNING: DEFAULT PORT WILL BE ACM0\033[0m' +"\n")
    print('this default setting was left for developement' + "\n" + "\n")
    time.sleep(2.5)



if len(sys.argv)>1:
    print('using command line arg, and provided device!')
    device=sys.argv[1]


#setting up more sensor stuff from the library
spi = SPI(device)
spi.mode = 1
spi.max_speed_hz = 500000
spi.lsbfirst = False

#This loop initializes the sensor and should only run at the start
while InitializeLoop == True:
    try:
        #This detects which model of opc and prints the relevent data
        dev = opc.detect(spi)
        # print(type(dev))
        print(f'device information: {dev.info()}')
        print(f'serial: {dev.serial()}')

        #this just formats the serial number string to look better
        SerialNumberStr = str(dev.serial())
        SerialNumberStr = SerialNumberStr.replace("N3","N3-")
        SerialNumberStr = SerialNumberStr.replace(" ","")

        print(f'firmware version: {dev.serial()}')
        print('sucessfully connected to device')
        break

    except Exception as e:
        print('ERROR connecting to sensor, trying again........')
        print(e)
        time.sleep(1)


#This exits one directory at a time so its on the local computer so you dont get csvs on your repository
os.chdir("..")
os.chdir("..")

#This creates the file and the first row and and the labels
fname = '{0}_Alphasense_{1}.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S"), SerialNumberStr)
file = open(fname,'w')
titleStr = 'Serial Number,Date Label, Dates (YMD), Bin 0, Bin 1, Bin 2, Bin 3, Bin 4, Bin 5, Bin 6, Bin 7, Bin 8, Bin 9, Bin 10, Bin 11, Bin 12, Bin 13, Bin 14, Bin 15, Bin 16, Bin 17, Bin 18, Bin 19, Bin 20, Bin 21, Bin 22, Bin 23, Bin1 MToF,Bin3 MToF,Bin5 MToF,Bin7 MToF,Sampling Period,SFR,Temperature C,Relative humidity,PM1 ug/m3,PM2.5 ug/m3,PM10 ug/m3,#RejectGlitch,#RejectLongTOF,#RejectRatio,#RejectOutOfRange,Fan rev count,Laser status,Checksum'
file.write(titleStr  +"\n")
file.flush()
dev.on()

#This loop controls data collection
while DataLoop ==True:
    try:
       # query particle mass readings
        time.sleep(1)
        #print(dev.pm())
        recorded_data = dev.histogram()
        print(recorded_data)

        dataStr = ', {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23},\
		             {24}, {25}, {26}, {27},\
					 {28}, {29}, {30}, {31},\
					 {32}, {33}, {34}, \
					 {35}, {36}, {37}, {38}, {39}, {40}, {41}'.format(
		recorded_data.get('Bin 0', ''),
		recorded_data.get('Bin 1', ''),
		recorded_data.get('Bin 2', ''),
		recorded_data.get('Bin 3', ''),
		recorded_data.get('Bin 4', ''),
		recorded_data.get('Bin 5', ''),
		recorded_data.get('Bin 6', ''),
		recorded_data.get('Bin 7', ''),
		recorded_data.get('Bin 8', ''),
		recorded_data.get('Bin 9', ''),
		recorded_data.get('Bin 10', ''),
		recorded_data.get('Bin 11', ''),
		recorded_data.get('Bin 12', ''),
		recorded_data.get('Bin 13', ''),
		recorded_data.get('Bin 14', ''),
		recorded_data.get('Bin 15', ''),
		recorded_data.get('Bin 16', ''),
		recorded_data.get('Bin 17', ''),
		recorded_data.get('Bin 18', ''),
		recorded_data.get('Bin 19', ''),
		recorded_data.get('Bin 20', ''),
		recorded_data.get('Bin 21', ''),
		recorded_data.get('Bin 22', ''),
		recorded_data.get('Bin 23', ''),
		recorded_data.get('Bin1 MToF', ''),         # 24
		#recorded_data.get('Bin2 MToF', ''),
		recorded_data.get('Bin3 MToF', ''),         # 25
		#recorded_data.get('Bin4 MToF', ''),
		recorded_data.get('Bin5 MToF', ''),         # 26
		#recorded_data.get('Bin6 MToF', ''),
		recorded_data.get('Bin7 MToF', ''),         # 27
		
		recorded_data.get('Sampling Period', ''),   # 28
		recorded_data.get('SFR', ''),               # 29
		recorded_data.get('Temperature', ''),       # 30
		recorded_data.get('Relative humidity', ''), # 31
		
		recorded_data.get('PM1', ''),               # 32 (ug/m3), datasheet pdf page 13
		recorded_data.get('PM2.5', ''),             # 33 (ug/m3)
		recorded_data.get('PM10', ''),              # 34 (ug/m3)
		
		recorded_data.get('#RejectGlitch', ''),     # 35
		recorded_data.get('#RejectLongTOF', ''),    # 36
		recorded_data.get('#RejectRatio', ''),      # 37
		recorded_data.get('#RejectOutOfRange', ''), # 38
		recorded_data.get('Fan rev count', ''),     # 39
		recorded_data.get('Laser status', ''),      # 40
		recorded_data.get('Checksum', ''))          # 41

        dateStr =', Date:, {0}'.format(datetime.now())

        print("\n" + SerialNumberStr + dateStr + dataStr + "\n")
        file.write(SerialNumberStr + dateStr + dataStr + "\n")
        file.flush()

    except BaseException as e:
        print(e)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

