# postprocessing_point_monitors

trial_all_csv_plots.py: Python file to plot x vs y plot for all the csv/out files available in a given folder.
Structure of the files should be: 

"point18-rfile"
"Time Step" "point18 etc.."
("Time Step" "point18" "flow-time")
0 0 0
1 2.733302703356435e-241 0.01
2 0 0.02
3 0 0.03
4 0 0.04
5 0 0.05
6 0 0.06 
....

Where, the first three lines (headers) would be deleted. The thrid column (flow time) is x, the second column (point 18) is y. Accordingly x vs y is plotted and saved. 
If there are additional columns in any file in the folder, the code will read all files and all columns and then delete additional columns to main consistency of 3 columns. 
