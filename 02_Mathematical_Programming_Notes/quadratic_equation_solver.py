"""
Quadratic Equation Solver - Mathematical Programming Notes
========================================================

This program solves quadratic equations of the form: ax² + bx + c = 0
Demonstrates mathematical computation, conditional logic, and complex numbers in Python.

Formula: x = (-b ± √(b² - 4ac)) / 2a
Discriminant: Δ = b² - 4ac

Author: Python Learning Notes
Date: September 2025
Last Updated: October 3, 2025
Topic: Quadratic Equations, Mathematical Computing, Conditional Logic
Version: 1.1
"""

import math
import cmath  # For complex number operations
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, Dict, List, Optional

# =============================================================================
# QUADRATIC EQUATION THEORY
# =============================================================================

def explain_quadratic_equations():
    """
    Educational explanation of quadratic equations
    """
    print("📐 QUADRATIC EQUATION SOLVER")
    print("=" * 40)
    
    print("\n📋 What is a Quadratic Equation?")
    print("A quadratic equation is a polynomial equation of degree 2:")
    print("   ax² + bx + c = 0")
    print("   where a ≠ 0")
    
    print("\n🔍 Components:")
    print("   • a: coefficient of x² (quadratic term)")
    print("   • b: coefficient of x (linear term)")  
    print("   • c: constant term")
    
    print("\n📊 The Discriminant (Δ = b² - 4ac) determines:")
    print("   • Δ > 0: Two distinct real roots")
    print("   • Δ = 0: One repeated real root")
    print("   • Δ < 0: Two complex conjugate roots")

# =============================================================================
# QUADRATIC SOLVER FUNCTIONS
# =============================================================================

def get_coefficients():
    """
    Get coefficients from user with input validation
    """
    while True:
        try:
            print("\n📝 Enter coefficients for ax² + bx + c = 0:")
            a = float(input("Enter coefficient 'a' (≠ 0): "))
            
            if a == 0:
                print("❌ Error: 'a' cannot be zero for quadratic equation!")
                continue
                
            b = float(input("Enter coefficient 'b': "))
            c = float(input("Enter constant 'c': "))
            
            return a, b, c
            
        except ValueError:
            print("❌ Error: Please enter valid numbers!")

def calculate_discriminant(a, b, c):
    """
    Calculate and analyze discriminant
    
    Args:
        a, b, c: Coefficients of quadratic equation
    
    Returns:
        discriminant: The discriminant value
    """
    discriminant = b*b - 4*a*c
    
    print(f"\n🧮 Calculating Discriminant:")
    print(f"   Δ = b² - 4ac")
    print(f"   Δ = ({b})² - 4({a})({c})")
    print(f"   Δ = {b*b} - {4*a*c}")
    print(f"   Δ = {discriminant}")
    
    return discriminant

def solve_quadratic_real_roots(a, b, discriminant):
    """
    Solve quadratic equation with real roots
    
    Args:
        a, b: Coefficients
        discriminant: Discriminant value (≥ 0)
    
    Returns:
        tuple: The real roots
    """
    sqrt_discriminant = math.sqrt(discriminant)
    
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    print(f"\n✅ Real Roots Calculation:")
    print(f"   x₁ = (-b + √Δ) / 2a = ({-b} + {sqrt_discriminant:.4f}) / {2*a} = {root1:.4f}")
    print(f"   x₂ = (-b - √Δ) / 2a = ({-b} - {sqrt_discriminant:.4f}) / {2*a} = {root2:.4f}")
    
    return root1, root2

def solve_quadratic_complex_roots(a, b, discriminant):
    """
    Solve quadratic equation with complex roots
    
    Args:
        a, b: Coefficients
        discriminant: Discriminant value (< 0)
    
    Returns:
        tuple: The complex roots
    """
    sqrt_discriminant = cmath.sqrt(discriminant)
    
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    print(f"\n🔢 Complex Roots Calculation:")
    print(f"   x₁ = (-b + √Δ) / 2a = {root1}")
    print(f"   x₂ = (-b - √Δ) / 2a = {root2}")
    
    return root1, root2

