#Created by Kaleb Nails, Ahsan Ali


import pandas as pd
import os
from datetime import datetime
import numpy as np




def Process(df):

    #print(list(df.keys())[0])
    column_length= len(list(df.values())[0].keys())    
    print(f"each sensor has {column_length} columns")

    # Create column headers based on the number of sensors
    columns = [
        f"{col}_{i}"
        for i in range(len(df))
        for col in df[list(df.keys())[0]].keys()
    ]       
    #print(columns)
    new_column = []

    #new_column += [element for name in columns for element in columns if name[:-2] in element] this might do it in one line but i dont care
    #print(new_column)

    #reoganize you columns
    for name in columns:
 
        #print(name[:-2])
        result = [element for element in columns if name[:-2] in element]
        new_column += result #it was in a double matrix in a matrix, this stops it from being that way
 
    new_column = np.unique(new_column) #I need the unique, is the easiest way to removing some duplicates I accidentally created
    print(f"\nthe new organized column is \n {new_column}")
    columns = new_column 

    # Create an empty DataFrame with the specified columns
    result = pd.DataFrame(columns=columns)

    # Iterate over the sensor data
    sensor_count = 0
    for df_name, df_data in df.items():
        # Iterate over the columns in the sensor data
        #print(f"df_data {df_name} is:{df_data}")
        
        for col in df_data.keys():
            # Append columns from each sensor to the interleaved_columns list
            result[f"{col}_{sensor_count}"] = df_data[col]
        sensor_count = sensor_count + 1
        
        
    #print(result)
    result.to_csv(f"{datetime.now().strftime('%Y_%m_%d')}_{list(df.keys())[0][:-2]}.csv", index=False)
    print(f"Saved {datetime.now().strftime('%Y_%m_%d')}_{list(df.keys())[0][:-2]}.csv")
    return result



#define initial variables
Sensirion_df = {}
Sensirion_count = 0

plantower_df = {}
plantower_count = 0

Alphasense_df = {}
Alphasense_count = 0

#Go to the directory above it to look for the csv's
current_dir = os.path.abspath(os.curdir)
parent_dir = os.path.dirname(current_dir)

for filename in os.listdir(parent_dir):
    if os.path.isfile(os.path.join(parent_dir, filename)) and filename.endswith(".csv"):

        if "Sensirion" in filename:
            print("Sensirion file being read:", filename)
            df_name = f"Sensirion_{Sensirion_count}"
            Sensirion_count += 1
            Sensirion_df[df_name] = pd.read_csv(os.path.join(parent_dir, filename))

            #Below is hard coded column headers I am just deleting
            Sensirion_df[df_name].drop(columns=['Date Label'], inplace=True)
            
        elif "plantower" in filename:
            print("plantower file being read:", filename)
            df_name = f"Plantower_{plantower_count}"
            plantower_count += 1
            plantower_df[df_name] = pd.read_csv(os.path.join(parent_dir, filename))

            #remove extra columns:
            plantower_df[df_name].drop(columns=['Date Label', ' Sensor 1'], inplace=True)

        elif "Alphasense" in filename:
            print("Alphasense file being read:", filename)
            df_name = f"Alphasense_{Alphasense_count}"
            Alphasense_count += 1
            Alphasense_df[df_name] = pd.read_csv(os.path.join(parent_dir, filename))

            #print(Alphasense_df[df_name].keys())

            #remove extra columns:
            Alphasense_df[df_name].drop(columns=['Date Label'," Bin 0", " Bin 1", " Bin 2", " Bin 3", " Bin 4", " Bin 5", " Bin 6", " Bin 7"," Bin 8", " Bin 9", " Bin 10", " Bin 11", " Bin 12", " Bin 13", " Bin 14", " Bin 15"," Bin 16", " Bin 17", " Bin 18", " Bin 19", " Bin 20", " Bin 21", " Bin 22", " Bin 23"," Bin1 MToF", "Bin3 MToF", "Bin5 MToF", "Bin7 MToF", "Sampling Period", "SFR", "Checksum", "Fan rev count","Laser status",'#RejectGlitch','#RejectLongTOF','#RejectOutOfRange','#RejectRatio'], inplace=True)

#This runs post processing if the files exist, this a simple solution
if Sensirion_count > 0:
    print("\n\033[1;31m" + "Processing Sensirion:" + "\033[0m")
    Process(Sensirion_df)

if plantower_count > 0:
    print("\n\033[1;31m" + "Processing plantower:" + "\033[0m")
    Process(plantower_df)

if Alphasense_count > 0:
    print("\n\033[1;31m" + "Processing Alphasense:" + "\033[0m")
    Process(Alphasense_df)
