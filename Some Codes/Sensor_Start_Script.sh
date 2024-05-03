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

sensirion0_device="/dev/ttyUSB0"
echo "Starting sensirion0 logger"
screen -dm -S sensirion0 python3 SPS30_Sensirion_Run.py $sensirion0_device

PMS0_device="/dev/ttyUSB3"
echo "Starting PMS0 logger"
screen -dm -S PMS0 python3 pm25_simpletest.py $PMS0_device

PMS1_device="/dev/ttyUSB4"
echo "Starting PMS1 logger"
screen -dm -S PMS1 python3 pm25_simpletest.py $PMS1_device

PMS2_device="/dev/ttyUSB5"
echo "Starting PMS2 logger"
screen -dm -S PMS2 python3 pm25_simpletest.py $PMS2_device

sensirion1_device="/dev/ttyUSB1"
echo "Starting sensirion1 logger"
screen -dm -S sensirion1 python3 SPS30_Sensirion_Run.py $sensirion1_device

PMS0_device="/dev/ttyUSB3"
echo "Starting PMS0 logger"
screen -dm -S PMS0 python3 pm25_simpletest.py $PMS0_device

PMS1_device="/dev/ttyUSB4"
echo "Starting PMS1 logger"
screen -dm -S PMS1 python3 pm25_simpletest.py $PMS1_device

PMS2_device="/dev/ttyUSB5"
echo "Starting PMS2 logger"
screen -dm -S PMS2 python3 pm25_simpletest.py $PMS2_device

sensirion2_device="/dev/ttyUSB2"
echo "Starting sensirion2 logger"
screen -dm -S sensirion2 python3 SPS30_Sensirion_Run.py $sensirion2_device

PMS0_device="/dev/ttyUSB3"
echo "Starting PMS0 logger"
screen -dm -S PMS0 python3 pm25_simpletest.py $PMS0_device

PMS1_device="/dev/ttyUSB4"
echo "Starting PMS1 logger"
screen -dm -S PMS1 python3 pm25_simpletest.py $PMS1_device

PMS2_device="/dev/ttyUSB5"
echo "Starting PMS2 logger"
screen -dm -S PMS2 python3 pm25_simpletest.py $PMS2_device

