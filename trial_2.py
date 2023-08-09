# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:07:42 2023

@author: Shashank.S.Tiwari
"""

import os
import csv

def concatenate_csv_files(main_folder):
    csv_files = {}
    for subdir, _, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.out'):
                csv_path = os.path.join(subdir, file)
                csv_basename = os.path.basename(csv_path)
                csv_folder_name = os.path.basename(os.path.dirname(csv_path))
                
                if csv_basename not in csv_files:
                    csv_files[csv_basename] = []

                with open(csv_path, 'r', newline='') as input_csvfile:
                    csv_reader = csv.reader(input_csvfile)
                    # Skip 3 header lines
                    for _ in range(3):
                        try:
                            next(csv_reader)
                        except StopIteration:
                            break

                    data = []
                    for row in csv_reader:
                        data.append(",".join(row))  # Combine columns with space separation

                    csv_files[csv_basename].append(('\n'.join(data)))  # Concatenate lines with newline

    # Write concatenated data to new CSV files for each unique basename
    for csv_basename, data_list in csv_files.items():
        output_file = os.path.join(main_folder, f"{csv_basename}_concatenated.csv")
        with open(output_file, 'w', newline='') as output_csvfile:
            output_csvfile.write('\n'.join(data_list))

if __name__ == "__main__":
    main_folder = "C:/Users/Shashank.S.Tiwari/OneDrive - Shell/Simulations/SUF_PearlGTL/8hours/"

    concatenate_csv_files(main_folder)
    print("CSV files have been concatenated and saved.")