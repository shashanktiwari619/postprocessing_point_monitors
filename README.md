# postprocessing_point_monitors

**trial_all_csv_plots.py**: Python file to plot x vs y plot for all the csv/out files available in a given folder.
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



**trial_2.py**: Python file to concatenate files of same name placed in different folders, e.g., point18.out, point19.out, .... consisting continuous data, e.g., point18.out in folder 1 contains data from t=0 sec to t= 2 sec, point18.out in folder 2 contains data from t=2.1 sec to t = 50 sec, an so on. After concatenation, a new file would be generated with the name point18.out_concatenated.csv  