def solve_quadratic_equation(a, b, c):
    """
    Complete quadratic equation solver
    
    Args:
        a, b, c: Coefficients of the quadratic equation
    """
    print(f"\n🎯 Solving: {a}x² + {b}x + {c} = 0")
    
    # Calculate discriminant
    discriminant = calculate_discriminant(a, b, c)
    
    # Determine nature of roots
    if discriminant > 0:
        print(f"\n📈 Since Δ = {discriminant} > 0:")
        print("   The equation has TWO DISTINCT REAL ROOTS")
        
        root1, root2 = solve_quadratic_real_roots(a, b, discriminant)
        
        print(f"\n🎯 SOLUTION:")
        print(f"   Root 1: x₁ = {root1:.6f}")
        print(f"   Root 2: x₂ = {root2:.6f}")
        
        return root1, root2
        
    elif discriminant == 0:
        print(f"\n📊 Since Δ = {discriminant} = 0:")
        print("   The equation has ONE REPEATED REAL ROOT")
        
        root = -b / (2 * a)
        
        print(f"\n✅ Repeated Root Calculation:")
        print(f"   x = -b / 2a = {-b} / {2*a} = {root:.6f}")
        
        print(f"\n🎯 SOLUTION:")
        print(f"   Repeated Root: x = {root:.6f}")
        
        return root, root
        
    else:  # discriminant < 0
        print(f"\n📉 Since Δ = {discriminant} < 0:")
        print("   The equation has TWO COMPLEX CONJUGATE ROOTS")
        
        root1, root2 = solve_quadratic_complex_roots(a, b, discriminant)
        
        print(f"\n🎯 SOLUTION:")
        print(f"   Root 1: x₁ = {root1}")
        print(f"   Root 2: x₂ = {root2}")
        
        return root1, root2

def verify_solution(a, b, c, roots):
    """
    Verify the solution by substituting back into original equation
    
    Args:
        a, b, c: Original coefficients
        roots: Tuple of calculated roots
    """
    print(f"\n🔍 VERIFICATION:")
    print("Substituting roots back into the original equation:")
    
    root1, root2 = roots
    
    # Verify root1
    if isinstance(root1, complex):
        result1 = a * root1**2 + b * root1 + c
        print(f"   For x₁ = {root1}:")
        print(f"   {a}({root1})² + {b}({root1}) + {c} = {result1}")
    else:
        result1 = a * root1**2 + b * root1 + c
        print(f"   For x₁ = {root1:.6f}:")
        print(f"   {a}({root1:.6f})² + {b}({root1:.6f}) + {c} = {result1:.10f}")
    
    # Verify root2 (if different)
    if root1 != root2:
        if isinstance(root2, complex):
            result2 = a * root2**2 + b * root2 + c
            print(f"   For x₂ = {root2}:")
            print(f"   {a}({root2})² + {b}({root2}) + {c} = {result2}")
        else:
            result2 = a * root2**2 + b * root2 + c
            print(f"   For x₂ = {root2:.6f}:")
            print(f"   {a}({root2:.6f})² + {b}({root2:.6f}) + {c} = {result2:.10f}")

def demonstrate_examples():
    """
    Demonstrate solving different types of quadratic equations
    """
    print("\n🌟 EXAMPLE PROBLEMS")
    print("=" * 30)
    
    examples = [
        (1, -5, 6),    # Two distinct real roots
        (1, -4, 4),    # One repeated root
        (1, 0, 1),     # Two complex roots
        (2, -3, -2),   # Two distinct real roots
    ]
    
    for i, (a, b, c) in enumerate(examples, 1):
        print(f"\n📝 Example {i}:")
        roots = solve_quadratic_equation(a, b, c)
        verify_solution(a, b, c, roots)
        print("-" * 40)

def interactive_solver():
    """
    Interactive quadratic equation solver
    """
    print("\n🚀 INTERACTIVE QUADRATIC SOLVER")
    print("=" * 40)
    
    while True:
        try:
            # Get coefficients from user
            a, b, c = get_coefficients()
            
            # Solve the equation
            roots = solve_quadratic_equation(a, b, c)
            
            # Verify the solution
            verify_solution(a, b, c, roots)
            
            # Ask if user wants to solve another equation
            again = input("\n❓ Solve another equation? (y/n): ").lower().strip()
            if again not in ['y', 'yes']:
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    """
    Main execution block
    """
    print(__doc__)
    
    # Explain theory
    explain_quadratic_equations()
    
    # Show examples
    demonstrate_examples()
    
    # Interactive solver
    interactive_solver()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of quadratic equations")
    print("✅ Knowledge of discriminant and root types")
    print("✅ Implementation of mathematical formulas")
    print("✅ Handling of complex numbers")
    print("✅ Input validation and error handling")
    print("✅ Solution verification techniques")
    print("✅ Graphical representation of parabolas")
    print("✅ Discriminant analysis and classification")
    
    print("\n💡 Key Concepts Learned:")
    print("• Mathematical problem-solving in Python")
    print("• Conditional logic based on discriminant")
    print("• Complex number arithmetic")
    print("• Input validation and user interaction")
    print("• Data visualization with matplotlib")
    print("• Mathematical analysis and interpretation")

