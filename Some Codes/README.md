## GitHub Created and Managed By: Kaleb Nails ##

# Air Quality Sensor Repository
This repository contains code for different air quality sensors. Each directory represents a specific sensor model, and the code within each directory is tailored to that sensor. Authors listed are immediate authors to our club, of course a lot of this code is found from other online, and the are cited within the programs files themselves.

To pip install the dependent libraries run:
   ```bash
   pip install -r requirements.txt
``` 
Also I have made some YouTube tutorials. They explain some simple things and issues you might run into. I will continue to update as the need arises.
https://youtube.com/playlist?list=PLwAqsBL94ygYDSl61qIoNLhPo3zRYZZli&si=xE07LIelMbSo7oQt

## 📝 File Structure 
```text
📦Sensor_Code
 ┣ 📂Alphasense
 ┃ ┣ 📄OPC_Simple_v2.py
 ┃ ┣ 📄README.md
 ┃ ┗ 📄start_Alphasense_loggers.sh
 ┣ 📂PMS plantower
 ┃ ┣ 📄.gitkeep
 ┃ ┣ 📄README.md
 ┃ ┣ 📄 pm25_simpletest.py
 ┃ ┗ 📄start_Plantower_loggers.sh
 ┣ 📂Post_Processing
 ┃ ┣ 📄Post_Processing.py
 ┃ ┗ 📄README.md
 ┣ 📂Sensirion
 ┃ ┣ 📄.gitkeep
 ┃ ┣ 📄 README.md
 ┃ ┣ 📄SPS30_Senirion_run.py
 ┃ ┣ 📄exampleReadSPS30.py
 ┃ ┣ 📄sps30.py
 ┃ ┣ 📄start_Sensirion_loggers.sh
 ┃ ┗ 📄stop_Sensirion_loggers.sh
 ┣ 📂Viasala
 ┃ ┗ 📄.gitkeep
 ┣ 📄Alphasense_Start_Script.sh
 ┣ 📄Sensor_Start_Script.sh
 ┣ 📄gui_popup.py
 ┣ 📄requirements.txt
 ┣ 📄.gitnore
 ┣ 📄sensor_UART_configs.json
 ┗ 📄README.md
```
# Sensor Models #

