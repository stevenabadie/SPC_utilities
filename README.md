= Statistical Process Control Utilities =

This repository is a collection of utilities for processing and plotting statistical process control data. 


=== Control Chart ===

python control_chart.py path/to/csv/file.csv

Use the sample_control_chart.csv template to generate a correctly formatted csv.
* Column 1 is a legend for the Config column
* Config column is used to fill in the correct fields and labels
* All following columns should be used for data with the first row set as the name of the data set. The exact column name should then be used in the config column to set the axis or control limits.

|           | Config    | Diameter  | UCL
| --------- | --------- | --------- | ------
|Chart title| Title	    | 2.0       | 10
|X-axis     |           | 2.2       | 10
|Y-axis 1   | Diamater  | 2.1       | 10
|Y-axis 2   |           | 2.05      | 10	
|Y-axis 3	|           | 2.4       | 10
|Y-axis 4	|           | 2.6       | 10
|UCL	    | UCL       | 2.3       | 10
|LCL	    |           | 2.2       | 10
|X label	| Sample    | 2.0       | 10
|Y label	| Diameter  | 2.2       | 10

