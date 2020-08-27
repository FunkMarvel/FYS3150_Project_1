# Project 1 FYS3150, Anders P. Åsbø.
import os

import numpy as np


def main():
    """This program calculates the log10 of the relative error for
    different data sets generated with "project_specialized.py", and saves
    it in a textfile table with the log10 of the step-size."""

    dir = os.path.dirname(os.path.realpath(__file__))
    name = input("Label data: ")
    # preping arrays:
    N = np.array([10, 100, 1000, 10000, 100000, 1000000, 10000000])
    h = np.empty(len(N))
    epsilon = np.empty(len(N))

    for i in range(len(N)):  # reading data from files:
        u_num = np.loadtxt("%s/data_files/solution_%s%i.dat"
                           % (dir, name, 1 + i))
        u_anal = np.loadtxt("%s/data_files/anal_solution_for_%s%i.dat"
                            % (dir, name, 1 + i))

        h[i] = np.log10(1 / len(u_num))  # calculating log 10 of step-size.

        # calculating log10 of relative error:
        err = np.abs((u_num[1:-2] - u_anal[1:-2]) / u_anal[1:-2])
        epsilon[i] = np.max(np.log10(err))

        """
        # used to extract the array that gave
        # RuntimeWarning: divide by zero encountered in log10
        if i == 5:
            np.savetxt("dad.dat", err, fmt="%e")
            break
        """

    # saving the results
    table = np.empty((len(N), 2))
    table[:, 0] = h
    table[:, 1] = epsilon
    np.savetxt("%s/data_files/error_table_%s.dat" % (dir, name), table,
               fmt="%g")


if __name__ == '__main__':
    main()

# example run:
"""
$ python3 erroranlaysis.py
Label data: test
erroranlaysis.py:27: RuntimeWarning: divide by zero encountered in log10
  epsilon[i] = np.max(np.log10(err))
"""
# table of log10 of stepsizes, and max errors is saved to file
