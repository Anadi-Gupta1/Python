"""
SciPy Scientific Computing - Comprehensive Guide
===============================================

Educational guide to SciPy for optimization, signal processing, statistics, and integration.
Includes practical examples and best practices for scientific computing.

Author: Python Learning Notes
Date: September 2025
Topic: SciPy, Optimization, Signal Processing, Statistics, Integration
"""

import numpy as np
from scipy import optimize, signal, stats, integrate

# =============================================================================
# OPTIMIZATION
# =============================================================================

def optimization_demo():
    print("\n🔎 Optimization Demo")
    def func(x):
        return (x - 2) ** 2 + 1
    result = optimize.minimize(func, x0=0)
    print(f"Minimum of (x-2)^2+1 at x = {result.x[0]:.2f}, f(x) = {result.fun:.2f}")

# =============================================================================
# SIGNAL PROCESSING
# =============================================================================

def signal_processing_demo():
    print("\n📶 Signal Processing Demo")
    t = np.linspace(0, 1, 500)
    sig = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(500)
    filtered = signal.medfilt(sig, kernel_size=5)
    print(f"Original signal mean: {np.mean(sig):.2f}, Filtered mean: {np.mean(filtered):.2f}")

# =============================================================================
# STATISTICS
# =============================================================================

def statistics_demo():
    print("\n📊 Statistics Demo (SciPy)")
    data = np.random.normal(loc=0, scale=1, size=1000)
    mean, var = stats.norm.fit(data)
    print(f"Fitted mean: {mean:.2f}, variance: {var:.2f}")
    ks_stat, ks_p = stats.kstest(data, 'norm')
    print(f"KS test statistic: {ks_stat:.2f}, p-value: {ks_p:.2f}")

# =============================================================================
# INTEGRATION
# =============================================================================

def integration_demo():
    print("\n∫ Integration Demo")
    result, error = integrate.quad(lambda x: np.exp(-x ** 2), -2, 2)
    print(f"Integral of exp(-x^2) from -2 to 2: {result:.4f} (error: {error:.2e})")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    optimization_demo()
    signal_processing_demo()
    statistics_demo()
    integration_demo()

if __name__ == "__main__":
    main()
