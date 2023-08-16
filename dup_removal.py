# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 01:31:01 2023

@author: Shashank.S.Tiwari
"""

import os
import pandas as pd

# Specify the input folder containing CSV files
input_folder = 'C:/Users/Shashank.S.Tiwari/OneDrive - Shell/Simulations/SUF_PearlGTL/800TperHr/900sec1e-5/k0_075/'

# Specify the output folder to save new CSV files
output_folder = 'C:/Users/Shashank.S.Tiwari/OneDrive - Shell/Simulations/SUF_PearlGTL/800TperHr/900sec1e-5/k0_075/'

# List all files in the input folder
csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

# Process each CSV file
for i, csv_file in enumerate (csv_files, start=1):
    input_file_path = os.path.join(input_folder, csv_file)
    output_file_path = os.path.join(output_folder, csv_file)
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file_path, sep=' ')
    
    duplicated_values = df.iloc[:, 0][df.iloc[:, 0].duplicated()]
    duplicated_count = duplicated_values.count()
    print(f"Duplicated values in file {i}: {duplicated_count}")
    
    # Drop duplicate rows
    df_unique = df.drop_duplicates(subset=df.columns[0])
       
    # Save the unique rows to a new CSV file
    df_unique.to_csv(output_file_path,sep=' ', index=False)

print("Duplicated rows removed and unique rows saved.")
