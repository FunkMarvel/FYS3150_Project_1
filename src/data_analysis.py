from subprocess import call, run
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def main():
    """
    This program solves Poisson's eq with thomas algorithm
    and lu decomposition in cpp, and plots the result against
    an analytic solution.
    """
    mpl.rcParams.update({"text.usetex": True})  # using latex.

    N = np.array([10, 100, 1000])  # array of N values.
    call(["make"])  # compiling any changed cpp files.
    for i in N:
        run(["./main.exe", f"{i}"])  # running algorithms for each N.

        # reading data from file:
        x = np.fromfile(f"x{i}.bin")
        u_anal = np.fromfile(f"u_anal{i}.bin")
        u_special = np.fromfile(f"u_special{i}.bin")
        u_general = np.fromfile(f"u_general{i}.bin")
        u_LUdecomp = np.fromfile(f"u_LUdecomp{i}.bin")

        # plotting each numerical solve vs analytic solve:
        plt.figure()
        plt.plot(x, u_anal, label="analytic solution")
        plt.plot(x, u_general, label="numerical solution")
        plt.xlabel("$x$")
        plt.ylabel("$f(x)$")
        plt.title(f"Numerical integration using general algorithm, N = {i}")
        plt.legend()
        plt.grid()

        plt.figure()
        plt.plot(x, u_anal, label="analytic solution")
        plt.plot(x, u_special, label="numerical solution")
        plt.xlabel("$x$")
        plt.ylabel("$f(x)$")
        plt.title(f"Numerical integration using special algorithm, N = {i}")
        plt.legend()
        plt.grid()

        plt.figure()
        plt.plot(x, u_anal, label="analytic solution")
        plt.plot(x, u_LUdecomp, label="numerical solution")
        plt.xlabel("$x$")
        plt.ylabel("$f(x)$")
        plt.title(f"Numerical integration using LU decomposition, N = {i}")
        plt.legend()
        plt.grid()

    call(["make", "cleanbin"])  # deleting data files.
    plt.show()  # displaying plots


if __name__ == '__main__':
    main()
