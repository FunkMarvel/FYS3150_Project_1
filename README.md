# FYS3150_Project_1
Project 1, FYS3150

To test run the project try
```console
$ python3 data_analysis.py plot
```
## Usage:
The python 3 script "data_analysis.py" builds and runs the cpp implementations of the Thomas' algorithm, and LU-decomposition. The script takes in 3 optional command line arguments (see below). The command line arguments can be mixed and matched in any order:
```console
$ python3 data_analysis.py 4 plot error
```
```console
$ python3 data_analysis.py error plot
```
```console
$ python3 data_analysis.py plot 7 error
```
### Optional arguments:
##### The largest $n$ for which to run the algorithms.
  * If you provide an integer $i$, the script will run the algorithms for every power of ten from $n = 10^{1}$ to $n = 10^{i}$.
  * $n = 10^{3}$ if no integer is provided on the command line.
  * Example running algorithms for $n = 10^{1}, 10^{2}, 10^{3}, 10^{4}$:
  ```console
  $ python3 data_analysis.py 4
  ```

##### plot
  * Using the "plot" keyword will plot the numerical and analytical solutions from the general Thomas' algorithm.
  * This plots for every value of $n$.
  * If the keyword is not provided, no plots will be generated.
  * Example plotting for $n = 10^{1}, 10^{2}, 10^{3}$:
  ```console
  $ python3 data_analysis.py plot
  ```

##### error
  * Using the "error" keyword will calculate the $\log_{10}$ relative error for the general and special algorithms, and save the results to a file "errortable.dat" together with the $\log_{10}$ of the corresponding $\log_{10}$ of the step size $h$.
  * If the keyword is not provided, no file "errortable.dat" will be generated.
  * Example generating "errortable.dat" $n = 10^{1}, 10^{2}, 10^{3}$:
  ```console
  $ python3 data_analysis.py error
  ```

## Using the cpp program directly
If you wish, you can build the cpp executable by running:
```console
$ make all
```
The executable can then be run from command line with $n$ as a command line argument:
```console
$ ./main.exe [n]
```
The data from the run will be saved to binary files "x[n].bin", and "u_[solver][n].bin". To clean up data binaries, run:
```console
$ make cleanbin
```
To clean up all executables, object-files and binaries, run:
```console
$ make clean
```
