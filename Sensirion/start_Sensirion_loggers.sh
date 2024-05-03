#!/bin/bash -x 
#
# bash shell script to start multiple logger codes
#
# mdc
# created : 13 Dec 2023
# modified: 13 Dec 2023

device1='/dev/ttyUSB0'
device2='/dev/ttyUSB1'

DATE=`date`
echo "starting sensirion1 logger at $DATE"
screen -dm -S sen1 python3 SPS30_Senirion_Run.py $device1

echo "starting sensirion2 logger"
screen -dm -S sen2 python3 SPS30_Senirion_Run.py $device2


 

