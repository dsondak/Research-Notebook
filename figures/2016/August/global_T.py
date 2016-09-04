import numpy as np
import matplotlib.pyplot as plt
import config

plt.rcParams.update(config.pars)

mac = True # Working on mac or at work?

Tmin = 450.0
Tmax = 3000.0
delta = 1.0

T = np.linspace(Tmin, Tmax, 10000)

Tag  = 0.0
Tigg = 919.0
Tadg = 2680.0
global_react_1 = 0.5 * np.exp(-Tag / T) * (np.tanh((T - Tigg) / delta) - np.tanh((T - Tadg) / delta))

Tag  = 250.0
Tigg = 919.0
Tadg = 2680.0
global_react_2 = 0.5 * np.exp(-Tag / T) * (np.tanh((T - Tigg) / delta) - np.tanh((T - Tadg) / delta))

Tag  = 500.0
Tigg = 919.0
Tadg = 2680.0
global_react_3 = 0.5 * np.exp(-Tag / T) * (np.tanh((T - Tigg) / delta) - np.tanh((T - Tadg) / delta))

Tag  = 750.0
Tigg = 919.0
Tadg = 2680.0
global_react_4 = 0.5 * np.exp(-Tag / T) * (np.tanh((T - Tigg) / delta) - np.tanh((T - Tadg) / delta))

Tag  = 1000.0
Tigg = 919.0
Tadg = 2680.0
global_react_5 = 0.5 * np.exp(-Tag / T) * (np.tanh((T - Tigg) / delta) - np.tanh((T - Tadg) / delta))

if mac:
   fig, ax = plt.subplots(1,1, figsize=(10,7))
else:
   fig, ax = plt.subplots(1,1, figsize=(15,10))


ax.plot(T, global_react_1, lw=5, ls='-',  label=r'$T_{ag} = 0$')
ax.plot(T, global_react_2, lw=5, ls='--', label=r'$T_{ag} = 250$')
ax.plot(T, global_react_3, lw=5, ls='-.', label=r'$T_{ag} = 250$')
ax.plot(T, global_react_4, lw=5, ls='-.', label=r'$T_{ag} = 750$')
ax.plot(T, global_react_5, lw=5, ls=':', label=r'$T_{ag} = 1000$')

ax.legend(loc='best')

ax.set_xlabel(r'$T$')
ax.set_ylabel(r'$g\left(T\right)$')

fig.savefig('global_T.pdf')

plt.show()
