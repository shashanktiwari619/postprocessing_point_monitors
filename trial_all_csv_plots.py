# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:38:39 2023

@author: Shashank.S.Tiwari
"""

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the folder path where the CSV files are located
folder_path = 'C:/Users/Shashank.S.Tiwari/OneDrive - Shell/Simulations/SUF_PearlGTL/40per_800TPH/16ppm_900secs/'

# Get a list of all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, '*.out'))

# Set the DPI value for the plot (adjust as needed)
dpi = 300

# Set font options
font_size = 14
font_family = 'Arial'

# Set color palette
color_palette = 'viridis'  # Choose a color palette of your preference

# Set seaborn style
sns.set(style='ticks')

# Loop through each CSV file
for file in csv_files:
    # Read the CSV file and skip the first three lines
    df = pd.read_csv(file, delimiter=' ', skiprows=3, header=None)
    
    # Check the number of columns in the DataFrame
    if df.shape[1] == 4:
        # If there are four columns, drop the fourth column
        df = df.drop(columns=[3])
    
    # Assign column names
    df.columns = ['Time Step', 'Concentration', 'Flow-Time']
    
    # Convert 1.6e-5 concentration to desired amount
    df['Concentration'] *= 5.4
    
    # Convert concentration to ppm
    df['Concentration'] *= 1e6
    
    # Convert flow-time to hours
    df['Flow-Time'] /= 3600
    
    # Find the index where concentration reaches 16 ppm
    exposure_start = df[df['Concentration'] >= 16].iloc[0]['Flow-Time']
    exposure_end = df[df['Concentration'] >= 16].iloc[-1]['Flow-Time']

    # Calculate exposure duration
    exposure_duration = exposure_end - exposure_start
    
    # Generate the plot
    plt.plot(df['Flow-Time'], df['Concentration'])
    
    # Add a horizontal line at concentration of 16 ppm
    plt.axhline(y=16, color='red', linestyle='--')
    
    plt.xlabel('Flow-Time (hours)', fontsize=font_size, fontfamily=font_family)
    plt.ylabel('Concentration (ppm)', fontsize=font_size, fontfamily=font_family)
    plt.title('Flow-Time vs Concentration', fontsize=font_size, fontfamily=font_family)
    
    # Set font options for tick labels
    plt.xticks(fontsize=font_size-2, fontfamily=font_family)
    plt.yticks(fontsize=font_size-2, fontfamily=font_family)

    # Set x-axis limits
    plt.xlim(0, 12)
    plt.ylim(0, 50)

    # Set color palette
    sns.set_palette(color_palette)

    # Set seaborn style
    sns.set_style('ticks')
    
    # Find the position for the text within the plot
    text_x = exposure_start + (exposure_duration / 2)
    text_y = 16 + (max(df['Concentration']) - 16) / 3
    
    # # Check if the text position is too close to the curve
    # if text_y < max(df['Concentration']):
    #     text_y += (max(df['Concentration']) - text_y) / 5
    
    # Add the exposure duration as text on the plot
    text_to_show = f"16 ppm Exposure for {exposure_duration:.2f} hours"
    plt.text(3.8, 20, text_to_show, fontsize=10,fontfamily=font_family,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9))
    
    
    # Save the plot as a PNG image
    file_name = os.path.splitext(os.path.basename(file))[0] + '.png'
    save_path = os.path.join(folder_path, file_name)
    plt.savefig(save_path, dpi=dpi)
    
    # Close the plot
    plt.close()
