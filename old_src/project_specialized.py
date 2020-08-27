# Project 1 FYS3150, Anders P. Åsbø
import os
import timeit as time

import matplotlib.pyplot as plt
import numpy as np

import data_generator as gen


def main():
    """Program solves matrix equation Au=f, using decomposition, forward
    substitution and backward substitution, for a Toeplitz, NxN matrix A."""
    init_data()  # initialising data

    # performing decomp. and forward and backward sub.:
    decomp_and_forward_and_backward_sub()

    save_sol()  # saving numerical solution in "data_files" directory.

    plot_solutions()  # plotting numerical solution vs analytical solution.

    plt.show()  # displaying plot.


def init_data():
    """Initialising data for program as global variables."""
    global dir, N, name, x, h, anal_sol, u, d, d_prime, a, b, g, g_prime
    dir = os.path.dirname(os.path.realpath(__file__))  # current directory.

    # defining number of rows and columns in matrix:
    N = int(eval(input("Specify number of data points N: ")))
    # defining common label for data files:
    name = input("Label of data-sets without file extension: ")

    x = np.linspace(0, 1, N)  # array of normalized positions.
    h = (x[0] - x[-1]) / N  # defining step-siz.

    gen.generate_data(x, name)  # generating dataanal_name set.
    anal_sol = np.loadtxt("%s/data_files/anal_solution_for_%s.dat" %
                          (dir, name))

    u = np.empty(N)  # array for unkown values.
    s = np.arange(1, N + 1)
    d_prime = 2 * (s) / (2 * (s + 1))  # pre-calculating the 1/d_prime factors.
    f = np.loadtxt("%s/data_files/%s.dat" % (dir, name))
    g = f * h ** 2
    g_prime = np.empty(N)  # array for g after decomp. and sub.


def decomp_and_forward_and_backward_sub():
    """Function that performs the matrix decomposition and forward
    and backward substitution."""
    # setting boundary conditions:
    u[0], u[-1] = 0, 0
    g_prime[0] = g[0]
    start = time.default_timer()
    for i in range(1, len(u)):  # performing decomp. and forward sub.
        g_prime[i] = g[i] + g_prime[i - 1] * d_prime[i - 1]

    for i in reversed(range(1, len(u) - 1)):  # performing backward sub.
        u[i] = (g_prime[i] + u[i + 1]) * d_prime[i - 1]

    end = time.default_timer()
    print("Time spent on loop %g" % (end - start))


def save_sol():
    """Function for saving numerical solution in data_files directory
    with prefix "solution"."""
    path = "%s/data_files/solution_%s.dat" % (dir, name)
    np.savetxt(path, u, fmt="%g")


def plot_solutions():
    """Function for plotting numerical vs analytical solutions."""
    x_prime = np.linspace(x[0], x[-1], len(anal_sol))

    plt.figure()
    plt.plot(x, u, label="Numerical solve")
    plt.plot(x_prime, anal_sol, label="Analytical solve")
    plt.title("Integrating with a %iX%i tridiagonal matrix" % (N, N))
    plt.xlabel(r"$x \in [0,1]$")
    plt.ylabel(r"$u(x)$")
    plt.legend()
    plt.grid()


if __name__ == '__main__':
    main()

# example run:
"""
$ python3 project.py
Specify number of data points N: 1000
Label of data-sets without file extension: opti1000x1000
"""
# a plot is displayed, and the data is saved to the data_files directory.
