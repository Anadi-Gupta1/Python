"""
SciPy Integration - Complete Numerical Integration and ODE Guide
============================================================

Comprehensive guide to SciPy's integration capabilities, covering numerical
integration, ordinary differential equations (ODEs), partial differential 
equations (PDEs), and advanced mathematical techniques for scientific computing.

Author: Python Learning Notes
Date: September 2025
Topic: Numerical Integration, ODEs, Mathematical Analysis
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.integrate import quad, dblquad, tplquad, nquad
from scipy.integrate import odeint, solve_ivp
import time
from typing import Callable, Dict, List, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# NUMERICAL INTEGRATION FUNDAMENTALS
# =============================================================================

def integration_fundamentals():
    """
    Complete introduction to numerical integration concepts and methods
    """
    print("∫ SCIPY INTEGRATION FUNDAMENTALS")
    print("=" * 34)
    
    print("📊 Numerical Integration Overview:")
    print("   Numerical integration approximates definite integrals when")
    print("   analytical solutions are difficult or impossible to obtain.")
    
    print(f"\n🎯 Integration Problem Types:")
    integration_types = [
        ("Single Variable", "∫f(x)dx", "One-dimensional integration", "quad()"),
        ("Double Integral", "∫∫f(x,y)dxdy", "Two-dimensional integration", "dblquad()"),
        ("Triple Integral", "∫∫∫f(x,y,z)dxdydz", "Three-dimensional integration", "tplquad()"),
        ("Multiple Integral", "∫...∫f(x₁,...,xₙ)dx₁...dxₙ", "N-dimensional integration", "nquad()"),
        ("Improper Integral", "∫₋∞^∞ f(x)dx", "Infinite or semi-infinite limits", "quad() with np.inf"),
        ("Oscillatory", "∫f(x)cos(ωx)dx", "Rapidly oscillating functions", "Special techniques")
    ]
    
    print("   ┌─────────────────┬─────────────────────────┬─────────────────────────────┬─────────────────┐")
    print("   │ Type            │ Mathematical Form       │ Description                 │ SciPy Method    │")
    print("   ├─────────────────┼─────────────────────────┼─────────────────────────────┼─────────────────┤")
    
    for int_type, math_form, description, method in integration_types:
        print(f"   │ {int_type:<15} │ {math_form:<23} │ {description:<27} │ {method:<15} │")
    
    print("   └─────────────────┴─────────────────────────┴─────────────────────────────┴─────────────────┘")
    
    print(f"\n⚙️  Numerical Integration Methods:")
    methods = [
        ("Gauss-Kronrod", "Adaptive quadrature", "Default in quad()", "High accuracy, efficient"),
        ("Simpson's Rule", "Fixed-step method", "Classical approach", "Simple, pedagogical"),
        ("Trapezoidal Rule", "Fixed-step method", "Simplest method", "Easy to understand"),
        ("Monte Carlo", "Random sampling", "High-dimensional", "Good for complex domains"),
        ("Romberg", "Richardson extrapolation", "Sequential refinement", "Very high accuracy"),
        ("Clenshaw-Curtis", "Chebyshev nodes", "Smooth functions", "Fast convergence")
    ]
    
    print("   Method           │ Category         │ Usage            │ Characteristics")
    print("   ─────────────────┼──────────────────┼──────────────────┼────────────────────")
    
    for method, category, usage, characteristics in methods:
        print(f"   {method:<16} │ {category:<16} │ {usage:<16} │ {characteristics}")

def single_variable_integration():
    """
    Comprehensive demonstration of single-variable integration
    """
    print("\n📈 SINGLE VARIABLE INTEGRATION")
    print("=" * 31)
    
    # Example 1: Basic definite integral
    print("🎯 Example 1: Basic Definite Integral")
    print("   ∫₀^π sin(x) dx = 2")
    
    def sin_function(x):
        """Simple sine function"""
        return np.sin(x)
    
    result1, error1 = integrate.quad(sin_function, 0, np.pi)
    analytical_result1 = 2.0
    
    print(f"   Numerical result: {result1:.10f}")
    print(f"   Analytical result: {analytical_result1:.10f}")
    print(f"   Error estimate: {error1:.2e}")
    print(f"   Actual error: {abs(result1 - analytical_result1):.2e}")
    
    # Example 2: Gaussian integral
    print(f"\n📊 Example 2: Gaussian Integral")
    print("   ∫₋∞^∞ e^(-x²) dx = √π")
    
    def gaussian(x):
        """Gaussian function e^(-x²)"""
        return np.exp(-x**2)
    
    result2, error2 = integrate.quad(gaussian, -np.inf, np.inf)
    analytical_result2 = np.sqrt(np.pi)
    
    print(f"   Numerical result: {result2:.10f}")
    print(f"   Analytical result: {analytical_result2:.10f}")
    print(f"   Error estimate: {error2:.2e}")
    print(f"   Actual error: {abs(result2 - analytical_result2):.2e}")
    
    # Example 3: Oscillatory integral
    print(f"\n🌊 Example 3: Oscillatory Integral")
    print("   ∫₀^10π sin(10x)/x dx")
    
    def oscillatory(x):
        """Oscillatory function sin(10x)/x"""
        if x == 0:
            return 10  # Limit as x approaches 0
        return np.sin(10*x) / x
    
    result3, error3 = integrate.quad(oscillatory, 0, 10*np.pi)
    
    print(f"   Numerical result: {result3:.8f}")
    print(f"   Error estimate: {error3:.2e}")
    print(f"   Challenge: Highly oscillatory function")
    
    # Example 4: Improper integral with singularity
    print(f"\n⚠️  Example 4: Improper Integral with Singularity")
    print("   ∫₀^1 x^(-1/2) dx = 2")
    
    def power_singularity(x):
        """Function with singularity at x=0"""
        return x**(-0.5)
    
    result4, error4 = integrate.quad(power_singularity, 0, 1)
    analytical_result4 = 2.0
    
    print(f"   Numerical result: {result4:.10f}")
    print(f"   Analytical result: {analytical_result4:.10f}")
    print(f"   Error estimate: {error4:.2e}")
    print(f"   Note: SciPy handles the singularity automatically")
    
    # Example 5: Integration with parameters
    print(f"\n⚙️  Example 5: Parametric Integration")
    print("   ∫₀^∞ e^(-ax) dx = 1/a (for a > 0)")
    
    def exponential_decay(x, a):
        """Exponential decay function with parameter a"""
        return np.exp(-a * x)
    
    parameters = [0.5, 1.0, 2.0, 5.0]
    
    print("   Parameter │ Numerical     │ Analytical    │ Relative Error")
    print("   ──────────┼───────────────┼───────────────┼───────────────")
    
    for a in parameters:
        result, error = integrate.quad(exponential_decay, 0, np.inf, args=(a,))
        analytical = 1.0 / a
        rel_error = abs(result - analytical) / analytical
        
        print(f"   a = {a:<5.1f} │ {result:<13.10f} │ {analytical:<13.10f} │ {rel_error:<13.2e}")
    
    return {
        'sin_integral': result1,
        'gaussian_integral': result2,
        'oscillatory_integral': result3,
        'singular_integral': result4,
        'parametric_results': [(a, 1.0/a) for a in parameters]
    }

def multivariable_integration():
    """
    Comprehensive demonstration of multivariable integration
    """
    print("\n🎲 MULTIVARIABLE INTEGRATION")
    print("=" * 29)
    
    # Example 1: Double integral over rectangle
    print("📊 Example 1: Double Integral over Rectangle")
    print("   ∫₀¹ ∫₀² xy dx dy = 1")
    
    def integrand_2d(y, x):
        """2D integrand: xy (note order: y first, then x)"""
        return x * y
    
    result_2d, error_2d = integrate.dblquad(integrand_2d, 0, 2, 0, 1)
    analytical_2d = 1.0
    
    print(f"   Numerical result: {result_2d:.10f}")
    print(f"   Analytical result: {analytical_2d:.10f}")
    print(f"   Error estimate: {error_2d:.2e}")
    print(f"   Actual error: {abs(result_2d - analytical_2d):.2e}")
    
    # Example 2: Double integral over triangle
    print(f"\n📐 Example 2: Double Integral over Triangle")
    print("   ∫₀¹ ∫₀^(1-x) (x + y) dy dx")
    
    def integrand_triangle(y, x):
        """Integrand over triangular domain"""
        return x + y
    
    def y_upper(x):
        """Upper limit for y: y = 1 - x"""
        return 1 - x
    
    def y_lower(x):
        """Lower limit for y: y = 0"""
        return 0
    
    result_tri, error_tri = integrate.dblquad(
        integrand_triangle, 0, 1, y_lower, y_upper
    )
    
    # Analytical solution: ∫₀¹ ∫₀^(1-x) (x + y) dy dx = 1/3
    analytical_tri = 1.0/3.0
    
    print(f"   Domain: Triangle with vertices (0,0), (1,0), (0,1)")
    print(f"   Numerical result: {result_tri:.10f}")
    print(f"   Analytical result: {analytical_tri:.10f}")
    print(f"   Error estimate: {error_tri:.2e}")
    print(f"   Actual error: {abs(result_tri - analytical_tri):.2e}")
    
    # Example 3: Triple integral
    print(f"\n🎯 Example 3: Triple Integral")
    print("   ∫₀¹ ∫₀¹ ∫₀¹ xyz dx dy dz = 1/8")
    
    def integrand_3d(z, y, x):
        """3D integrand: xyz (note order: z, y, x)"""
        return x * y * z
    
    result_3d, error_3d = integrate.tplquad(
        integrand_3d, 0, 1, 0, 1, 0, 1
    )
    analytical_3d = 1.0/8.0
    
    print(f"   Numerical result: {result_3d:.10f}")
    print(f"   Analytical result: {analytical_3d:.10f}")
    print(f"   Error estimate: {error_3d:.2e}")
    print(f"   Actual error: {abs(result_3d - analytical_3d):.2e}")
    
    # Example 4: Integration over circular domain
    print(f"\n⭕ Example 4: Integration over Circular Domain")
    print("   ∫∫_D (x² + y²) dA, where D is the unit disk")
    
    def integrand_polar(r, theta):
        """Integrand in polar coordinates: r² * r (Jacobian)"""
        return r**3
    
    # Using polar coordinates: x² + y² = r², dA = r dr dθ
    result_circle, error_circle = integrate.dblquad(
        integrand_polar, 0, 2*np.pi, 0, 1
    )
    
    # Analytical result: ∫₀^(2π) ∫₀¹ r³ dr dθ = π/2
    analytical_circle = np.pi / 2.0
    
    print(f"   Using polar coordinates: (x² + y²) → r², dA → r dr dθ")
    print(f"   Numerical result: {result_circle:.10f}")
    print(f"   Analytical result: {analytical_circle:.10f}")
    print(f"   Error estimate: {error_circle:.2e}")
    print(f"   Actual error: {abs(result_circle - analytical_circle):.2e}")
    
    # Example 5: N-dimensional integration
    print(f"\n🌐 Example 5: N-Dimensional Integration")
    print("   4D integral: ∫₀¹ ∫₀¹ ∫₀¹ ∫₀¹ (x₁ + x₂ + x₃ + x₄) dx₁ dx₂ dx₃ dx₄")
    
    def integrand_4d(x):
        """4D integrand: sum of coordinates"""
        return np.sum(x)
    
    # Define integration bounds for 4D
    ranges = [[0, 1], [0, 1], [0, 1], [0, 1]]
    
    result_4d, error_4d = integrate.nquad(integrand_4d, ranges)
    
    # Analytical result: 4 * (1/2) = 2
    analytical_4d = 2.0
    
    print(f"   Dimensions: 4")
    print(f"   Numerical result: {result_4d:.10f}")
    print(f"   Analytical result: {analytical_4d:.10f}")
    print(f"   Error estimate: {error_4d:.2e}")
    print(f"   Actual error: {abs(result_4d - analytical_4d):.2e}")
    
    return {
        'rectangle_integral': result_2d,
        'triangle_integral': result_tri,
        'triple_integral': result_3d,
        'circle_integral': result_circle,
        'nd_integral': result_4d
    }

# =============================================================================
# ORDINARY DIFFERENTIAL EQUATIONS (ODEs)
# =============================================================================

def ode_fundamentals():
    """
    Complete introduction to solving ODEs with SciPy
    """
    print("\n🔄 ORDINARY DIFFERENTIAL EQUATIONS (ODEs)")
    print("=" * 42)
    
    print("📊 ODE Classification and Methods:")
    
    ode_types = [
        ("First-order", "dy/dt = f(t,y)", "Single variable", "Exponential decay/growth"),
        ("Second-order", "d²y/dt² = f(t,y,dy/dt)", "Two variables needed", "Oscillatory motion"),
        ("System of ODEs", "dy₁/dt = f₁(t,y₁,y₂,...)", "Multiple coupled equations", "Predator-prey models"),
        ("Stiff ODEs", "Multiple time scales", "Requires special methods", "Chemical reactions"),
        ("Boundary Value", "Conditions at boundaries", "Not initial value", "Beam deflection")
    ]
    
    print("   ┌─────────────────┬─────────────────────────┬─────────────────────────┬─────────────────────────┐")
    print("   │ ODE Type        │ Mathematical Form       │ Characteristics         │ Applications            │")
    print("   ├─────────────────┼─────────────────────────┼─────────────────────────┼─────────────────────────┤")
    
    for ode_type, math_form, characteristics, applications in ode_types:
        print(f"   │ {ode_type:<15} │ {math_form:<23} │ {characteristics:<23} │ {applications:<23} │")
    
    print("   └─────────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────┘")
    
    print(f"\n⚙️  SciPy ODE Solvers:")
    solvers = [
        ("solve_ivp", "Modern interface", "Adaptive methods", "Recommended for new code"),
        ("odeint", "Legacy interface", "LSODA method", "Backward compatibility"),
        ("RK45", "Runge-Kutta 4(5)", "Explicit method", "General purpose"),
        ("DOP853", "Dormand-Prince 8(5,3)", "High accuracy", "Smooth problems"),
        ("Radau", "Implicit method", "Stiff problems", "Chemical kinetics"),
        ("BDF", "Backward differentiation", "Very stiff problems", "Electrical circuits")
    ]
    
    print("   Method    │ Interface     │ Algorithm           │ Best For")
    print("   ──────────┼───────────────┼─────────────────────┼──────────────────────")
    
    for method, interface, algorithm, best_for in solvers:
        print(f"   {method:<9} │ {interface:<13} │ {algorithm:<19} │ {best_for}")

def first_order_odes():
    """
    Comprehensive examples of first-order ODEs
    """
    print("\n📈 FIRST-ORDER ODE EXAMPLES")
    print("=" * 28)
    
    # Example 1: Exponential decay
    print("☢️  Example 1: Radioactive Decay")
    print("   dy/dt = -λy, y(0) = y₀")
    print("   Analytical solution: y(t) = y₀ e^(-λt)")
    
    def radioactive_decay(t, y, lam):
        """dy/dt = -lambda * y"""
        return -lam * y
    
    # Parameters
    lambda_val = 0.5  # decay constant
    y0 = 100.0        # initial amount
    t_span = (0, 10)  # time interval
    t_eval = np.linspace(0, 10, 100)
    
    # Solve the ODE
    solution1 = integrate.solve_ivp(
        radioactive_decay, t_span, [y0], t_eval=t_eval, 
        args=(lambda_val,), dense_output=True
    )
    
    # Analytical solution for comparison
    y_analytical = y0 * np.exp(-lambda_val * t_eval)
    
    # Calculate error
    max_error = np.max(np.abs(solution1.y[0] - y_analytical))
    
    print(f"   Parameters: λ = {lambda_val}, y₀ = {y0}")
    print(f"   Time span: [0, 10]")
    print(f"   Maximum error: {max_error:.2e}")
    print(f"   Final value: Numerical = {solution1.y[0, -1]:.6f}, Analytical = {y_analytical[-1]:.6f}")
    
    # Example 2: Logistic growth
    print(f"\n📊 Example 2: Logistic Growth")
    print("   dy/dt = r*y*(1 - y/K), y(0) = y₀")
    print("   Analytical solution: y(t) = K/(1 + ((K-y₀)/y₀)*e^(-rt))")
    
    def logistic_growth(t, y, r, K):
        """dy/dt = r*y*(1 - y/K)"""
        return r * y * (1 - y / K)
    
    # Parameters
    r = 0.3    # growth rate
    K = 1000   # carrying capacity
    y0_log = 10  # initial population
    
    # Solve the ODE
    solution2 = integrate.solve_ivp(
        logistic_growth, (0, 20), [y0_log], t_eval=np.linspace(0, 20, 200),
        args=(r, K), dense_output=True
    )
    
    # Analytical solution
    t_log = solution2.t
    y_log_analytical = K / (1 + ((K - y0_log) / y0_log) * np.exp(-r * t_log))
    
    max_error_log = np.max(np.abs(solution2.y[0] - y_log_analytical))
    
    print(f"   Parameters: r = {r}, K = {K}, y₀ = {y0_log}")
    print(f"   Maximum error: {max_error_log:.2e}")
    print(f"   Final population: {solution2.y[0, -1]:.1f}")
    print(f"   Carrying capacity: {K}")
    
    # Example 3: First-order linear ODE
    print(f"\n🔢 Example 3: First-Order Linear ODE")
    print("   dy/dt + 2y = 3e^(-t), y(0) = 1")
    print("   Analytical solution: y(t) = (3t + 1)e^(-t)")
    
    def linear_ode(t, y):
        """dy/dt + 2y = 3e^(-t) => dy/dt = -2y + 3e^(-t)"""
        return -2*y + 3*np.exp(-t)
    
    # Solve the ODE
    solution3 = integrate.solve_ivp(
        linear_ode, (0, 5), [1], t_eval=np.linspace(0, 5, 100),
        dense_output=True
    )
    
    # Analytical solution
    t_lin = solution3.t
    y_lin_analytical = (3*t_lin + 1) * np.exp(-t_lin)
    
    max_error_lin = np.max(np.abs(solution3.y[0] - y_lin_analytical))
    
    print(f"   Maximum error: {max_error_lin:.2e}")
    print(f"   Final value: Numerical = {solution3.y[0, -1]:.6f}, Analytical = {y_lin_analytical[-1]:.6f}")
    
    return {
        'decay_solution': solution1,
        'logistic_solution': solution2,
        'linear_solution': solution3,
        'errors': {
            'decay': max_error,
            'logistic': max_error_log,
            'linear': max_error_lin
        }
    }

def systems_of_odes():
    """
    Comprehensive examples of ODE systems
    """
    print("\n🔗 SYSTEMS OF ODEs")
    print("=" * 19)
    
    # Example 1: Lotka-Volterra predator-prey model
    print("🐰🦊 Example 1: Lotka-Volterra Predator-Prey Model")
    print("   dx/dt = αx - βxy  (prey)")
    print("   dy/dt = δxy - γy  (predator)")
    
    def lotka_volterra(t, z, alpha, beta, gamma, delta):
        """Lotka-Volterra system"""
        x, y = z
        dxdt = alpha * x - beta * x * y
        dydt = delta * x * y - gamma * y
        return [dxdt, dydt]
    
    # Parameters
    alpha, beta, gamma, delta = 1.0, 0.5, 0.75, 0.25
    
    # Initial conditions
    x0, y0 = 10, 5
    
    # Solve the system
    t_span = (0, 20)
    t_eval = np.linspace(0, 20, 1000)
    
    solution_lv = integrate.solve_ivp(
        lotka_volterra, t_span, [x0, y0], t_eval=t_eval,
        args=(alpha, beta, gamma, delta), dense_output=True
    )
    
    # Calculate system properties
    x_sol, y_sol = solution_lv.y
    
    # Find approximate period (time for one cycle)
    x_peaks = []
    for i in range(1, len(x_sol)-1):
        if x_sol[i] > x_sol[i-1] and x_sol[i] > x_sol[i+1]:
            x_peaks.append(t_eval[i])
    
    if len(x_peaks) >= 2:
        period = x_peaks[1] - x_peaks[0]
    else:
        period = "Unknown"
    
    print(f"   Parameters: α={alpha}, β={beta}, γ={gamma}, δ={delta}")
    print(f"   Initial conditions: x₀={x0} (prey), y₀={y0} (predator)")
    print(f"   Approximate period: {period:.2f} time units" if isinstance(period, float) else f"   Period: {period}")
    print(f"   Final populations: prey={x_sol[-1]:.2f}, predator={y_sol[-1]:.2f}")
    
    # Example 2: Damped harmonic oscillator
    print(f"\n🌊 Example 2: Damped Harmonic Oscillator")
    print("   mx'' + cx' + kx = F(t)")
    print("   Convert to system: x₁ = x, x₂ = x'")
    print("   dx₁/dt = x₂")
    print("   dx₂/dt = (F(t) - cx₂ - kx₁)/m")
    
    def damped_oscillator(t, z, m, c, k, F):
        """Damped harmonic oscillator"""
        x, v = z  # position, velocity
        force = F(t) if callable(F) else F
        dxdt = v
        dvdt = (force - c * v - k * x) / m
        return [dxdt, dvdt]
    
    # Parameters
    m = 1.0     # mass
    c = 0.1     # damping coefficient
    k = 4.0     # spring constant
    
    # External force (sinusoidal)
    omega_drive = 2.0
    amplitude = 1.0
    
    def external_force(t):
        return amplitude * np.sin(omega_drive * t)
    
    # Initial conditions
    x0_osc, v0_osc = 1.0, 0.0
    
    # Solve the system
    solution_osc = integrate.solve_ivp(
        damped_oscillator, (0, 20), [x0_osc, v0_osc], 
        t_eval=np.linspace(0, 20, 1000),
        args=(m, c, k, external_force), dense_output=True
    )
    
    # Calculate natural frequency and damping ratio
    omega_n = np.sqrt(k / m)  # natural frequency
    zeta = c / (2 * np.sqrt(k * m))  # damping ratio
    
    print(f"   Parameters: m={m}, c={c}, k={k}")
    print(f"   Natural frequency: ωₙ = {omega_n:.3f} rad/s")
    print(f"   Damping ratio: ζ = {zeta:.3f} ({'underdamped' if zeta < 1 else 'overdamped' if zeta > 1 else 'critically damped'})")
    print(f"   Driving frequency: ω = {omega_drive:.3f} rad/s")
    print(f"   Final amplitude: {np.abs(solution_osc.y[0, -1]):.4f}")
    
    # Example 3: Chemical reaction kinetics (Oregonator)
    print(f"\n🧪 Example 3: Chemical Reaction Kinetics")
    print("   Simplified Oregonator model (3 species)")
    
    def oregonator(t, z, k1, k2, k3, k4, k5):
        """Simplified Oregonator chemical reaction model"""
        x, y, z_conc = z
        
        dxdt = k1*(y - x*y + x - k2*x**2)
        dydt = k3*(-y - x*y + k4*z_conc)
        dzdt = k5*(x - z_conc)
        
        return [dxdt, dydt, dzdt]
    
    # Parameters (typical values)
    k1, k2, k3, k4, k5 = 77.27, 8.375e-6, 0.161, 2e-4, 1.0
    
    # Initial conditions
    x0_chem, y0_chem, z0_chem = 1.0, 1.0, 1.0
    
    # Solve the system
    solution_chem = integrate.solve_ivp(
        oregonator, (0, 20), [x0_chem, y0_chem, z0_chem],
        t_eval=np.linspace(0, 20, 2000),
        args=(k1, k2, k3, k4, k5), method='Radau'  # Use stiff solver
    )
    
    print(f"   Chemical species: X, Y, Z")
    print(f"   Time span: 20 time units")
    print(f"   Solver: Radau (for stiff systems)")
    print(f"   Final concentrations: X={solution_chem.y[0, -1]:.4f}, Y={solution_chem.y[1, -1]:.4f}, Z={solution_chem.y[2, -1]:.4f}")
    
    return {
        'predator_prey': solution_lv,
        'harmonic_oscillator': solution_osc,
        'chemical_reaction': solution_chem,
        'system_properties': {
            'lv_period': period if isinstance(period, float) else None,
            'oscillator_frequency': omega_n,
            'damping_ratio': zeta
        }
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive SciPy integration guide
    """
    print(__doc__)
    
    # Integration fundamentals
    integration_fundamentals()
    single_results = single_variable_integration()
    
    # Multivariable integration
    multi_results = multivariable_integration()
    
    # ODE fundamentals and examples
    ode_fundamentals()
    first_order_results = first_order_odes()
    
    # Systems of ODEs
    system_results = systems_of_odes()
    
    return {
        'single_variable': single_results,
        'multivariable': multi_results,
        'first_order_odes': first_order_results,
        'ode_systems': system_results
    }

