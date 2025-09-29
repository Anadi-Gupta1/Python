"""
SciPy Introduction - Scientific Computing Powerhouse
=================================================

Comprehensive introduction to SciPy, the scientific computing library that extends
NumPy with advanced mathematical algorithms, statistical functions, optimization
routines, and scientific tools for engineering, physics, and data science.

Author: Python Learning Notes
Date: September 2025
Topic: SciPy Introduction, Scientific Computing, Mathematical Algorithms
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, optimize, stats, integrate, linalg, signal, sparse
from scipy.spatial.distance import cdist
from scipy.interpolate import interp1d
import time
import sys
from typing import Dict, List, Any, Optional, Tuple

# =============================================================================
# SCIPY FUNDAMENTALS AND OVERVIEW
# =============================================================================

def scipy_comprehensive_introduction():
    """
    Complete introduction to SciPy and its role in scientific computing
    """
    print("🔬 SCIPY COMPREHENSIVE INTRODUCTION")
    print("=" * 37)
    
    print("🎯 What is SciPy?")
    print("   SciPy (Scientific Python) is a collection of mathematical algorithms")
    print("   and convenience functions built on NumPy that provides:")
    print("   • Advanced mathematical functions and algorithms")
    print("   • Statistical analysis and probability distributions")
    print("   • Optimization and root-finding algorithms")
    print("   • Signal and image processing tools")
    print("   • Linear algebra operations beyond NumPy")
    print("   • Integration and differential equation solvers")
    
    print(f"\n📚 Historical Background:")
    print("   • Created by Travis Oliphant, Pearu Peterson, Eric Jones (2001)")
    print("   • Built on top of NumPy for efficient array operations") 
    print("   • Name: Scientific Python (SciPy)")
    print("   • Open source under BSD license")
    print("   • Actively maintained by a global scientific community")
    
    print(f"\n🏗️  SciPy Architecture:")
    print("   ┌─────────────────────────────────────┐")
    print("   │          SciPy Modules              │")
    print("   │  (Advanced Scientific Functions)    │")
    print("   ├─────────────────────────────────────┤")
    print("   │             NumPy                   │")
    print("   │    (Arrays + Basic Math)            │")
    print("   ├─────────────────────────────────────┤")
    print("   │            Python                   │")
    print("   │    (Language Foundation)            │")
    print("   └─────────────────────────────────────┘")
    
    # Check SciPy version and components
    print(f"\n📊 Current SciPy Installation:")
    try:
        import scipy
        print(f"   Version: {scipy.__version__}")
        print(f"   Installation path: {scipy.__file__}")
    except ImportError:
        print("   ⚠️  SciPy not installed")
    
    print(f"   NumPy Version: {np.__version__}")
    print(f"   Python Version: {sys.version}")

def scipy_vs_numpy_comparison():
    """
    Detailed comparison between SciPy and NumPy capabilities
    """
    print("\n⚖️  SCIPY VS NUMPY - DETAILED COMPARISON")
    print("=" * 42)
    
    comparison_table = [
        {
            "aspect": "Basic Arrays",
            "numpy": "✅ Core array operations, basic math",
            "scipy": "✅ Extends with advanced algorithms",
            "winner": "NumPy for basics, SciPy for advanced"
        },
        {
            "aspect": "Linear Algebra",
            "numpy": "✅ Basic operations (dot, solve, eig)",
            "scipy": "✅ Advanced (sparse, decompositions, special)",
            "winner": "SciPy for comprehensive linear algebra"
        },
        {
            "aspect": "Statistics", 
            "numpy": "⚠️  Basic (mean, std, percentile)",
            "scipy": "✅ Comprehensive (distributions, tests, models)",
            "winner": "SciPy for statistical analysis"
        },
        {
            "aspect": "Optimization",
            "numpy": "❌ Not available",
            "scipy": "✅ Extensive (minimize, curve_fit, root finding)",
            "winner": "SciPy only option"
        },
        {
            "aspect": "Signal Processing",
            "numpy": "⚠️  Basic FFT operations",
            "scipy": "✅ Complete (filters, spectrograms, wavelets)",
            "winner": "SciPy for signal processing"
        },
        {
            "aspect": "Integration",
            "numpy": "❌ Not available",
            "scipy": "✅ Numerical integration (quad, odeint, solve_ivp)",
            "winner": "SciPy only option"
        }
    ]
    
    print("📊 Feature Comparison:")
    print("   ┌─────────────────────┬─────────────────────────────┬─────────────────────────────┐")
    print("   │ Aspect              │ NumPy                       │ SciPy                       │")
    print("   ├─────────────────────┼─────────────────────────────┼─────────────────────────────┤")
    
    for comp in comparison_table:
        aspect = comp["aspect"][:19]
        numpy_cap = comp["numpy"][:27]
        scipy_cap = comp["scipy"][:27]
        print(f"   │ {aspect:<19} │ {numpy_cap:<27} │ {scipy_cap:<27} │")
    
    print("   └─────────────────────┴─────────────────────────────┴─────────────────────────────┘")
    
    # Performance comparison example
    print(f"\n⚡ Performance Comparison Example:")
    print("   Task: Solve linear system Ax = b (1000x1000 matrix)")
    
    # Generate test data
    n = 1000
    A = np.random.randn(n, n)
    b = np.random.randn(n)
    
    # NumPy solution
    start_time = time.time()
    x_numpy = np.linalg.solve(A, b)
    numpy_time = time.time() - start_time
    
    # SciPy solution
    start_time = time.time()
    x_scipy = linalg.solve(A, b)
    scipy_time = time.time() - start_time
    
    print(f"   NumPy solve time: {numpy_time:.4f} seconds")
    print(f"   SciPy solve time: {scipy_time:.4f} seconds")
    print(f"   Solutions match: {np.allclose(x_numpy, x_scipy)}")
    
    if scipy_time < numpy_time:
        print(f"   SciPy is {numpy_time/scipy_time:.1f}x faster")
    else:
        print(f"   NumPy is {scipy_time/numpy_time:.1f}x faster")

# =============================================================================
# SCIPY MODULES AND CAPABILITIES
# =============================================================================

def scipy_modules_overview():
    """
    Complete overview of all SciPy modules and their capabilities
    """
    print("\n📦 SCIPY MODULES - COMPLETE OVERVIEW")
    print("=" * 37)
    
    modules = {
        "scipy.constants": {
            "description": "Physical and mathematical constants",
            "key_features": ["Physical constants", "Unit conversions", "Mathematical constants"],
            "example": "constants.c (speed of light), constants.pi"
        },
        "scipy.optimize": {
            "description": "Optimization and root-finding algorithms",
            "key_features": ["Function minimization", "Curve fitting", "Root finding", "Linear programming"],
            "example": "optimize.minimize(), optimize.curve_fit()"
        },
        "scipy.stats": {
            "description": "Statistical functions and probability distributions",
            "key_features": ["Probability distributions", "Statistical tests", "Descriptive statistics"],
            "example": "stats.norm(), stats.ttest_ind()"
        },
        "scipy.integrate": {
            "description": "Integration and differential equations",
            "key_features": ["Numerical integration", "ODEs", "Quadrature"],
            "example": "integrate.quad(), integrate.solve_ivp()"
        },
        "scipy.linalg": {
            "description": "Advanced linear algebra operations", 
            "key_features": ["Matrix decompositions", "Eigenvalues", "Special matrices"],
            "example": "linalg.svd(), linalg.eig()"
        },
        "scipy.signal": {
            "description": "Signal processing tools",
            "key_features": ["Digital filters", "Spectral analysis", "Wavelets"],
            "example": "signal.butter(), signal.find_peaks()"
        },
        "scipy.spatial": {
            "description": "Spatial data structures and algorithms",
            "key_features": ["Distance metrics", "Nearest neighbors", "Convex hulls"],
            "example": "spatial.distance.cdist()"
        },
        "scipy.sparse": {
            "description": "Sparse matrix operations",
            "key_features": ["Sparse matrix formats", "Sparse linear algebra", "Graph algorithms"],
            "example": "sparse.csr_matrix(), sparse.linalg.spsolve()"
        },
        "scipy.interpolate": {
            "description": "Interpolation and approximation",
            "key_features": ["1D/2D interpolation", "Spline fitting", "Radial basis functions"],
            "example": "interpolate.interp1d(), interpolate.griddata()"
        },
        "scipy.ndimage": {
            "description": "Multi-dimensional image processing",
            "key_features": ["Image filters", "Morphological operations", "Measurements"],
            "example": "ndimage.gaussian_filter()"
        },
        "scipy.fft": {
            "description": "Fast Fourier Transform operations",
            "key_features": ["FFT algorithms", "Discrete transforms", "Real FFTs"],
            "example": "fft.fft(), fft.rfft()"
        }
    }
    
    print("🔧 SciPy Module Ecosystem:")
    for module_name, info in modules.items():
        print(f"\n   📋 {module_name}:")
        print(f"      Description: {info['description']}")
        print(f"      Key Features: {', '.join(info['key_features'])}")
        print(f"      Example: {info['example']}")

def scipy_constants_comprehensive():
    """
    Comprehensive exploration of SciPy constants
    """
    print("\n🔢 SCIPY CONSTANTS - COMPREHENSIVE GUIDE")
    print("=" * 42)
    
    print("📊 Physical Constants:")
    
    physical_constants = [
        ("Speed of light", "constants.c", constants.c, "m/s"),
        ("Planck constant", "constants.h", constants.h, "J⋅s"),
        ("Boltzmann constant", "constants.k", constants.k, "J/K"),
        ("Avogadro number", "constants.N_A", constants.N_A, "1/mol"),
        ("Gas constant", "constants.R", constants.R, "J/(mol⋅K)"),
        ("Electron mass", "constants.m_e", constants.m_e, "kg"),
        ("Proton mass", "constants.m_p", constants.m_p, "kg"),
        ("Elementary charge", "constants.e", constants.e, "C"),
        ("Gravitational constant", "constants.G", constants.G, "m³/(kg⋅s²)")
    ]
    
    print("   ┌─────────────────────┬─────────────────────┬─────────────────────┬─────────────┐")
    print("   │ Constant            │ SciPy Name          │ Value               │ Unit        │")
    print("   ├─────────────────────┼─────────────────────┼─────────────────────┼─────────────┤")
    
    for name, scipy_name, value, unit in physical_constants:
        print(f"   │ {name:<19} │ {scipy_name:<19} │ {value:<19.3e} │ {unit:<11} │")
    
    print("   └─────────────────────┴─────────────────────┴─────────────────────┴─────────────┘")
    
    print(f"\n📐 Mathematical Constants:")
    
    math_constants = [
        ("Pi", "constants.pi", constants.pi),
        ("Golden ratio", "constants.golden", constants.golden),
        ("Euler's number", "np.e", np.e)
    ]
    
    for name, const_name, value in math_constants:
        print(f"   • {name}: {const_name} = {value}")
    
    print(f"\n🔄 Unit Conversions:")
    
    # Unit conversion examples
    conversions = [
        ("Length", "1 inch", constants.inch, "meters"),
        ("Length", "1 foot", constants.foot, "meters"),
        ("Volume", "1 liter", constants.liter, "cubic meters"),
        ("Volume", "1 gallon", constants.gallon, "cubic meters"),
        ("Pressure", "1 atm", constants.atm, "pascals"),
        ("Temperature", "0°C", constants.zero_Celsius, "Kelvin"),
        ("Energy", "1 eV", constants.eV, "joules"),
        ("Mass", "1 amu", constants.u, "kg")
    ]
    
    for category, quantity, value, unit in conversions:
        print(f"   • {quantity} = {value:.6f} {unit}")

# =============================================================================
# PRACTICAL SCIPY DEMONSTRATIONS
# =============================================================================

def scipy_optimization_demo():
    """
    Practical demonstration of SciPy optimization capabilities
    """
    print("\n🎯 SCIPY OPTIMIZATION - PRACTICAL DEMO")
    print("=" * 39)
    
    # Example 1: Function minimization
    print("📈 Example 1: Function Minimization")
    
    def objective_function(x):
        """Rosenbrock function - classic optimization test problem"""
        return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2
    
    # Initial guess
    initial_guess = np.array([0, 0])
    
    # Minimize using different methods
    methods = ['BFGS', 'Nelder-Mead', 'Powell']
    
    print("   Minimizing Rosenbrock function f(x,y) = 100(y-x²)² + (1-x)²")
    print("   Known minimum: f(1,1) = 0")
    
    for method in methods:
        result = optimize.minimize(objective_function, initial_guess, method=method)
        print(f"   {method:>12}: x = [{result.x[0]:6.3f}, {result.x[1]:6.3f}], f = {result.fun:8.6f}")
    
    # Example 2: Curve fitting
    print(f"\n📊 Example 2: Curve Fitting")
    
    # Generate noisy data
    np.random.seed(42)
    x_data = np.linspace(0, 4, 50)
    y_true = 2.5 * np.exp(-0.5 * x_data) * np.cos(2 * np.pi * x_data)
    y_data = y_true + 0.1 * np.random.normal(size=len(x_data))
    
    def model_function(x, a, b, c):
        """Model: a * exp(-b * x) * cos(c * x)"""
        return a * np.exp(-b * x) * np.cos(c * x)
    
    # Fit the curve
    popt, pcov = optimize.curve_fit(model_function, x_data, y_data)
    
    print(f"   Model: a * exp(-b * x) * cos(c * x)")
    print(f"   True parameters: a=2.5, b=0.5, c=6.28")
    print(f"   Fitted parameters: a={popt[0]:.2f}, b={popt[1]:.2f}, c={popt[2]:.2f}")
    print(f"   Parameter uncertainties: ±{np.sqrt(np.diag(pcov))}")
    
    # Calculate R-squared
    y_pred = model_function(x_data, *popt)
    ss_res = np.sum((y_data - y_pred)**2)
    ss_tot = np.sum((y_data - np.mean(y_data))**2)
    r_squared = 1 - (ss_res / ss_tot)
    print(f"   R-squared: {r_squared:.4f}")
    
    # Example 3: Root finding
    print(f"\n🔍 Example 3: Root Finding")
    
    def equation(x):
        """Find roots of: x³ - 6x² + 11x - 6 = 0"""
        return x**3 - 6*x**2 + 11*x - 6
    
    # Find roots using different methods
    root1 = optimize.brentq(equation, 0, 2)
    root2 = optimize.brentq(equation, 2, 3)
    root3 = optimize.brentq(equation, 3, 4)
    
    print(f"   Equation: x³ - 6x² + 11x - 6 = 0")
    print(f"   Root 1: x = {root1:.6f}, f(x) = {equation(root1):.2e}")
    print(f"   Root 2: x = {root2:.6f}, f(x) = {equation(root2):.2e}")
    print(f"   Root 3: x = {root3:.6f}, f(x) = {equation(root3):.2e}")
    print(f"   Analytical roots: 1, 2, 3")

def scipy_stats_demo():
    """
    Practical demonstration of SciPy statistical capabilities
    """
    print("\n📊 SCIPY STATISTICS - PRACTICAL DEMO")
    print("=" * 37)
    
    # Example 1: Probability distributions
    print("📈 Example 1: Probability Distributions")
    
    # Generate sample data
    np.random.seed(42)
    sample1 = np.random.normal(100, 15, 100)  # Group A: μ=100, σ=15
    sample2 = np.random.normal(105, 12, 100)  # Group B: μ=105, σ=12
    
    print(f"   Sample A: n=100, mean={np.mean(sample1):.1f}, std={np.std(sample1):.1f}")
    print(f"   Sample B: n=100, mean={np.mean(sample2):.1f}, std={np.std(sample2):.1f}")
    
    # Statistical tests
    print(f"\n🧪 Statistical Tests:")
    
    # t-test
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    print(f"   Independent t-test:")
    print(f"     t-statistic: {t_stat:.3f}")
    print(f"     p-value: {p_value:.6f}")
    print(f"     Significant difference (α=0.05): {'Yes' if p_value < 0.05 else 'No'}")
    
    # Normality test
    shapiro_stat1, shapiro_p1 = stats.shapiro(sample1)
    shapiro_stat2, shapiro_p2 = stats.shapiro(sample2)
    
    print(f"\n   Shapiro-Wilk normality test:")
    print(f"     Sample A: W={shapiro_stat1:.4f}, p={shapiro_p1:.4f}")
    print(f"     Sample B: W={shapiro_stat2:.4f}, p={shapiro_p2:.4f}")
    
    # Example 2: Distribution fitting
    print(f"\n📊 Example 2: Distribution Fitting")
    
    # Fit normal distribution
    mu, sigma = stats.norm.fit(sample1)
    print(f"   Fitted normal distribution to Sample A:")
    print(f"     μ = {mu:.2f}, σ = {sigma:.2f}")
    
    # Goodness of fit test
    ks_stat, ks_p = stats.kstest(sample1, lambda x: stats.norm.cdf(x, mu, sigma))
    print(f"     Kolmogorov-Smirnov test: D={ks_stat:.4f}, p={ks_p:.4f}")
    
    # Example 3: Correlation analysis
    print(f"\n🔗 Example 3: Correlation Analysis")
    
    # Generate correlated data
    correlation_matrix = np.array([[1, 0.7], [0.7, 1]])
    correlated_data = np.random.multivariate_normal([50, 60], correlation_matrix * 100, 100)
    
    x, y = correlated_data[:, 0], correlated_data[:, 1]
    
    # Calculate correlations
    pearson_r, pearson_p = stats.pearsonr(x, y)
    spearman_r, spearman_p = stats.spearmanr(x, y)
    
    print(f"   Correlation between X and Y:")
    print(f"     Pearson r: {pearson_r:.3f} (p={pearson_p:.4f})")
    print(f"     Spearman ρ: {spearman_r:.3f} (p={spearman_p:.4f})")
    
    return sample1, sample2, x, y

def scipy_integration_demo():
    """
    Practical demonstration of SciPy integration capabilities
    """
    print("\n∫ SCIPY INTEGRATION - PRACTICAL DEMO")
    print("=" * 38)
    
    # Example 1: Numerical integration
    print("📊 Example 1: Numerical Integration")
    
    def integrand(x):
        """Function to integrate: e^(-x²) * cos(x)"""
        return np.exp(-x**2) * np.cos(x)
    
    # Integrate from 0 to infinity
    result, error = integrate.quad(integrand, 0, np.inf)
    
    print(f"   ∫₀^∞ e^(-x²) cos(x) dx")
    print(f"   Numerical result: {result:.6f} ± {error:.2e}")
    print(f"   Analytical result: {np.sqrt(np.pi) / (2 * np.exp(0.25)):.6f}")
    
    # Example 2: Double integration
    print(f"\n📊 Example 2: Double Integration")
    
    def integrand_2d(y, x):
        """2D function: x*y*e^(-x²-y²)"""
        return x * y * np.exp(-x**2 - y**2)
    
    # Integrate over square [0,1] × [0,1]
    result_2d, error_2d = integrate.dblquad(integrand_2d, 0, 1, 0, 1)
    
    print(f"   ∫₀¹ ∫₀¹ xy e^(-x²-y²) dy dx")
    print(f"   Result: {result_2d:.6f} ± {error_2d:.2e}")
    
    # Example 3: Solving ODEs
    print(f"\n🔄 Example 3: Solving Ordinary Differential Equations")
    
    def lotka_volterra(t, y, alpha, beta, gamma, delta):
        """Lotka-Volterra predator-prey model"""
        x, z = y
        dxdt = alpha * x - beta * x * z
        dzdt = delta * x * z - gamma * z
        return [dxdt, dzdt]
    
    # Parameters: prey growth, predation, predator death, predation efficiency
    params = (1.0, 0.5, 0.75, 0.25)
    
    # Initial conditions: [prey, predator]
    y0 = [10, 5]
    
    # Time span
    t_span = (0, 20)
    t_eval = np.linspace(0, 20, 200)
    
    # Solve the ODE
    solution = integrate.solve_ivp(
        lotka_volterra, t_span, y0, t_eval=t_eval, args=params, dense_output=True
    )
    
    print(f"   Lotka-Volterra predator-prey model:")
    print(f"     dx/dt = αx - βxz,  dz/dt = δxz - γz")
    print(f"     Parameters: α=1.0, β=0.5, γ=0.75, δ=0.25")
    print(f"     Initial conditions: x₀=10, z₀=5")
    print(f"     Solution computed for t ∈ [0, 20]")
    
    # Final populations
    final_prey = solution.y[0, -1]
    final_predator = solution.y[1, -1]
    print(f"     Final populations: prey={final_prey:.2f}, predator={final_predator:.2f}")
    
    return solution

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive SciPy introduction
    """
    print(__doc__)
    
    # Core introduction
    scipy_comprehensive_introduction()
    scipy_vs_numpy_comparison()
    
    # Modules overview
    scipy_modules_overview()
    scipy_constants_comprehensive()
    
    # Practical demonstrations
    scipy_optimization_demo()
    samples = scipy_stats_demo()
    ode_solution = scipy_integration_demo()
    
    return {
        'statistical_samples': samples,
        'ode_solution': ode_solution
    }

