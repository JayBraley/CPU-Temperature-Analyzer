# CPU Temp Analyzer

## Description
This program accepts a set of CPU temperature readings from each CPU core. For each core, the following is generated:

- A piecewise linear interpolation
- A global linear least squares approximation

## Requirements

-Python 3.7+

## Input Library
The input library being used is an input helper written in Python by Thomas J. Kennedy, designed as an assist
in reading the raw CPU temperature input data.

## Data Preprocessing
The input data is organized as several list data structures, one containing time intervals, and another
containing collections of readings for each CPU core.
For example, data for 4 CPU cores at 2 different times would be stored as follows:

~~~
times = [0, 30]
core_readings = [[61, 81],[57, 91],[39, 70],[68, 45]]
~~~

# Sample Execution & Output	
This program must run with one command line argument, the source data file. The analyst is not prompted for
any additional information. For each CPU core, a .txt file of processed data is produced.

An example of a valid program command is

~~~			
cpu_temp_analyzer.py input-file.txt
~~~

with the contents of input-file.txt being

~~~
61.0 63.0 50.0 58.0
80.0 81.0 68.0 77.0
62.0 63.0 52.0 60.0
83.0 82.0 70.0 79.0
68.0 69.0 58.0 65.0
~~~

and would produce 4 .txt files, one being

~~~
0 <= x <=       30 ; y =      61.0000 +       0.6333 x ; interpolation
30 <= x <=       60 ; y =      98.0000 +      -0.6000 x ; interpolation
60 <= x <=       90 ; y =      20.0000 +       0.7000 x ; interpolation
90 <= x <=      120 ; y =     128.0000 +      -0.5000 x ; interpolation
0 <= x <=      120 ; y =      67.4000 +       0.0567 x ; least-squares
~~~