## ALPHASENSE OPC
![image](https://github.com/MOVEUAS/Sensor_Code/assets/117048000/2488073d-5645-47d8-9b6e-21c8f2c8ef74)

**Authors:** Kaleb Nails, Erik Liebergall, Marc Compere  
**Created:** 10/6/2023  

### Description
This directory contains code for the ALSPHASENSE air quality sensor. The main script, `OPC_Simple_v2.py`, interfaces with the sensor, reads data, and logs it to a CSV file. This is using the USB adaptor for the Alphasenses

### Instructions
1. Connect the ALSPHASENSE sensor to your system.
2. Run the `pm25_SPS30_Senirion_Run.py` script with the appropriate device name as a command-line argument (default is `/dev/ttyACM0`).
   ```bash
   python3 pm25_SPS30_Senirion_Run.py /dev/ttyUSB0
   
The script will log air quality data to a CSV file with a timestamp.


## PMS plantower
![image](https://github.com/MOVEUAS/Sensor_Code/assets/117048000/e1553597-c06a-49dd-b361-26345a3ea2d6)

**Authors:** Erik Liebergall, Leah Smith, Kaleb Nails, Marc Compere  
**Created:** 10 Feb 2023  

### Description
This directory contains code for the PMS plantower air quality sensor. The `pm25_simpletest.py` script interfaces with the sensor, reads data, and outputs air quality information to the console.

### Instructions
1. Connect the PMS plantower sensor to your system.
2. Run the `pm25_simpletest.py` script with the appropriate device name as a command-line argument (default is `/dev/ttyUSB0`).
   ```bash
   python3 pm25_simpletest.py /dev/ttyUSB0

### Output
The script provides air quality measurements in both standard and environmental concentration units. Below is an example output:

```plaintext
Concentration Units (Standard)
---------------------------------------
PM 1.0: 10   PM 2.5: 15   PM 10: 20

Concentration Units (Environmental)
---------------------------------------
PM 1.0: 8    PM 2.5: 12   PM 10: 16
---------------------------------------
Particles > 0.3um / 0.1L air: 1000
Particles > 0.5um / 0.1L air: 800
Particles > 1.0um / 0.1L air: 500
Particles > 2.5um / 0.1L air: 200
Particles > 5.0um / 0.1L air: 100
Particles > 10um / 0.1L air: 50
```

## Sensirion SPS30
**Authors:** Erik Liebergall, Marc Compere, Kaleb Nails  
**Created:** 13 Oct 2023

![image](https://github.com/MOVEUAS/Sensor_Code/assets/117048000/af3127f4-a29f-4fac-9898-43c5310545e8)

### Description
This directory contains code for the Sensirion SPS30 air quality sensor. The `pm25_SPS30_Senirion_Run.py` script interfaces with the sensor, reads data, and logs air quality information to a CSV file.

### Instructions
1. Connect the Sensirion SPS30 sensor to your system.
2. Run the `pm25_SPS30_Senirion_Run.py` script with the appropriate device name as a command-line argument (default is `/dev/ttyUSB0`).
   ```bash
   python3 pm25_SPS30_Senirion_Run.py /dev/ttyUSB0
The script will continuously read data from the sensor and log it to a CSV file.

# CSV File Format
Note these are subject to change are are up to date as off 1/26/2024

## AlphaSense CSV File Format
The script outputs air quality information to a CSV file. The CSV format includes the following columns:
- **Serial Number**
- **Date Label**
- **Dates (YMD)**
- **Bin 0 to 23**
- **Bin1 MToF to Bin7 MToF**
- **Sampling Period**
- **SFR**
- **Temperature C**
- **Relative humidity**
- **PM1 ug/m³**
- **PM2.5 ug/m³**
- **PM10 ug/m³**
- **#RejectGlitch**
- **#RejectLongTOF**
- **#RejectRatio**
- **#RejectOutOfRange**
- **Fan rev count**
- **Laser status**
- **Checksum**

Each row in the CSV file represents a set of air quality measurements at a specific date and time, with corresponding values for each parameter.

## PMS plantower CSV File Format
The script outputs air quality information to a CSV file. The CSV format includes the following columns:

- **Date Label**
- **Dates (YMD)**
- **Sensor 1**
- **pm1.0 standard ug/m³**
- **pm2.5 standard ug/m³**
- **pm10.0 standard ug/m³**
- **pm1.0 env ug/m³**
- **pm2.5 env ug/m³**
- **pm10.0 env ug/m³**
- **particles 0.3um**
- **particles 0.5um**
- **particles 1.0um**
- **particles 2.5um**
- **particles 5.0um**
- **particles 10.0um**

Each row in the CSV file represents a set of air quality measurements at a specific date and time, with corresponding values for each parameter.

## SENSIRION CSV File Format ##
The script outputs air quality information to a CSV file. The CSV format includes the following columns:
- **Serial Number**
- **Date Label**
- **Dates (YMD)**
- **Mass Concentration PM1.0 (µg/m³)**
- **Mass Concentration PM2.5 (µg/m³)**
- **Mass Concentration PM4.0 (µg/m³)**
- **Mass Concentration PM10.0 (µg/m³)**
- **Number Concentration PM0.5 (#/cm³)**
- **Number Concentration PM1.0 (#/cm³)**
- **Number Concentration PM2.5 (#/cm³)**
- **Number Concentration PM4.0 (#/cm³)**
- **Number Concentration PM10.0 (#/cm³)**
- **Typical Particle Size [µm]**
Each row in the CSV file represents a set of air quality measurements at a specific date and time, with corresponding values for each parameter.








