# Documentation #
Official Documentation:
https://www.aqmd.gov/docs/default-source/aq-spec/resources-page/plantower-pms5003-manual_v2-3.pdf

Necessary uncommon imports pip commands are found on the line they are imported in.
(THIS IMAGE IS NOT THE EXACT SENSOR, BUT THEY ARE THE SAME AT A GLANCE, just for reference)
![Alt Text](https://m.media-amazon.com/images/I/71+cgzmX+pL._AC_SX679_.jpg)



# Personal Knowledge #
For this code run: python3 pm25_simpletest.py 
this will default to USB0 of your computer, and you will get a warning as well.

If you have multiple sensors or its just on another port use:
python3 pm25_simpletest.py /dev/ttyUSB#

The # is the port it is on.


BELOW ARE IMAGES ON HOW WE WIRE THEM (not for everyone):
![image](https://github.com/MOVEUAS/Sensor_Code/assets/117048000/d1159ea7-c33e-477f-a33f-659150fc29de)
![image](https://github.com/MOVEUAS/Sensor_Code/assets/117048000/ca50b5bd-99b6-46cc-95a3-b07300ec5d48)
