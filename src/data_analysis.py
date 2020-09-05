import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({"text.usetex": True})

x = np.fromfile("x.bin")
u_anal = np.fromfile("u_anal.bin")
u_special = np.fromfile("u_special.bin")
u_general = np.fromfile("u_general.bin")
u_LUdecomp = np.fromfile("u_LUdecomp.bin")

plt.figure()
plt.plot(x, u_anal, label="analytic solution")
plt.plot(x, u_general, label="numerical solution")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Numerical integration using generalized Thomas algorithm")
plt.legend()
plt.grid()

plt.figure()
plt.plot(x, u_anal, label="analytic solution")
plt.plot(x, u_special, label="numerical solution")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Numerical integration using specialized Thomas algorithm")
plt.legend()
plt.grid()

plt.figure()
plt.plot(x, u_anal, label="analytic solution")
plt.plot(x, u_LUdecomp, label="numerical solution")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Numerical integration using LU decomposition")
plt.legend()
plt.grid()

plt.show()
