import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

S0 = 100 # initial stock price
mu = 0.08 #expected return (annual)
sigma = 0.2 #volatility(annual)
T = 1.0 #time horizon(years)
N = 252 #number of time steps(daily)
M = 10000 #number of simulated paths

dt = T/N #lenght of each time step
t = np.linspace(0,T,N+1) # time points (0 to T)
Z = np.random.randn(N,M) #random stocks( M path, N steps)
S = np.zeros((M, N+1)) # array to store simulates prices
S[:, 0] = S0 #set initial price for all paths
for i in range(N):
    S[:, i+1] = S[:, i] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[i, :])

final_prices = S[:, -1] #stock prices at time T
mean_price = np.mean(final_prices)
std_price = np.std(final_prices)
print(f'Mean final price: {mean_price:.2f}')
print(f'Standard deviation:{std_price:.2f}')

plt.figure(figsize=(12, 6))

plt.plot(t, S[:100, :].T, lw=0.8, alpha=0.6)

plt.title('Monte Carlo Simulation of Geometric Brownian Motion (GBM)')
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price ($)')
plt.grid(True)

plt.axhline(y=mean_price, color='r', linestyle='--', label=f'Mean Final Price: {mean_price:.2f}')
plt.legend(loc='upper left')

plt.show()