if __name__ == "__main__":
    """
    Execute comprehensive SciPy integration guide and demonstrations
    """
    results = main()
    
    print("\n" + "=" * 60)
    print("🎓 SCIPY INTEGRATION MASTERY SUMMARY")
    print("=" * 60)
    print("✅ Complete numerical integration fundamentals")
    print("✅ Single-variable integration with various techniques")
    print("✅ Multivariable integration (2D, 3D, N-dimensional)")
    print("✅ Improper integrals and singular functions")
    print("✅ Oscillatory and parametric integration")
    print("✅ Comprehensive ODE solving capabilities")
    print("✅ First-order ODEs (decay, growth, linear)")
    print("✅ Systems of ODEs (predator-prey, oscillators)")
    print("✅ Advanced applications (chemical kinetics)")
    print("✅ Stiff ODE solvers and numerical methods")
    
    print("\n💡 SciPy Integration Mastery Key Points:")
    key_points = [
        "Choose appropriate integration method based on problem type",
        "Handle singularities and improper integrals carefully",
        "Use adaptive methods for efficient and accurate results",
        "Transform coordinates for complex integration domains",
        "Select proper ODE solver based on stiffness and accuracy needs",
        "Validate solutions against analytical results when possible",
        "Consider numerical stability and convergence properties",
        "Apply appropriate error estimation and control strategies"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Integration Applications in Science & Engineering:")
    applications = [
        "Physics: Quantum mechanics and statistical mechanics",
        "Engineering: Control systems and signal processing",
        "Biology: Population dynamics and epidemiology",
        "Chemistry: Reaction kinetics and thermodynamics",
        "Economics: Financial modeling and optimization",
        "Climate science: Atmospheric and oceanic modeling",
        "Medicine: Pharmacokinetics and drug delivery",
        "Astronomy: Orbital mechanics and stellar evolution"
    ]
    
    for i, app in enumerate(applications, 1):
        print(f"   {i}. {app}")
    
    print(f"\n🚀 Ready for Advanced Mathematical Modeling!")
    print("Master the numerical techniques for complex scientific problems!")