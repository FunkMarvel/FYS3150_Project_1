from subprocess import call, run
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# default arguments:
plotflag = False
errorflag = False
n_max = 3

# checking for commandline arguments:
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isnumeric():
            n_max = int(sys.argv[i])  # setting custom N values
        if sys.argv[i] == "plot":
            plotflag = True  # enable plotting of general algorithm
        if sys.argv[i] == "error":
            errorflag = True


lnmax = n_max
N = np.asarray([10**i for i in range(1, lnmax+1)])  # array of N values.
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
        plt.plot(x[2], u_anal[2], label="analytic solution")
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
    error = np.empty((3, len(N)))  # array for errors.
    log10_of_h = np.log10(1/(N+1))  # array for log of stepsize

    for j in range(len(N)):  # calculating errors.
        error[0, j] = np.max(np.log10(
            np.abs((u_general[j][1:-1]-u_anal[j][1:-1]) / u_anal[j][1:-1])))
        error[1, j] = np.max(np.log10(
            np.abs((u_special[j][1:-1]-u_anal[j][1:-1]) / u_anal[j][1:-1])))

    # writing errortable to file:
    with open("errortable.dat", "w") as outfile:
        outfile.write("Relative error as function of step size\n")
        outfile.write(
            "log10(h): | epsilon general algorithm: | epsilon special algorithm: | N\n")
        for i in range(len(N)):
            outfile.write(
                f"{log10_of_h[i]:e} | {error[0,i]:e} | {error[1,i]:e} | 10^{i+1}\n")


if __name__ == '__main__':
    main()
