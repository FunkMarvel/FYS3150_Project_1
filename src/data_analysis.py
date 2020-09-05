from subprocess import call, run
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# default arguments:
plotflag = False
n_max = int(1e3)

# checking for commandline arguments:
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isnumeric():
            n_max = int(sys.argv[i])  # setting custom N values
        if sys.argv[i] == "plot":
            plotflag = True  # enable plotting of general algorithm


lnmax = int(np.log10(n_max)+1)
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
    if plotflag:
        plotter()
        plt.show()  # displaying plots


def generate_data():
    call(["make"])  # compiling any changed cpp files.

    for i in range(len(N)):
        run(["./main.exe", f"{N[i]}"])  # running algorithms for each N.

        # reading data from file:
        x.append(np.fromfile(f"x{N[i]}.bin"))
        u_anal.append(np.fromfile(f"u_anal{N[i]}.bin"))
        u_special.append(np.fromfile(f"u_special{N[i]}.bin"))
        u_general.append(np.fromfile(f"u_general{N[i]}.bin"))
        u_LUdecomp.append(np.fromfile(f"u_LUdecomp{N[i]}.bin"))

    call(["make", "cleanbin"])  # deleting data files.


def plotter():
    mpl.rcParams.update({"text.usetex": True})  # using latex.
    for i in range(len(N)):
        # plotting each numerical solve vs analytic solve:
        plt.figure()
        plt.plot(x[i], u_anal[i], label="analytic solution")
        plt.plot(x[i], u_general[i], label="numerical solution")
        plt.xlabel("$x$")
        plt.ylabel("$f(x)$")
        plt.title(f"Numerical integration using general algorithm, N = {N[i]}")
        plt.legend()
        plt.grid()

        # plt.figure()
        # plt.plot(x[i], u_anal[i], label="analytic solution")
        # plt.plot(x[i], u_special[i], label="numerical solution")
        # plt.xlabel("$x$")
        # plt.ylabel("$f(x)$")
        # plt.title(f"Numerical integration using special algorithm, N = {N[i]}")
        # plt.legend()
        # plt.grid()

        # plt.figure()
        # plt.plot(x[i], u_anal[i], label="analytic solution")
        # plt.plot(x[i], u_LUdecomp[i], label="numerical solution")
        # plt.xlabel("$x$")
        # plt.ylabel("$f(x)$")
        # plt.title(f"Numerical integration using LU decomposition, N = {N[i]}")
        # plt.legend()
        # plt.grid()


if __name__ == '__main__':
    main()
