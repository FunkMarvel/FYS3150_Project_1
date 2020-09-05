from subprocess import call, run
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def main():
    mpl.rcParams.update({"text.usetex": True})

    N = np.array([10, 100, 1000])
    call(["make"])
    for i in N:
        run(["./main.exe", f"{i}"])

        x = np.fromfile(f"x{i}.bin")
        u_anal = np.fromfile(f"u_anal{i}.bin")
        u_special = np.fromfile(f"u_special{i}.bin")
        u_general = np.fromfile(f"u_general{i}.bin")
        u_LUdecomp = np.fromfile(f"u_LUdecomp{i}.bin")

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

    call(["make", "cleanbin"])
    plt.show()


if __name__ == '__main__':
    main()