if __name__ == "__main__":
    """
    Execute comprehensive SciPy introduction and demonstrations
    """
    results = main()
    
    print("\n" + "=" * 60)
    print("🎓 SCIPY SCIENTIFIC COMPUTING SUMMARY")
    print("=" * 60)
    print("✅ Comprehensive SciPy introduction and architecture")
    print("✅ Detailed comparison with NumPy capabilities")
    print("✅ Complete overview of all SciPy modules")
    print("✅ Physical and mathematical constants exploration")
    print("✅ Optimization algorithms and curve fitting")
    print("✅ Statistical analysis and hypothesis testing")
    print("✅ Numerical integration and ODE solving")
    print("✅ Real-world scientific computing applications")
    
    print("\n💡 SciPy Mastery Key Points:")
    key_points = [
        "SciPy extends NumPy with advanced scientific algorithms",
        "Comprehensive modules for optimization, statistics, integration",
        "Industry-standard algorithms for scientific and engineering problems", 
        "Seamless integration with NumPy arrays and Python ecosystem",
        "Performance-optimized implementations in C/Fortran",
        "Essential for research, engineering, and data science",
        "Rich collection of physical and mathematical constants",
        "Powerful tools for curve fitting and model validation"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Next Steps in Scientific Computing:")
    next_steps = [
        "Explore specific SciPy modules relevant to your domain",
        "Practice optimization techniques for your problems",
        "Learn advanced statistical analysis methods",
        "Master signal processing for time series data",
        "Study numerical methods for differential equations",
        "Integrate SciPy with visualization libraries",
        "Apply to real scientific and engineering challenges"
    ]
    
    for i, step in enumerate(next_steps, 1):
        print(f"   {i}. {step}")
    
    print(f"\n🚀 Ready for Advanced Scientific Computing!")
    print("SciPy provides the mathematical foundation for solving")
    print("complex scientific and engineering problems with Python!")
    
    # Additional learning resources
    print(f"\n📚 Recommended Learning Resources:")
    resources = [
        "SciPy Official Documentation (scipy.org)",
        "SciPy Cookbook for practical examples",
        "Scientific Python Lectures (scipy-lectures.org)",
        "Python Scientific Computing books",
        "Domain-specific applications and case studies"
    ]
    
    for resource in resources:
        print(f"   • {resource}")
