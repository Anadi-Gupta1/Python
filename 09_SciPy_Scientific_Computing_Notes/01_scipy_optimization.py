"""
SciPy Optimization - Complete Mathematical Optimization Guide
==========================================================

Comprehensive guide to SciPy's optimization capabilities, covering function 
minimization, curve fitting, root finding, linear programming, and constrained
optimization with practical applications in science, engineering, and data science.

Author: Python Learning Notes
Date: September 2025
Topic: Mathematical Optimization, Function Minimization, Curve Fitting
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import minimize, curve_fit, root, linprog
import time
from typing import Callable, Dict, List, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# FUNCTION MINIMIZATION FUNDAMENTALS
# =============================================================================

def optimization_fundamentals():
    """
    Complete introduction to optimization concepts and SciPy methods
    """
    print("🎯 SCIPY OPTIMIZATION FUNDAMENTALS")
    print("=" * 36)
    
    print("📊 Mathematical Optimization Overview:")
    print("   Optimization is the process of finding the best solution")
    print("   from a set of available alternatives.")
    
    print(f"\n🎯 Types of Optimization Problems:")
    problem_types = [
        ("Unconstrained", "No restrictions on variables", "minimize(f, x0)"),
        ("Constrained", "Subject to equality/inequality constraints", "minimize(f, x0, constraints)"),
        ("Linear Programming", "Linear objective and constraints", "linprog(c, A, b)"),
        ("Integer Programming", "Some/all variables must be integers", "Special algorithms"),
        ("Multi-objective", "Multiple competing objectives", "Pareto optimization"),
        ("Global Optimization", "Find global minimum (not local)", "differential_evolution")
    ]
    
    print("   ┌──────────────────┬────────────────────────────────┬─────────────────────────────┐")
    print("   │ Type             │ Description                    │ SciPy Method                │")
    print("   ├──────────────────┼────────────────────────────────┼─────────────────────────────┤")
    
    for type_name, desc, method in problem_types:
        print(f"   │ {type_name:<16} │ {desc:<30} │ {method:<27} │")
    
    print("   └──────────────────┴────────────────────────────────┴─────────────────────────────┘")
    
    print(f"\n⚙️  SciPy Optimization Methods:")
    methods = [
        ("BFGS", "Quasi-Newton method", "Good general purpose", "O(n²) memory"),
        ("L-BFGS-B", "Limited memory BFGS", "Bounded variables", "O(n) memory"),
        ("Nelder-Mead", "Simplex algorithm", "Derivative-free", "Robust but slow"),
        ("Powell", "Direction set method", "Derivative-free", "Good for separable"),
        ("CG", "Conjugate gradient", "Large problems", "Requires gradient"),
        ("Newton-CG", "Newton conjugate gradient", "Fast convergence", "Requires Hessian")
    ]
    
    print("   Method      │ Type              │ Best For         │ Notes")
    print("   ────────────┼───────────────────┼──────────────────┼────────────────")
    for method, method_type, best_for, notes in methods:
        print(f"   {method:<11} │ {method_type:<17} │ {best_for:<16} │ {notes}")

def classic_optimization_problems():
    """
    Demonstrate classic optimization problems and their solutions
    """
    print("\n📚 CLASSIC OPTIMIZATION PROBLEMS")
    print("=" * 33)
    
    # Problem 1: Rosenbrock Function (Banana Function)
    print("🍌 Problem 1: Rosenbrock Function")
    print("   f(x,y) = 100(y - x²)² + (1 - x)²")
    print("   Known global minimum: f(1,1) = 0")
    
    def rosenbrock(x):
        """The Rosenbrock function"""
        return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2
    
    def rosenbrock_grad(x):
        """Gradient of the Rosenbrock function"""
        df_dx = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
        df_dy = 200 * (x[1] - x[0]**2)
        return np.array([df_dx, df_dy])
    
    # Test different starting points and methods
    starting_points = [[-1.2, 1.0], [0, 0], [-2, -2]]
    methods = ['BFGS', 'Nelder-Mead', 'Powell']
    
    print(f"\n   Optimization Results:")
    print("   Starting Point    │ Method      │ Solution       │ Function Value │ Iterations")
    print("   ──────────────────┼─────────────┼────────────────┼────────────────┼───────────")
    
    for start in starting_points:
        for method in methods:
            result = optimize.minimize(rosenbrock, start, method=method, 
                                     jac=rosenbrock_grad if method in ['BFGS', 'CG'] else None)
            print(f"   {str(start):<17} │ {method:<11} │ [{result.x[0]:5.3f}, {result.x[1]:5.3f}] │ {result.fun:14.6f} │ {result.nit:10d}")
    
    # Problem 2: Himmelblau's Function (Multiple Minima)
    print(f"\n🏔️  Problem 2: Himmelblau's Function (Multiple Minima)")
    print("   f(x,y) = (x² + y - 11)² + (x + y² - 7)²")
    print("   Known minima at: (3,2), (-2.8,3.1), (-3.8,-3.3), (3.6,-1.8)")
    
    def himmelblau(x):
        """Himmelblau's function with 4 global minima"""
        return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    
    # Use global optimization to find all minima
    bounds = [(-5, 5), (-5, 5)]
    
    print(f"\n   Global Optimization Results:")
    minima_found = []
    
    for i in range(10):  # Multiple random starts
        result = optimize.differential_evolution(himmelblau, bounds, seed=i)
        
        # Check if this is a new minimum
        is_new = True
        for prev_min in minima_found:
            if np.linalg.norm(result.x - prev_min) < 0.1:
                is_new = False
                break
        
        if is_new and result.fun < 1e-10:
            minima_found.append(result.x)
    
    print(f"   Found {len(minima_found)} distinct minima:")
    for i, minimum in enumerate(minima_found, 1):
        print(f"     Minimum {i}: ({minimum[0]:5.3f}, {minimum[1]:5.3f}), f = {himmelblau(minimum):.2e}")
    
    # Problem 3: Constrained Optimization
    print(f"\n🔒 Problem 3: Constrained Optimization")
    print("   Minimize: f(x,y) = (x-1)² + (y-2.5)²")
    print("   Subject to: x + 2y ≥ 2, -x + 2y ≤ 6, -x - 2y ≤ 2, x,y ≥ 0")
    
    def constrained_objective(x):
        """Objective function for constrained problem"""
        return (x[0] - 1)**2 + (x[1] - 2.5)**2
    
    # Define constraints
    constraints = [
        {'type': 'ineq', 'fun': lambda x: x[0] + 2*x[1] - 2},    # x + 2y >= 2
        {'type': 'ineq', 'fun': lambda x: 6 - (-x[0] + 2*x[1])}, # -x + 2y <= 6
        {'type': 'ineq', 'fun': lambda x: 2 - (-x[0] - 2*x[1])}, # -x - 2y <= 2
    ]
    
    bounds = [(0, None), (0, None)]  # x, y >= 0
    
    result_constrained = optimize.minimize(
        constrained_objective, [0, 0], method='SLSQP', 
        constraints=constraints, bounds=bounds
    )
    
    print(f"   Constrained optimum: ({result_constrained.x[0]:.3f}, {result_constrained.x[1]:.3f})")
    print(f"   Minimum value: {result_constrained.fun:.6f}")
    print(f"   Success: {result_constrained.success}")
    
    return {
        'rosenbrock_solutions': None,
        'himmelblau_minima': minima_found,
        'constrained_solution': result_constrained.x
    }

