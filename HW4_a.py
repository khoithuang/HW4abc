import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def calculate_and_plot_probabilities():
    """
    This function calculates and plots the probability density functions (PDFs)
    and cumulative distribution functions (CDFs) for two normal distributions.
    It highlights areas under the curve representing specific probabilities:
    - The probability of a value being less than 1 for a standard normal distribution (mean=0, std=1).
    - The probability of a value being greater than two standard deviations above the mean
      for another normal distribution (mean=175, std=3).
    """

    # Define parameters for two normal distributions
    mu1, sigma1 = 0, 1  # Parameters for the standard normal distribution N(0, 1)
    mu2, sigma2 = 175, 3  # Parameters for a normal distribution N(175, 3)

    # Calculate probabilities of interest
    P_x_less_than_1 = stats.norm(mu1, sigma1).cdf(1)  # Probability for N(0, 1)
    P_x_greater_than_mu2_plus_2sigma = 1 - stats.norm(mu2, sigma2).cdf(mu2 + 2*sigma2)  # Probability for N(175, 3)

    # Generate x values for plotting PDF and CDF
    x1 = np.linspace(mu1 - 4*sigma1, mu1 + 4*sigma1, 10000)  # X values for N(0, 1)
    y1 = stats.norm(mu1, sigma1).pdf(x1)  # PDF for N(0, 1)
    x2 = np.linspace(mu2 - 4*sigma2, mu2 + 4*sigma2, 10000)  # X values for N(175, 3)
    y2 = stats.norm(mu2, sigma2).cdf(x2)  # CDF for N(175, 3)

    # Creating subplots for each distribution
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot PDF for N(0, 1)
    axs[0].plot(x1, y1, label='N(0, 1)')
    axs[0].fill_between(x1, y1, where=(x1 < 1), color='blue', alpha=0.3, label=f'P(x<1)={P_x_less_than_1:.4f}')
    axs[0].legend()
    axs[0].grid(True)
    axs[0].set_title('Probability Density Function for N(0, 1)')

    # Plot CDF for N(175, 3)
    axs[1].plot(x2, y2, label='N(175, 3)')
    axs[1].fill_between(x2, y2, where=(x2 > mu2 + 2*sigma2), color='red', alpha=0.3, label=f'P(x>μ+2σ)={P_x_greater_than_mu2_plus_2sigma:.4f}')
    axs[1].legend()
    axs[1].grid(True)
    axs[1].set_title('Cumulative Distribution Function for N(175, 3)')

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

# Call and execute the function to calculate probabilities and generate plots
calculate_and_plot_probabilities()
