from subprocess import call, run
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# default arguments:
plotflag = False
errorflag = False
n_max = int(1e3)

# checking for commandline arguments:
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isnumeric():
            n_max = int(10 * sys.argv[i])  # setting custom N values
        if sys.argv[i] == "plot":
            plotflag = True  # enable plotting of general algorithm
        if sys.argv[i] == "error":
            errorflag = True


lnmax = int(np.log10(n_max))
N = np.asarray([10**i for i in range(1, lnmax)])  # array of N values.
x = []
u_anal = []
u_general = []
u_special = []
u_LUdecomp = []


def main():
    """
    This program solves Poisson's eq with thomas algorithm
    and lu decomposition in cpp. Use key argument 'plot' to plot:
    """
    generate_data()
    if errorflag:
        error_analysis()

    if plotflag:
        plotter()
    if errorflag or plotflag:
        plt.show()  # displaying plots


def generate_data():
    """
    Function for running building and running cpp program, as well as
    getting data from binaries.
    """
    call(["make"])  # compiling any changed cpp files.

    for i in range(len(N)):
        run(["./main.exe", f"{N[i]}"])  # running algorithms for each N.

        # reading data from file:
        x.append(np.fromfile(f"x{N[i]}.bin"))
        u_anal.append(np.fromfile(f"u_anal{N[i]}.bin"))
        u_special.append(np.fromfile(f"u_special{N[i]}.bin"))
        u_general.append(np.fromfile(f"u_general{N[i]}.bin"))
        # if N[i] <= 10000:
        #     u_LUdecomp.append(np.fromfile(f"u_LUdecomp{N[i]}.bin"))

    call(["make", "cleanbin"])  # deleting data files.


def plotter():
    """
    Function for plotting numerical and analytical solution
    from general algorithm.
    """
    mpl.rcParams.update({"text.usetex": True})  # using latex.
    for i in range(len(N)):
        # plotting numerical solve vs analytic solve:
        plt.figure()
        plt.plot(x[i], u_anal[i], label="analytic solution")
        plt.plot(x[i], u_general[i], label="numerical solution")
        plt.xlabel("$x$")
        plt.ylabel("$f(x)$")
        plt.title(f"Numerical integration using general algorithm, N = {N[i]}")
        plt.legend()
        plt.grid()


def error_analysis():
    """
    Function for calculating relative error and saving table to file.
    """
    error = np.empty((3, len(N)))
    log10_of_h = np.log10(1/(N+1))

    for j in range(len(N)):
        error[0, j] = np.max(np.log10(
            np.abs((u_general[j][1:-1]-u_anal[j][1:-1]) / u_anal[j][1:-1])))
        error[1, j] = np.max(np.log10(
            np.abs((u_special[j][1:-1]-u_anal[j][1:-1]) / u_anal[j][1:-1])))
        # if N[i] <= 10000:
        #     error[2, j] = np.max(np.log10(
        #         np.abs(
        #             (u_LUdecomp[j][1:-1]-u_anal[j][1:-1]) / u_anal[j][1:-1])))

    plt.figure()
    plt.plot(log10_of_h, error[0, :], label="General algorithm")
    plt.plot(log10_of_h, error[1, :], label="Special algorithm")
    # plt.plot(log10_of_h[:5], error[2, :], label="LU decomposition")
    plt.xlabel("$\log_{10}(h)$")
    plt.ylabel("$\log_{10}(\epsilon_{rel})$")
    plt.title(f"Relative error as function of step size")
    plt.legend()
    plt.grid()


if __name__ == '__main__':
    main()