# =============================================================================
# CURVE FITTING AND PARAMETER ESTIMATION
# =============================================================================

def comprehensive_curve_fitting():
    """
    Complete guide to curve fitting with real-world examples
    """
    print("\n📊 COMPREHENSIVE CURVE FITTING")
    print("=" * 32)
    
    # Example 1: Exponential Decay (Radioactive Decay Model)
    print("⚛️  Example 1: Exponential Decay Model")
    print("   Model: N(t) = N₀ * e^(-λt)")
    print("   Application: Radioactive decay, drug elimination")
    
    # Generate synthetic data with noise
    np.random.seed(42)
    t_true = np.linspace(0, 10, 50)
    N0_true = 1000.0
    lambda_true = 0.3
    N_true = N0_true * np.exp(-lambda_true * t_true)
    noise = 0.05 * N_true * np.random.normal(size=len(t_true))
    N_measured = N_true + noise
    
    def exponential_decay(t, N0, lam):
        """Exponential decay model"""
        return N0 * np.exp(-lam * t)
    
    # Fit the model
    popt, pcov = optimize.curve_fit(exponential_decay, t_true, N_measured)
    N0_fit, lambda_fit = popt
    
    # Calculate parameter uncertainties
    param_std = np.sqrt(np.diag(pcov))
    
    # Calculate goodness of fit
    N_pred = exponential_decay(t_true, *popt)
    ss_res = np.sum((N_measured - N_pred)**2)
    ss_tot = np.sum((N_measured - np.mean(N_measured))**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    print(f"\n   Fitting Results:")
    print(f"     True parameters:   N₀ = {N0_true:.1f}, λ = {lambda_true:.3f}")
    print(f"     Fitted parameters: N₀ = {N0_fit:.1f} ± {param_std[0]:.1f}, λ = {lambda_fit:.3f} ± {param_std[1]:.3f}")
    print(f"     R-squared: {r_squared:.6f}")
    
    # Calculate half-life
    half_life_true = np.log(2) / lambda_true
    half_life_fit = np.log(2) / lambda_fit
    print(f"     Half-life: True = {half_life_true:.2f}, Fitted = {half_life_fit:.2f}")
    
    # Example 2: Sigmoidal Growth (Logistic Model)
    print(f"\n📈 Example 2: Sigmoidal Growth Model")
    print("   Model: P(t) = K / (1 + ((K-P₀)/P₀) * e^(-rt))")
    print("   Application: Population growth, technology adoption")
    
    # Generate logistic growth data
    t_growth = np.linspace(0, 20, 40)
    K_true = 1000.0  # Carrying capacity
    P0_true = 10.0   # Initial population
    r_true = 0.3     # Growth rate
    
    def logistic_growth(t, K, P0, r):
        """Logistic growth model"""
        return K / (1 + ((K - P0) / P0) * np.exp(-r * t))
    
    P_true = logistic_growth(t_growth, K_true, P0_true, r_true)
    P_noise = P_true + 0.05 * P_true * np.random.normal(size=len(t_growth))
    
    # Fit logistic model
    # Provide reasonable initial guesses
    initial_guess = [max(P_noise), min(P_noise), 0.1]
    
    try:
        popt_logistic, pcov_logistic = optimize.curve_fit(
            logistic_growth, t_growth, P_noise, p0=initial_guess, maxfev=10000
        )
        
        K_fit, P0_fit, r_fit = popt_logistic
        param_std_logistic = np.sqrt(np.diag(pcov_logistic))
        
        print(f"   Fitting Results:")
        print(f"     True parameters:   K = {K_true:.0f}, P₀ = {P0_true:.1f}, r = {r_true:.3f}")
        print(f"     Fitted parameters: K = {K_fit:.0f} ± {param_std_logistic[0]:.0f}, ")
        print(f"                        P₀ = {P0_fit:.1f} ± {param_std_logistic[1]:.1f}, ")
        print(f"                        r = {r_fit:.3f} ± {param_std_logistic[2]:.3f}")
        
    except Exception as e:
        print(f"   Fitting failed: {e}")
        popt_logistic = initial_guess
    
    # Example 3: Polynomial Fitting with Model Selection
    print(f"\n🔢 Example 3: Polynomial Fitting and Model Selection")
    
    # Generate data from a cubic polynomial with noise
    x_poly = np.linspace(-2, 2, 30)
    true_coeffs = [1, -0.5, -2, 1]  # 1 - 0.5x - 2x² + x³
    y_true_poly = np.polyval(true_coeffs, x_poly)
    y_noisy_poly = y_true_poly + 0.5 * np.random.normal(size=len(x_poly))
    
    print(f"   Testing polynomial degrees 1 through 6:")
    print("   Degree │ R²      │ AIC     │ BIC     │ RMSE    │ Parameters")
    print("   ───────┼─────────┼─────────┼─────────┼─────────┼────────────")
    
    results = []
    for degree in range(1, 7):
        # Fit polynomial
        coeffs = np.polyfit(x_poly, y_noisy_poly, degree)
        y_pred = np.polyval(coeffs, x_poly)
        
        # Calculate metrics
        n = len(y_noisy_poly)
        k = degree + 1  # Number of parameters
        
        ss_res = np.sum((y_noisy_poly - y_pred)**2)
        ss_tot = np.sum((y_noisy_poly - np.mean(y_noisy_poly))**2)
        r_squared = 1 - (ss_res / ss_tot)
        
        mse = ss_res / n
        rmse = np.sqrt(mse)
        
        # Information criteria (lower is better)
        aic = n * np.log(mse) + 2 * k
        bic = n * np.log(mse) + k * np.log(n)
        
        results.append({
            'degree': degree,
            'r_squared': r_squared,
            'aic': aic,
            'bic': bic,
            'rmse': rmse,
            'coeffs': coeffs
        })
        
        print(f"   {degree:6d} │ {r_squared:7.5f} │ {aic:7.2f} │ {bic:7.2f} │ {rmse:7.4f} │ {k}")
    
    # Find best model by BIC
    best_model = min(results, key=lambda x: x['bic'])
    print(f"\n   Best model by BIC: Degree {best_model['degree']}")
    print(f"   True degree: 3")
    
    return {
        'exponential_fit': (popt, pcov),
        'logistic_fit': popt_logistic if 'popt_logistic' in locals() else None,
        'polynomial_results': results
    }

# =============================================================================
# ROOT FINDING AND EQUATION SOLVING
# =============================================================================

def comprehensive_root_finding():
    """
    Complete guide to root finding algorithms and equation solving
    """
    print("\n🎯 COMPREHENSIVE ROOT FINDING")
    print("=" * 31)
    
    print("📊 Root Finding Methods Overview:")
    methods = [
        ("brentq", "Brent's method", "Bracketing", "Fast, robust", "f(a)⋅f(b)<0"),
        ("newton", "Newton-Raphson", "Open", "Very fast", "Good initial guess"),
        ("bisect", "Bisection", "Bracketing", "Slow but robust", "f(a)⋅f(b)<0"),
        ("secant", "Secant method", "Open", "Fast", "Two initial guesses"),
        ("fsolve", "Hybrid method", "General", "Robust", "Works for systems")
    ]
    
    print("   Method   │ Algorithm        │ Type       │ Speed/Robustness │ Requirements")
    print("   ─────────┼──────────────────┼────────────┼──────────────────┼─────────────")
    for method, algorithm, method_type, speed, req in methods:
        print(f"   {method:<8} │ {algorithm:<16} │ {method_type:<10} │ {speed:<16} │ {req}")
    
    # Example 1: Single Variable Root Finding
    print(f"\n🔍 Example 1: Single Variable Root Finding")
    print("   Equation: x³ - 6x² + 11x - 6 = 0")
    print("   Analytical roots: x = 1, 2, 3")
    
    def cubic_equation(x):
        """Cubic equation with known roots at 1, 2, 3"""
        return x**3 - 6*x**2 + 11*x - 6
    
    def cubic_derivative(x):
        """Derivative of cubic equation"""
        return 3*x**2 - 12*x + 11
    
    # Find roots using different methods
    print(f"\n   Root Finding Results:")
    print("   Method     │ Root 1   │ Root 2   │ Root 3   │ Function Calls")
    print("   ───────────┼──────────┼──────────┼──────────┼───────────────")
    
    # Bracketing methods (need intervals where function changes sign)
    intervals = [(0, 1.5), (1.5, 2.5), (2.5, 4)]
    
    for method_name in ['brentq', 'bisect']:
        roots = []
        total_calls = 0
        
        for a, b in intervals:
            result = optimize.root_scalar(cubic_equation, bracket=[a, b], method=method_name)
            roots.append(result.root)
            total_calls += result.function_calls
        
        print(f"   {method_name:<10} │ {roots[0]:8.6f} │ {roots[1]:8.6f} │ {roots[2]:8.6f} │ {total_calls:13d}")
    
    # Newton's method (needs initial guesses and derivative)
    newton_roots = []
    newton_calls = 0
    initial_guesses = [0.5, 1.5, 2.5]
    
    for x0 in initial_guesses:
        result = optimize.root_scalar(
            cubic_equation, x0=x0, fprime=cubic_derivative, method='newton'
        )
        newton_roots.append(result.root)
        newton_calls += result.function_calls
    
    print(f"   {'newton':<10} │ {newton_roots[0]:8.6f} │ {newton_roots[1]:8.6f} │ {newton_roots[2]:8.6f} │ {newton_calls:13d}")
    
    # Example 2: System of Nonlinear Equations
    print(f"\n🔗 Example 2: System of Nonlinear Equations")
    print("   System: x² + y² = 25")
    print("           xy = 12")
    print("   Solutions: (±3, ±4), (±4, ±3)")
    
    def system_equations(vars):
        """System of nonlinear equations"""
        x, y = vars
        eq1 = x**2 + y**2 - 25  # Circle: x² + y² = 25
        eq2 = x * y - 12        # Hyperbola: xy = 12
        return [eq1, eq2]
    
    # Find solutions with different initial guesses
    initial_guesses = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    
    print(f"\n   System Solutions:")
    print("   Initial Guess │ Solution        │ Residual     │ Success")
    print("   ──────────────┼─────────────────┼──────────────┼────────")
    
    solutions = []
    for guess in initial_guesses:
        result = optimize.root(system_equations, guess, method='hybr')
        residual = np.linalg.norm(result.fun)
        solutions.append(result.x)
        
        print(f"   {str(guess):<13} │ [{result.x[0]:6.3f}, {result.x[1]:6.3f}] │ {residual:12.2e} │ {result.success}")
    
    # Example 3: Transcendental Equation
    print(f"\n📐 Example 3: Transcendental Equation")
    print("   Equation: e^x = 3x (intersection of exponential and linear)")
    
    def transcendental(x):
        """Transcendental equation: e^x - 3x = 0"""
        return np.exp(x) - 3*x
    
    # Find intersection points
    # e^x grows faster than 3x, so there should be two intersections
    
    try:
        # First intersection (small x)
        root1 = optimize.brentq(transcendental, -1, 1)
        
        # Second intersection (larger x)  
        root2 = optimize.brentq(transcendental, 1, 2)
        
        print(f"   Intersection 1: x = {root1:.6f}, e^x = {np.exp(root1):.6f}, 3x = {3*root1:.6f}")
        print(f"   Intersection 2: x = {root2:.6f}, e^x = {np.exp(root2):.6f}, 3x = {3*root2:.6f}")
        print(f"   Verification: |e^x - 3x| = {abs(transcendental(root1)):.2e}, {abs(transcendental(root2)):.2e}")
        
    except ValueError as e:
        print(f"   Error finding roots: {e}")
        root1, root2 = None, None
    
    return {
        'cubic_roots': newton_roots,
        'system_solutions': solutions,
        'transcendental_roots': (root1, root2) if 'root1' in locals() else None
    }

# =============================================================================
# ADVANCED OPTIMIZATION TECHNIQUES
# =============================================================================

def advanced_optimization_techniques():
    """
    Advanced optimization methods including global optimization and evolutionary algorithms
    """
    print("\n🚀 ADVANCED OPTIMIZATION TECHNIQUES")
    print("=" * 36)
    
    # Example 1: Global Optimization vs Local
    print("🌍 Example 1: Global vs Local Optimization")
    print("   Function: Highly multimodal function with many local minima")
    
    def multimodal_function(x):
        """Complex function with multiple local minima"""
        return (np.sin(5*x[0]) * np.cos(5*x[1]) / 5 + 
                (x[0]**2 + x[1]**2) / 20 + 
                np.sin(x[0]) * np.sin(x[1]))
    
    bounds = [(-3, 3), (-3, 3)]
    
    # Local optimization (multiple random starts)
    print(f"\n   Local Optimization (10 random starts):")
    local_minima = []
    
    for i in range(10):
        np.random.seed(i)
        x0 = np.random.uniform(-3, 3, 2)
        result = optimize.minimize(multimodal_function, x0, method='L-BFGS-B', bounds=bounds)
        
        if result.success:
            # Check if this is a new minimum
            is_new = True
            for prev_min in local_minima:
                if np.linalg.norm(result.x - prev_min['x']) < 0.1:
                    is_new = False
                    break
            
            if is_new:
                local_minima.append({'x': result.x, 'fun': result.fun})
    
    print(f"     Found {len(local_minima)} distinct local minima:")
    for i, minimum in enumerate(local_minima, 1):
        print(f"       Local min {i}: x=({minimum['x'][0]:5.3f}, {minimum['x'][1]:5.3f}), f={minimum['fun']:8.6f}")
    
    # Global optimization
    print(f"\n   Global Optimization:")
    
    # Differential Evolution
    result_de = optimize.differential_evolution(multimodal_function, bounds, seed=42)
    print(f"     Differential Evolution: x=({result_de.x[0]:5.3f}, {result_de.x[1]:5.3f}), f={result_de.fun:8.6f}")
    
    # Basin Hopping
    result_bh = optimize.basinhopping(multimodal_function, [0, 0], niter=100, 
                                    minimizer_kwargs={'bounds': bounds})
    print(f"     Basin Hopping: x=({result_bh.x[0]:5.3f}, {result_bh.x[1]:5.3f}), f={result_bh.fun:8.6f}")
    
    # Example 2: Constrained Optimization with Penalties
    print(f"\n🔒 Example 2: Advanced Constrained Optimization")
    print("   Problem: Minimize x₁² + x₂² + x₃²")
    print("           Subject to: x₁ + x₂ + x₃ = 1")
    print("                      x₁² + x₂² ≤ 1")
    print("                      x₃ ≥ 0")
    
    def constrained_objective_3d(x):
        """3D quadratic objective"""
        return x[0]**2 + x[1]**2 + x[2]**2
    
    # Define constraints
    constraints = [
        {'type': 'eq', 'fun': lambda x: x[0] + x[1] + x[2] - 1},      # Equality constraint
        {'type': 'ineq', 'fun': lambda x: 1 - (x[0]**2 + x[1]**2)}   # Inequality constraint
    ]
    
    bounds = [(None, None), (None, None), (0, None)]  # x₃ ≥ 0
    
    # Solve with different methods
    methods = ['SLSQP', 'trust-constr']
    
    print(f"\n   Constrained Optimization Results:")
    for method in methods:
        result = optimize.minimize(
            constrained_objective_3d, [0.3, 0.3, 0.4], 
            method=method, constraints=constraints, bounds=bounds
        )
        
        print(f"     {method}: x=({result.x[0]:5.3f}, {result.x[1]:5.3f}, {result.x[2]:5.3f}), ")
        print(f"              f={result.fun:8.6f}, success={result.success}")
        
        # Verify constraints
        eq_violation = abs(result.x[0] + result.x[1] + result.x[2] - 1)
        ineq_violation = max(0, result.x[0]**2 + result.x[1]**2 - 1)
        bound_violation = max(0, -result.x[2])
        
        print(f"              Constraint violations: eq={eq_violation:.2e}, ineq={ineq_violation:.2e}, bound={bound_violation:.2e}")
    
    # Example 3: Multi-objective Optimization (Pareto Front)
    print(f"\n⚖️  Example 3: Multi-objective Optimization")
    print("   Objectives: f₁(x,y) = x² + y²")
    print("              f₂(x,y) = (x-1)² + (y-1)²")
    print("   Find Pareto optimal solutions")
    
    def objective1(x):
        """First objective: minimize distance from origin"""
        return x[0]**2 + x[1]**2
    
    def objective2(x):
        """Second objective: minimize distance from (1,1)"""
        return (x[0] - 1)**2 + (x[1] - 1)**2
    
    # Weighted sum method to find Pareto front
    pareto_solutions = []
    weights = np.linspace(0, 1, 11)
    
    for w in weights:
        def combined_objective(x):
            return w * objective1(x) + (1 - w) * objective2(x)
        
        result = optimize.minimize(combined_objective, [0.5, 0.5], method='BFGS')
        
        if result.success:
            f1_val = objective1(result.x)
            f2_val = objective2(result.x)
            pareto_solutions.append({
                'x': result.x,
                'f1': f1_val,
                'f2': f2_val,
                'weight': w
            })
    
    print(f"\n   Pareto Front Solutions (11 points):")
    print("   Weight │ x₁     │ x₂     │ f₁      │ f₂")
    print("   ───────┼────────┼────────┼─────────┼─────────")
    
    for sol in pareto_solutions:
        print(f"   {sol['weight']:6.2f} │ {sol['x'][0]:6.3f} │ {sol['x'][1]:6.3f} │ {sol['f1']:7.4f} │ {sol['f2']:7.4f}")
    
    return {
        'local_minima': local_minima,
        'global_minimum_de': result_de.x,
        'pareto_solutions': pareto_solutions
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive SciPy optimization guide
    """
    print(__doc__)
    
    # Fundamentals
    optimization_fundamentals()
    classic_results = classic_optimization_problems()
    
    # Curve fitting
    fitting_results = comprehensive_curve_fitting()
    
    # Root finding
    root_results = comprehensive_root_finding()
    
    # Advanced techniques
    advanced_results = advanced_optimization_techniques()
    
    return {
        'classic_problems': classic_results,
        'curve_fitting': fitting_results,
        'root_finding': root_results,
        'advanced_optimization': advanced_results
    }

if __name__ == "__main__":
    """
    Execute comprehensive SciPy optimization guide and demonstrations
    """
    results = main()
    
    print("\n" + "=" * 60)
    print("🎓 SCIPY OPTIMIZATION MASTERY SUMMARY")
    print("=" * 60)
    print("✅ Complete optimization fundamentals and method overview")
    print("✅ Classic optimization problems (Rosenbrock, Himmelblau)")
    print("✅ Constrained optimization with equality/inequality constraints")
    print("✅ Comprehensive curve fitting and parameter estimation")
    print("✅ Statistical model validation and uncertainty quantification")
    print("✅ Root finding algorithms and equation solving")
    print("✅ System of nonlinear equations")
    print("✅ Global optimization and evolutionary algorithms")
    print("✅ Multi-objective optimization and Pareto fronts")
    print("✅ Advanced constrained optimization techniques")
    
    print("\n💡 SciPy Optimization Mastery Key Points:")
    key_points = [
        "Choose appropriate optimization method based on problem characteristics",
        "Always validate convergence and check solution quality",
        "Use global optimization for multimodal functions",
        "Provide good initial guesses and parameter bounds",
        "Combine multiple methods for robust solutions",
        "Understand constraint formulations and penalty methods",
        "Apply statistical validation to curve fitting results",
        "Consider multi-objective approaches for real-world problems"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced Optimization Applications:")
    applications = [
        "Machine learning hyperparameter tuning",
        "Engineering design optimization",
        "Financial portfolio optimization",
        "Signal processing and system identification", 
        "Scientific model parameter estimation",
        "Operations research and logistics",
        "Control system design",
        "Data science and statistical modeling"
    ]
    
    for i, app in enumerate(applications, 1):
        print(f"   {i}. {app}")
    
    print(f"\n🚀 Ready for Advanced Mathematical Optimization!")
    print("Master the art of finding optimal solutions to complex problems!")