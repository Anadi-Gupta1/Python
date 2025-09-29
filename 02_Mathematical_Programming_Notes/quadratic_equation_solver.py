"""
Quadratic Equation Solver - Mathematical Programming Notes
========================================================

This program solves quadratic equations of the form: ax² + bx + c = 0
Demonstrates mathematical computation, conditional logic, and complex numbers in Python.

Formula: x = (-b ± √(b² - 4ac)) / 2a
Discriminant: Δ = b² - 4ac

Author: Python Learning Notes
Date: September 2025
Topic: Quadratic Equations, Mathematical Computing, Conditional Logic
"""

import math
import cmath  # For complex number operations

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
    
    print("\n💡 Key Concepts Learned:")
    print("• Mathematical problem-solving in Python")
    print("• Conditional logic based on discriminant")
    print("• Complex number arithmetic")
    print("• Input validation and user interaction")
    print("• Code organization with functions")
