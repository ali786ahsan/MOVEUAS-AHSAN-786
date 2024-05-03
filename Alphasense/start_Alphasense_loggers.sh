#!/bin/bash -x 
#
# bash shell script to start multiple logger codes
#
# mdc
# created : 13 Dec 2023
# modified: 13 Dec 2023

alpha1_device='/dev/ttyACM0'
alpha2_device='/dev/ttyACM1'

echo "starting alpha1 logger"
screen -dm -S alpha1 python3 OPC_Simple_v2.py $alpha1_device

echo "starting alpha2 logger"
screen -dm -S alpha2 python3 OPC_Simple_v2.py $alpha2_device


 

