#IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


"""

Value At Risk (Parametric) Formula:
VaR = delta*S0 * (mu*T - sigma*(T**1/2) * zc)

Parameters:
delta = Asset Quantity
S0 = Asset Price
mu = Expected Return (Drift)
T = Number Of Years
sigma = Volatility (Constant)
c = Confidence Level
zc = Standard Normal Value Corresponding To Confidence Level

"""


#PARAMETERS
delta = _ #Replace the underscore with Asset Quantity
S0 = _ #Replace the underscore with Asset Price
mu = _ #Replace the underscore with Expected Return (Drift)
sigma = _ #Replace the underscore with Volatility (Constant)
T = _ #Replace the underscore with Number Of Years
c = _ #Replace the underscore with Confidence Level 
zc = norm.ppf(c)


#VaR CALCULATION
VaR = delta*S0 * (sigma*np.sqrt(T)*zc - mu*T)
print(f"Value at Risk ({c*100:.0f}% confidence, Time = {T}Y): ${VaR:.2f}")


#PLOT (VaR)
x = np.linspace(start = mu - 4*sigma, stop = mu + 4*sigma, num = 1000)
y = norm(loc = mu, scale = sigma).pdf(x)
plt.plot(x, y, color = "gray")
plt.fill_between(x, y, color = "cyan", alpha = 0.2)
plt.fill_between(x, y, where=(x <= -zc*sigma), color = "red", alpha=0.5)
plt.xlabel(f"Mean = {mu}\n Standard Deviation = {sigma}")
plt.ylabel("Frequency")
plt.title("Standard Normal Distribution (Returns)")
plt.axvline(-zc*sigma, linestyle = "dashed", color = "red", label = "Value at Risk")
plt.legend()
plt.show()
