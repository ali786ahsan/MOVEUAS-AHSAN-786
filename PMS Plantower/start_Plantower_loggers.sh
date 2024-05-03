#!/bin/bash -x 
#
# bash shell script to start multiple logger codes
#
# mdc
# created : 13 Dec 2023
# modified: 13 Dec 2023

device1='/dev/ttyUSB2'
device2='/dev/ttyUSB3'
device3='/dev/ttyUSB4'
device4='/dev/ttyUSB5'

echo "starting plantower1 logger"
screen -dm -S pt1 python3 pm25_simpletest.py $device1 pt1

echo "starting plantower2 logger"
screen -dm -S pt2 python3 pm25_simpletest.py $device2 pt2

echo "starting plantower3 logger"
screen -dm -S pt3 python3 pm25_simpletest.py $device3 pt3

echo "starting plantower4 logger"
screen -dm -S pt4 python3 pm25_simpletest.py $device4 pt4

 

