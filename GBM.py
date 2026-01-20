import numpy as np
import matplotlib.pyplot as plt

"""

Geometric Brownian Motion Formula (Implicit):
dSt = mu*St*dt + sigma*St*dW

Geometric Brownian Motion Solution (Explicit):
St = S0**exp((mu - sigma**2 / 2)*t - sigma*Wt)

Parameters:
St = Asset Price At Time t
S0 = Asset Price At Time t=0 (Initial Price)
mu = Expected Return (Drift)
sigma = Volatility (Constant)
t = Time Periods
n = Number Of Time Periods
T = Number Of Years
Wt = Standard Brownian Motion (Wiener process)
Ns = Number Of Simulations

"""

#PARAMETERS
mu = 0.15
n = 365
T = 1
Ns = 100
S0 = 100
sigma = 0.12

#SIMULATION PROCESS
t = T/n
St = np.exp((mu - sigma ** 2 / 2) * t + sigma * np.random.normal(0, np.sqrt(t), size = (Ns, n)).T)
St = np.vstack([np.ones(Ns), St])
St = S0 * St.cumprod(axis = 0)

#TIME INTERVAL TO YEARS
time = np.linspace(0, T, n+1)
tt = np.full(shape = (Ns, n+1), fill_value = time).T

#PLOT
plt.plot(tt, St)
plt.xlabel("Years $(t)$")
plt.ylabel("Stock Price $(S_t)$")
plt.title("GBM Simulation")
plt.show()

print ("Successful")