def plot_quadratic_function(a: float, b: float, c: float, roots: List[complex] = None) -> None:
    """
    Plot the quadratic function and highlight roots
    
    Args:
        a, b, c: Coefficients of quadratic equation
        roots: List of roots to highlight
    """
    print(f"\n📊 Plotting quadratic function: {a}x² + {b}x + {c}")
    
    # Create x values
    discriminant = b**2 - 4*a*c
    
    # Determine x range based on roots
    if roots and all(isinstance(root, (int, float, complex)) for root in roots):
        real_roots = [root.real for root in roots if isinstance(root, complex) and root.imag == 0] or \
                    [root for root in roots if isinstance(root, (int, float))]
        
        if real_roots:
            min_root, max_root = min(real_roots), max(real_roots)
            x_range = max(abs(min_root), abs(max_root)) * 1.5
            x = np.linspace(min_root - x_range/2, max_root + x_range/2, 400)
        else:
            # Complex roots - center around vertex
            vertex_x = -b / (2 * a)
            x_range = max(10, abs(vertex_x) * 2)
            x = np.linspace(vertex_x - x_range, vertex_x + x_range, 400)
    else:
        vertex_x = -b / (2 * a) if a != 0 else 0
        x_range = max(10, abs(vertex_x) * 2)
        x = np.linspace(vertex_x - x_range, vertex_x + x_range, 400)
    
    # Calculate y values
    y = a * x**2 + b * x + c
    
    # Create the plot
    plt.figure(figsize=(10, 8))
    
    # Plot the parabola
    plt.plot(x, y, 'b-', linewidth=2, label=f'y = {a}x² + {b}x + {c}')
    
    # Plot x-axis
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Highlight real roots
    if roots:
        real_roots = []
        for root in roots:
            if isinstance(root, complex):
                if abs(root.imag) < 1e-10:  # Essentially real
                    real_roots.append(root.real)
            elif isinstance(root, (int, float)):
                real_roots.append(root)
        
        if real_roots:
            plt.scatter(real_roots, [0]*len(real_roots), color='red', s=100, zorder=5, 
                       label=f'Roots: {", ".join([f"{r:.2f}" for r in real_roots])}')
    
    # Mark vertex
    vertex_x = -b / (2 * a) if a != 0 else 0
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.scatter([vertex_x], [vertex_y], color='green', s=100, zorder=5, 
               label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')
    
    # Formatting
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title(f'Quadratic Function: f(x) = {a}x² + {b}x + {c}\n' + 
             f'Discriminant: Δ = {discriminant:.2f}', fontsize=14)
    plt.legend()
    
    # Add discriminant information
    if discriminant > 0:
        discriminant_text = "Two distinct real roots"
        color = 'green'
    elif discriminant == 0:
        discriminant_text = "One repeated real root"
        color = 'orange'
    else:
        discriminant_text = "Two complex conjugate roots"
        color = 'red'
    
    plt.text(0.02, 0.98, f'Analysis: {discriminant_text}', transform=plt.gca().transAxes,
             bbox=dict(boxstyle='round', facecolor=color, alpha=0.3),
             verticalalignment='top', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    print(f"✅ Graph plotted successfully!")

def analyze_discriminant_detailed(a: float, b: float, c: float) -> Dict[str, any]:
    """
    Perform detailed discriminant analysis
    
    Args:
        a, b, c: Coefficients of quadratic equation
        
    Returns:
        Dictionary containing detailed analysis
    """
    discriminant = b**2 - 4*a*c
    
    analysis = {
        'discriminant': discriminant,
        'equation': f"{a}x² + {b}x + {c} = 0",
        'vertex': (-b/(2*a), -(discriminant)/(4*a)) if a != 0 else (None, None),
        'axis_of_symmetry': -b/(2*a) if a != 0 else None,
        'opens': 'upward' if a > 0 else 'downward',
        'y_intercept': c
    }
    
    if discriminant > 0:
        analysis['root_type'] = 'Two distinct real roots'
        analysis['root_nature'] = 'Real and unequal'
        analysis['graph_intersections'] = 'Crosses x-axis at two points'
    elif discriminant == 0:
        analysis['root_type'] = 'One repeated real root'
        analysis['root_nature'] = 'Real and equal'
        analysis['graph_intersections'] = 'Touches x-axis at one point'
    else:
        analysis['root_type'] = 'Two complex conjugate roots'
        analysis['root_nature'] = 'Complex conjugates'
        analysis['graph_intersections'] = 'Does not intersect x-axis'
    
    # Additional properties
    if a != 0:
        analysis['is_minimum'] = a > 0
        analysis['is_maximum'] = a < 0
        analysis['extremum_value'] = -(discriminant)/(4*a)
    
    return analysis

def print_detailed_analysis(analysis: Dict[str, any]) -> None:
    """
    Print detailed analysis of the quadratic equation
    """
    print(f"\n🔍 DETAILED MATHEMATICAL ANALYSIS")
    print("=" * 45)
    
    print(f"📐 Equation: {analysis['equation']}")
    print(f"📊 Discriminant (Δ): {analysis['discriminant']:.4f}")
    print(f"🎯 Root Type: {analysis['root_type']}")
    print(f"🔗 Root Nature: {analysis['root_nature']}")
    print(f"📈 Graph: {analysis['graph_intersections']}")
    
    if analysis['vertex'][0] is not None:
        print(f"\n📍 Key Points:")
        print(f"   • Vertex: ({analysis['vertex'][0]:.4f}, {analysis['vertex'][1]:.4f})")
        print(f"   • Axis of symmetry: x = {analysis['axis_of_symmetry']:.4f}")
        print(f"   • Y-intercept: (0, {analysis['y_intercept']})")
        print(f"   • Parabola opens: {analysis['opens']}")
        
        if 'is_minimum' in analysis:
            extremum_type = "minimum" if analysis['is_minimum'] else "maximum"
            print(f"   • {extremum_type.title()} value: {analysis['extremum_value']:.4f}")

def enhanced_quadratic_solver():
    """
    Enhanced quadratic solver with graphical representation and detailed analysis
    """
    print(f"\n🚀 ENHANCED QUADRATIC EQUATION SOLVER")
    print("=" * 42)
    print("Features: Solution finding, graphical plotting, and detailed analysis")
    
    while True:
        try:
            print(f"\n📝 Enter coefficients for equation ax² + bx + c = 0:")
            
            # Get coefficients
            a, b, c = get_coefficients()
            
            # Solve equation
            roots = solve_quadratic_equation(a, b, c)
            
            # Detailed analysis
            analysis = analyze_discriminant_detailed(a, b, c)
            print_detailed_analysis(analysis)
            
            # Verify solution
            verify_solution(a, b, c, roots)
            
            # Ask about plotting
            plot_choice = input(f"\n📊 Would you like to see the graph? (y/n): ").lower().strip()
            if plot_choice in ['y', 'yes']:
                try:
                    plot_quadratic_function(a, b, c, roots)
                except Exception as e:
                    print(f"⚠️  Plotting error: {e}")
                    print("📝 Note: Make sure matplotlib is installed for graphing")
            
            # Continue prompt
            again = input(f"\n❓ Analyze another equation? (y/n): ").lower().strip()
            if again not in ['y', 'yes']:
                break
                
        except KeyboardInterrupt:
            print(f"\n\n👋 Enhanced solver terminated!")
            break
        except Exception as e:
            print(f"\n❌ Error in enhanced solver: {e}")

# Enhanced demonstration examples
def demonstrate_enhanced_examples():
    """
    Demonstrate enhanced examples with analysis and plotting
    """
    print(f"\n🎯 ENHANCED DEMONSTRATION EXAMPLES")
    print("=" * 37)
    
    examples = [
        (1, -5, 6, "Two distinct real roots"),      # (x-2)(x-3) = 0
        (1, -4, 4, "One repeated real root"),       # (x-2)² = 0  
        (1, 0, 1, "Two complex conjugate roots"),   # x² + 1 = 0
        (2, -8, 6, "Two distinct real roots"),      # More complex coefficients
        (-1, 2, 3, "Downward opening parabola")     # Negative leading coefficient
    ]
    
    for i, (a, b, c, description) in enumerate(examples, 1):
        print(f"\n📋 Example {i}: {description}")
        print(f"   Equation: {a}x² + {b}x + {c} = 0")
        
        # Solve
        roots = solve_quadratic_equation(a, b, c)
        
        # Quick analysis
        analysis = analyze_discriminant_detailed(a, b, c)
        print(f"   Discriminant: {analysis['discriminant']:.2f}")
        print(f"   Vertex: ({analysis['vertex'][0]:.2f}, {analysis['vertex'][1]:.2f})")
        print(f"   Nature: {analysis['root_nature']}")

if __name__ == "__main__":
    """
    Main execution block with enhanced features
    """
    print(__doc__)
    
    # Explain theory
    explain_quadratic_equations()
    
    # Enhanced examples
    demonstrate_enhanced_examples()
    
    # Original solver
    print(f"\n🔧 BASIC INTERACTIVE SOLVER")
    print("=" * 30)
    choice = input("Run basic solver? (y/n): ").lower().strip()
    if choice in ['y', 'yes']:
        interactive_solver()
    
    # Enhanced solver
    print(f"\n🚀 ENHANCED SOLVER WITH GRAPHICS")
    print("=" * 35)
    choice = input("Run enhanced solver with plotting? (y/n): ").lower().strip()
    if choice in ['y', 'yes']:
        enhanced_quadratic_solver()
    print("• Code organization with functions")
