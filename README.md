# postprocessing_point_monitors<br />

Folders 1 and 2 contain point monitors generated from Ansys Fluent simulations (these are sample files containing).<br />


Sructure of folders is as follows: <br />
**Main_Folder** <br />
    _Subfolder_1_ <br />
      -->File_1 <br />
      -->File_2 <br />
      -->....<br />
      -->File_n<br />
    _Subfolder_2_<br />
      -->File_1<br />
      -->File_2<br />
      -->....<br />
      -->File_n<br />

Sructure of files is as follows: <br /> 
"point18-rfile" <br />
"Time Step" "point18 etc.." <br />
("Time Step" "point18" "flow-time") <br />
0 0 0 <br />
1 2.733302703356435e-241 0.01 <br />
2 0 0.02 <br />
3 0 0.03 <br />
4 0 0.04 <br />
5 0 0.05 <br />
6 0 0.06 <br />
.... <br />

**trial_all_csv_plots.py**: Python file to plot x vs y plot for all the csv/out files available in a given folder. <br />
Where, the first three lines (headers) would be deleted. The thrid column (flow time) is x, the second column (point 18) is y. Accordingly x vs y is plotted and saved. 
If there are additional columns in any file in the folder, the code will read all files and all columns and then delete additional columns to main consistency of 3 columns. <br />

**trial_2.py**: Python file to concatenate files of same name placed in different folders, e.g., point18.out, point19.out, .... consisting continuous data, e.g., point18.out in folder 1 contains data from t=0 sec to t= 2 sec, point18.out in folder 2 contains data from t=2.1 sec to t = 50 sec, and so on. After concatenation, a new file would be generated with the name point18.out_concatenated.csv  <br />

**dup_removal.py**: Python file to remove duplicate rows from 'n' number of .csv files in a folder. <br />


