# Project 1 FYS3150, Anders P. Åsbø
import os
import timeit as time

import numpy as np
import scipy.linalg as sp

import data_generator as gen

dir = os.path.dirname(os.path.realpath(__file__))


def main():
    """Program uses LU-decomposition to solve Au=g"""

    # getting dimensions of matrix, and labeling data:
    global N
    N = int(eval(input("Give value for N: ")))
    name = "LUtest%i" % int(np.log10(N))

    # generating data:
    x = np.linspace(0, 1, N)
    h = (x[-1] - x[0]) / N
    gen.generate_data(x, name)
    g = np.loadtxt("%s/data_files/%s.dat" % (dir, name)) * h ** 2

    A = np.zeros((N, N))  # creating zero matrix.
    A = Afunc(A)  # populating the three diagonals.

    start = time.default_timer()  # timing solve.
    LU, piv = sp.lu_factor(A)  # decomp and forward sub.
    u = sp.lu_solve((LU, piv), g)  # backward sub.
    end = time.default_timer()
    print("Time spent on LU %g" % (end - start))  # printing elapsed time.

    # saving numerical solution:
    np.savetxt("%s/data_files/solution_%s.dat" % (dir, name), u, fmt="%g")


def Afunc(A):
    """Function that populates tridiagonal matrix with 2 along diagonal,
    and -1 as the non-zero, off-diagonal elements."""
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i, j] = 2
            elif i == j + 1:
                A[i, j] = -1
            elif j == i + 1:
                A[i, j] = -1

    return A


if __name__ == '__main__':
    main()

# example run:
"""
$ python3 LUdecomp.py
Give value for N: 1e4
Time spent on LU 6.23319
"""
# data is saved to files.
