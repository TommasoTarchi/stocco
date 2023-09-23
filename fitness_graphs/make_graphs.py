import matplotlib.pyplot as plt 
import numpy as np




m = 20

x = np.arange(m)

flat = np.full(m, 1)
static_inc = 1.01 ** x
static_dec = 1.01 ** (m-x-1)
static_mount = 1.01 ** (m-np.fabs(m-2*x))


plt.figure(figsize=(8, 4))
plt.plot(x, flat)
plt.xlabel('genotypic space')
plt.ylabel('fitness')
plt.ylim(0.5, 1.5)
plt.xticks(np.arange(0, m+1, 1))
plt.legend()
plt.savefig("flat.png")

plt.figure(figsize=(8, 4))
plt.plot(x, static_inc)
plt.xlabel('genotypic space')
plt.ylabel('fitness')
plt.ylim(0.5, 1.5)
plt.xticks(np.arange(0, m+1, 1))
plt.legend()
plt.savefig("static_inc.png")

plt.figure(figsize=(8, 4))
plt.plot(x, static_dec)
plt.xlabel('genotypic space')
plt.ylabel('fitness')
plt.ylim(0.5, 1.5)
plt.xticks(np.arange(0, m+1, 1))
plt.legend()
plt.savefig("static_dec.png")

plt.figure(figsize=(8, 4))
plt.plot(x, static_mount)
plt.xlabel('genotypic space')
plt.ylabel('fitness')
plt.ylim(0.5, 1.5)
plt.xticks(np.arange(0, m+1, 1))
plt.legend()
plt.savefig("static_mount.png")




classes = np.arange(4)
numeric_freq = np.array([10000, 0, 0, 0])

plt.figure(figsize=(4, 4))

plt.bar(classes, numeric_freq, tick_label=classes.tolist())

plt.xlabel('genotipic class')
plt.ylabel('population')
plt.legend()

plt.savefig("genotipic_space_before.png")
