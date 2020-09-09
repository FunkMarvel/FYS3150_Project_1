# Example run for selected results:
The following run generated the data in this directory.

```console
/FYS3150_Project_1/src$ python data_analysis.py 4 error
g++ -Wall -O2 -march=native main.cpp -c
g++ -Wall -O2 -march=native general_algorithm.cpp -c
g++ -Wall -O2 -march=native special_algorithm.cpp -c
g++ -Wall -O2 -march=native relative_error.cpp -c
g++ -Wall -O2 -march=native general_main.cpp -c
g++ -Wall -O2 -march=native special_main.cpp -c
g++ -Wall -O2 -march=native LU_main.cpp -c
g++ -Wall -O2 -march=native main.o general_algorithm.o special_algorithm.o relative_error.o general_ma
in.o special_main.o LU_main.o -o main.exe -larmadillo
General algorithm took 1e-06 seconds to finish.
Maximum (log10 of) relative error in general algorithm with 10 steps: 0.30262
Special algorithm took 1e-06 seconds to finish.
Maximum (log10 of) relative error in special algorithm with 10 steps: 0.360131
Solving with LU decomposition took 0.000391 seconds to finish.
Maximum (log10 of) relative error with the LU decomposition solver with 10 steps: 0.30262
General algorithm took 3e-06 seconds to finish.
Maximum (log10 of) relative error in general algorithm with 100 steps: 0.034263
Special algorithm took 1e-06 seconds to finish.
Maximum (log10 of) relative error in special algorithm with 100 steps: 0.0424988
Solving with LU decomposition took 0.000624 seconds to finish.
Maximum (log10 of) relative error with the LU decomposition solver with 100 steps: 0.034263
General algorithm took 2.2e-05 seconds to finish.
Maximum (log10 of) relative error in general algorithm with 1000 steps: 0.00347475
Special algorithm took 9e-06 seconds to finish.
Maximum (log10 of) relative error in special algorithm with 1000 steps: 0.00433859
Solving with LU decomposition took 0.164875 seconds to finish.
Maximum (log10 of) relative error with the LU decomposition solver with 1000 steps: 0.00347475
General algorithm took 0.000235 seconds to finish.
Maximum (log10 of) relative error in general algorithm with 10000 steps: 0.000347972
Special algorithm took 5.7e-05 seconds to finish.
Maximum (log10 of) relative error in special algorithm with 10000 steps: 0.000434783
Solving with LU decomposition took 159.658 seconds to finish.
Maximum (log10 of) relative error with the LU decomposition solver with 10000 steps: 0.000347972
rm -f *.bin
```
