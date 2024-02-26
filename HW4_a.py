from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the distributions
mu1, sigma1 = 0, 1  # N(0, 1)
mu2, sigma2 = 175, 3  # N(175, 3)

# Calculate probabilities
P_x_less_than_1 = stats.norm(mu1, sigma1).cdf(1)
P_x_greater_than_mu2_plus_2sigma = 1 - stats.norm(mu2, sigma2).cdf(mu2 + 2*sigma2)

# Creating numpy arrays for plotting
x1 = np.linspace(mu1 - 4*sigma1, mu1 + 4*sigma1, 10000)
y1 = stats.norm(mu1, sigma1).pdf(x1)
x2 = np.linspace(mu2 - 4*sigma2, mu2 + 4*sigma2, 10000)
y2 = stats.norm(mu2, sigma2).cdf(x2)

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot for N(0, 1)
axs[0].plot(x1, y1, label='N(0, 1)')
axs[0].fill_between(x1, y1, where=(x1 < 1), color='blue', alpha=0.3, label=f'P(x<1)={P_x_less_than_1:.4f}')
axs[0].legend()
axs[0].grid(True)
axs[0].set_title('Probability Density Function for N(0, 1)')

# Plot for N(175, 3)
axs[1].plot(x2, y2, label='N(175, 3)')
axs[1].fill_between(x2, y2, where=(x2 > mu2 + 2*sigma2), color='red', alpha=0.3, label=f'P(x>μ+2σ)={P_x_greater_than_mu2_plus_2sigma:.4f}')
axs[1].legend()
axs[1].grid(True)
axs[1].set_title('Probability Density Function for N(175, 3)')

plt.tight_layout()
plt.show()
