#!/bin/bash

alpha0_device="/dev/ttyACM0"
echo "Starting alpha0 logger"
screen -dm -S alpha0 python3 OPC_Simple_v2.py $alpha0_device

alpha1_device="/dev/ttyACM1"
echo "Starting alpha1 logger"
screen -dm -S alpha1 python3 OPC_Simple_v2.py $alpha1_device

alpha2_device="/dev/ttyACM2"
echo "Starting alpha2 logger"
screen -dm -S alpha2 python3 OPC_Simple_v2.py $alpha2_device

