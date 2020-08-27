# create data set for numerical testing, Ander P. Åsbø
import os

import numpy as np

dir = os.path.dirname(os.path.realpath(__file__))


def main():
    """Generates a set of test-data, if run individually."""
    test_generate_data()


def generate_data(x, name):
    """Function that generates a set of u''(x) data, as well as the
    corresponding, analytical u(x). The data is saved to text"""
    data = 100 * np.exp(-10 * x)
    path = "%s/data_files/%s.dat" % (dir, name)
    np.savetxt(path, data, fmt="%g")

    """
    # interpolated analytical solution used when plotting:
    x_prime = np.linspace(x[0], x[-1], 1000)
    analytical_solution = 1-(1-np.exp(-10))*x_prime-np.exp(-10*x_prime)
    """

    analytical_solution = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x)
    analytical_solution[0], analytical_solution[-1] = 0, 0
    anal_name = "%s/data_files/anal_solution_for_%s.dat" % (dir, name)
    np.savetxt(anal_name, analytical_solution, fmt="%g")


def test_generate_data():
    """Generates test data if run as stand-alone program."""
    x = np.linspace(0, 1, 1001)
    test_name = "Test_data"
    generate_data(x, test_name)


if __name__ == '__main__':
    main()

# example run:
"""
$ python3 data_generator.py
"""
# the test-data files are sucessfully generated.
