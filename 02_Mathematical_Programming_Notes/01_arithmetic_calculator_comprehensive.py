"""
Advanced Arithmetic Calculator - Complete Mathematical Computing Guide
====================================================================

Comprehensive arithmetic calculator system with advanced operations, error handling,
history tracking, scientific functions, expression parsing, and mathematical
utilities for professional computational applications.

Author: Python Learning Notes
Date: September 2025
Topic: Mathematical Computing, Calculator Design, Numerical Operations
"""

import math
import operator
import re
import json
import time
from decimal import Decimal, getcontext, InvalidOperation
from fractions import Fraction
from typing import Union, List, Dict, Any, Optional, Callable, Tuple
from collections import deque
import traceback

# =============================================================================
# CALCULATOR SYSTEM FUNDAMENTALS
# =============================================================================

def calculator_fundamentals():
    """
    Understanding calculator system design and mathematical computing principles
    """
    print("🧮 CALCULATOR SYSTEM FUNDAMENTALS")
    print("=" * 35)
    
    print("🎯 What is a Calculator System?")
    print("   A calculator system is a comprehensive computational tool that")
    print("   processes mathematical expressions, manages precision, handles")
    print("   errors gracefully, and provides extensive mathematical functions.")
    
    print(f"\n📋 Types of Calculator Operations:")
    operation_types = [
        ("Basic Arithmetic", "Addition, subtraction, multiplication, division", "+, -, *, /", "Fundamental operations"),
        ("Advanced Arithmetic", "Power, modulo, integer division", "**, %, //", "Extended mathematical operations"),
        ("Scientific Functions", "Trigonometry, logarithms, exponentials", "sin(), log(), exp()", "Advanced mathematical functions"),
        ("Statistical Operations", "Mean, median, standard deviation", "statistics library", "Data analysis functions"),
        ("Precision Computing", "High precision decimal operations", "Decimal class", "Financial calculations"),
        ("Expression Parsing", "Complex expression evaluation", "AST parsing", "Mathematical expression analysis"),
        ("History Management", "Operation history and recall", "Memory stack", "User experience features")
    ]
    
    print("   Type                │ Description                      │ Examples               │ Use Cases")
    print("   ────────────────────┼──────────────────────────────────┼────────────────────────┼─────────────────")
    
    for op_type, desc, examples, use_case in operation_types:
        print(f"   {op_type:<19} │ {desc:<32} │ {examples:<22} │ {use_case}")
    
    print(f"\n🔧 Calculator Design Principles:")
    print("   • Error handling and input validation for all operations")
    print("   • Precision management for accurate calculations")
    print("   • User-friendly interface with clear feedback")
    print("   • Extensible architecture for adding new functions")
    print("   • Memory management and operation history")
    print("   • Performance optimization for complex calculations")
    
    return {'operation_types': operation_types}

class AdvancedCalculator:
    """
    Advanced calculator with comprehensive mathematical operations
    """
    
    def __init__(self, precision: int = 28, history_limit: int = 100):
        """Initialize calculator with configuration"""
        self.precision = precision
        getcontext().prec = precision
        
        self.history: deque = deque(maxlen=history_limit)
        self.memory: Dict[str, Union[float, Decimal]] = {}
        self.variables: Dict[str, Union[float, Decimal]] = {}
        
        # Operation mappings
        self.basic_operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '//': operator.floordiv,
            '%': operator.mod,
            '**': operator.pow,
            '^': operator.pow  # Alternative power symbol
        }
        
        # Scientific functions
        self.scientific_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'log': math.log,
            'log10': math.log10,
            'log2': math.log2,
            'ln': math.log,
            'exp': math.exp,
            'sqrt': math.sqrt,
            'cbrt': lambda x: x ** (1/3),
            'abs': abs,
            'ceil': math.ceil,
            'floor': math.floor,
            'round': round,
            'factorial': math.factorial,
            'degrees': math.degrees,
            'radians': math.radians
        }
        
        # Mathematical constants
        self.constants = {
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau,
            'inf': math.inf,
            'nan': math.nan,
            'phi': (1 + math.sqrt(5)) / 2  # Golden ratio
        }
        
        print(f"🧮 Advanced Calculator initialized")
        print(f"   Precision: {self.precision} decimal places")
        print(f"   History limit: {history_limit} operations")
        print(f"   Available operations: {len(self.basic_operations)} basic, {len(self.scientific_functions)} scientific")

    def basic_arithmetic_operations(self):
        """
        Demonstrate and test basic arithmetic operations
        """
        print("\n➕ BASIC ARITHMETIC OPERATIONS")
        print("=" * 32)
        
        print("1️⃣ Basic Two-Number Operations:")
        
        # Test cases for basic operations
        test_cases = [
            (15.5, 4.2, '+', "Addition"),
            (20, 7, '-', "Subtraction"),
            (6.5, 3.2, '*', "Multiplication"),
            (25, 5, '/', "Division"),
            (23, 5, '//', "Integer division"),
            (23, 5, '%', "Modulo"),
            (2, 8, '**', "Power")
        ]
        
        print("   Operation examples:")
        results = []
        
        for a, b, op, name in test_cases:
            try:
                result = self.perform_operation(a, op, b)
                results.append((name, a, op, b, result))
                print(f"     {name}: {a} {op} {b} = {result}")
                
                # Log to history
                self.add_to_history(f"{a} {op} {b}", result)
                
            except Exception as e:
                print(f"     {name}: {a} {op} {b} = Error: {e}")
        
        return results

    def perform_operation(self, operand1: Union[float, int, Decimal], 
                         operation: str, 
                         operand2: Union[float, int, Decimal]) -> Union[float, Decimal]:
        """
        Perform basic arithmetic operation with error handling
        """
        # Input validation
        if not isinstance(operand1, (int, float, Decimal)):
            raise TypeError(f"First operand must be numeric, got {type(operand1)}")
        
        if not isinstance(operand2, (int, float, Decimal)):
            raise TypeError(f"Second operand must be numeric, got {type(operand2)}")
        
        if operation not in self.basic_operations:
            raise ValueError(f"Unsupported operation: {operation}")
        
        # Special case handling
        if operation == '/' and operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        if operation == '%' and operand2 == 0:
            raise ZeroDivisionError("Cannot perform modulo with zero divisor")
        
        if operation == '//' and operand2 == 0:
            raise ZeroDivisionError("Cannot perform integer division by zero")
        
        # Perform operation
        operation_func = self.basic_operations[operation]
        
        try:
            result = operation_func(operand1, operand2)
            
            # Handle special results
            if math.isnan(result):
                raise ValueError("Operation resulted in NaN (Not a Number)")
            
            if math.isinf(result):
                return float('inf') if result > 0 else float('-inf')
            
            return result
            
        except OverflowError:
            raise OverflowError("Operation resulted in numeric overflow")
        except Exception as e:
            raise ValueError(f"Operation failed: {str(e)}")

    def scientific_operations(self):
        """
        Advanced scientific and mathematical functions
        """
        print("\n🔬 SCIENTIFIC OPERATIONS")
        print("=" * 26)
        
        print("1️⃣ Trigonometric Functions:")
        
        # Trigonometric test cases
        angle_degrees = 45
        angle_radians = math.radians(angle_degrees)
        
        trig_operations = [
            ('sin', angle_radians, f"sin({angle_degrees}°)"),
            ('cos', angle_radians, f"cos({angle_degrees}°)"),
            ('tan', angle_radians, f"tan({angle_degrees}°)"),
            ('asin', 0.7071, "arcsin(0.7071)"),
            ('acos', 0.7071, "arccos(0.7071)"),
            ('atan', 1.0, "arctan(1.0)")
        ]
        
        trig_results = []
        for func_name, value, description in trig_operations:
            try:
                result = self.scientific_functions[func_name](value)
                trig_results.append((description, result))
                print(f"     {description} = {result:.6f}")
                
                # Convert back to degrees for arc functions
                if func_name.startswith('a'):
                    degrees_result = math.degrees(result)
                    print(f"       = {degrees_result:.2f}°")
                
            except Exception as e:
                print(f"     {description} = Error: {e}")
        
        print("\n2️⃣ Logarithmic and Exponential Functions:")
        
        # Logarithmic test cases
        log_operations = [
            ('log', math.e, "ln(e)"),
            ('log10', 100, "log₁₀(100)"),
            ('log2', 8, "log₂(8)"),
            ('exp', 1, "e¹"),
            ('sqrt', 16, "√16"),
            ('cbrt', 27, "∛27")
        ]
        
        log_results = []
        for func_name, value, description in log_operations:
            try:
                result = self.scientific_functions[func_name](value)
                log_results.append((description, result))
                print(f"     {description} = {result:.6f}")
            except Exception as e:
                print(f"     {description} = Error: {e}")
        
        print("\n3️⃣ Mathematical Constants:")
        
        print("     Available constants:")
        for name, value in self.constants.items():
            if not math.isnan(value) and not math.isinf(value):
                print(f"       {name} = {value:.10f}")
            else:
                print(f"       {name} = {value}")
        
        return {
            'trigonometric': trig_results,
            'logarithmic': log_results,
            'constants': self.constants
        }

    def precision_computing(self):
        """
        High-precision decimal calculations for financial and scientific applications
        """
        print("\n🎯 PRECISION COMPUTING")
        print("=" * 24)
        
        print("1️⃣ High-Precision Decimal Operations:")
        
        # Financial calculation examples
        price1 = Decimal('19.99')
        price2 = Decimal('25.49')
        tax_rate = Decimal('0.08')
        
        subtotal = price1 + price2
        tax_amount = subtotal * tax_rate
        total = subtotal + tax_amount
        
        print(f"     Financial calculation example:")
        print(f"       Item 1: ${price1}")
        print(f"       Item 2: ${price2}")
        print(f"       Subtotal: ${subtotal}")
        print(f"       Tax (8%): ${tax_amount:.2f}")
        print(f"       Total: ${total:.2f}")
        
        # Precision comparison
        print(f"\n2️⃣ Float vs Decimal Precision Comparison:")
        
        # Demonstrate precision issues with floats
        float_calc = 0.1 + 0.2
        decimal_calc = Decimal('0.1') + Decimal('0.2')
        
        print(f"     Float calculation: 0.1 + 0.2 = {float_calc}")
        print(f"     Decimal calculation: 0.1 + 0.2 = {decimal_calc}")
        print(f"     Precision difference: {abs(float(decimal_calc) - float_calc)}")
        
        # Complex precision calculations
        print(f"\n3️⃣ Complex Precision Calculations:")
        
        # Compound interest calculation
        principal = Decimal('10000.00')
        annual_rate = Decimal('0.05')  # 5%
        compounds_per_year = Decimal('12')  # Monthly
        years = Decimal('5')
        
        # A = P(1 + r/n)^(nt)
        base = 1 + (annual_rate / compounds_per_year)
        exponent = compounds_per_year * years
        final_amount = principal * (base ** exponent)
        interest_earned = final_amount - principal
        
        print(f"     Compound Interest Calculation:")
        print(f"       Principal: ${principal}")
        print(f"       Annual rate: {annual_rate * 100}%")
        print(f"       Compounded: Monthly for {years} years")
        print(f"       Final amount: ${final_amount:.2f}")
        print(f"       Interest earned: ${interest_earned:.2f}")
        
        return {
            'financial_example': {
                'subtotal': float(subtotal),
                'tax': float(tax_amount),
                'total': float(total)
            },
            'precision_comparison': {
                'float_result': float_calc,
                'decimal_result': float(decimal_calc)
            },
            'compound_interest': {
                'principal': float(principal),
                'final_amount': float(final_amount),
                'interest_earned': float(interest_earned)
            }
        }

    def expression_evaluation(self):
        """
        Advanced expression parsing and evaluation
        """
        print("\n📝 EXPRESSION EVALUATION")
        print("=" * 26)
        
        print("1️⃣ Simple Expression Parsing:")
        
        def safe_eval_expression(expression: str) -> Union[float, str]:
            """Safely evaluate mathematical expressions"""
            try:
                # Remove spaces and validate characters
                clean_expr = re.sub(r'\s+', '', expression)
                
                # Check for safe characters only
                allowed_chars = set('0123456789+-*/.()^%')
                if not all(c in allowed_chars for c in clean_expr):
                    return f"Invalid characters in expression: {expression}"
                
                # Replace ^ with ** for Python exponentiation
                clean_expr = clean_expr.replace('^', '**')
                
                # Evaluate safely (in production, use ast.literal_eval or similar)
                result = eval(clean_expr)
                
                return result
                
            except ZeroDivisionError:
                return "Division by zero error"
            except Exception as e:
                return f"Evaluation error: {str(e)}"
        
        # Test expressions
        test_expressions = [
            "2 + 3 * 4",
            "(15 + 5) / 4",
            "2^3 + 1",
            "100 / (5 - 5)",  # Division by zero test
            "2 * 3 + 4 * 5",
            "((10 + 5) * 2) / 3"
        ]
        
        expression_results = []
        print("     Expression evaluation examples:")
        
        for expr in test_expressions:
            result = safe_eval_expression(expr)
            expression_results.append((expr, result))
            print(f"       {expr} = {result}")
        
        print("\n2️⃣ Complex Expression Analysis:")
        
        def analyze_expression(expression: str) -> Dict[str, Any]:
            """Analyze mathematical expression structure"""
            analysis = {
                'original': expression,
                'length': len(expression),
                'operators': [],
                'numbers': [],
                'parentheses_count': 0,
                'complexity_score': 0
            }
            
            # Find operators
            operators = ['+', '-', '*', '/', '^', '%', '(', ')']
            for char in expression:
                if char in operators:
                    analysis['operators'].append(char)
                    if char in ['(', ')']:
                        analysis['parentheses_count'] += 1
            
            # Find numbers
            numbers = re.findall(r'\d+\.?\d*', expression)
            analysis['numbers'] = [float(num) for num in numbers]
            
            # Calculate complexity score
            analysis['complexity_score'] = (
                len(analysis['operators']) * 2 + 
                analysis['parentheses_count'] * 3 + 
                len(analysis['numbers'])
            )
            
            return analysis
        
        # Analyze complex expressions
        complex_expressions = [
            "(2 + 3) * (4 - 1) / 2",
            "10^2 + 5^2 - 3^2",
            "100 / (10 + 5) * 2 - 1"
        ]
        
        analysis_results = []
        print("     Expression analysis:")
        
        for expr in complex_expressions:
            analysis = analyze_expression(expr)
            analysis_results.append(analysis)
            print(f"       Expression: {expr}")
            print(f"         Numbers: {len(analysis['numbers'])}")
            print(f"         Operators: {len(analysis['operators'])}")
            print(f"         Complexity: {analysis['complexity_score']}")
            
            # Evaluate the expression
            result = safe_eval_expression(expr)
            print(f"         Result: {result}")
        
        return {
            'simple_expressions': expression_results,
            'complex_analysis': analysis_results
        }

    def calculator_memory_system(self):
        """
        Memory and history management system
        """
        print("\n💾 MEMORY AND HISTORY SYSTEM")
        print("=" * 30)
        
        print("1️⃣ Memory Operations:")
        
        # Memory storage operations
        self.memory['M1'] = 42.5
        self.memory['M2'] = 100.0
        self.memory['result'] = 15.75
        
        print("     Memory storage:")
        for key, value in self.memory.items():
            print(f"       {key}: {value}")
        
        # Memory recall and operations
        memory_calc = self.memory['M1'] + self.memory['M2']
        self.memory['sum'] = memory_calc
        
        print(f"     Memory calculation: M1 + M2 = {memory_calc}")
        
        print("\n2️⃣ Operation History:")
        
        # Add some operations to history
        sample_operations = [
            ("15 + 25", 40),
            ("100 / 4", 25),
            ("2^8", 256),
            ("sin(30°)", 0.5),
            ("√144", 12)
        ]
        
        for operation, result in sample_operations:
            self.add_to_history(operation, result)
        
        # Display history
        print("     Recent calculations:")
        for i, entry in enumerate(self.history, 1):
            timestamp = entry.get('timestamp', 'N/A')
            operation = entry.get('operation', 'N/A')
            result = entry.get('result', 'N/A')
            print(f"       {i}. {operation} = {result}")
        
        print("\n3️⃣ Variable System:")
        
        # Variable assignments
        self.variables['x'] = 10
        self.variables['y'] = 5
        self.variables['radius'] = 7
        
        # Calculate using variables
        area = math.pi * self.variables['radius'] ** 2
        self.variables['circle_area'] = area
        
        print("     Variables:")
        for var, value in self.variables.items():
            print(f"       {var} = {value}")
        
        return {
            'memory_slots': len(self.memory),
            'history_entries': len(self.history),
            'variables': len(self.variables)
        }

    def add_to_history(self, operation: str, result: Union[float, str]) -> None:
        """Add operation to history with timestamp"""
        entry = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'operation': operation,
            'result': result
        }
        self.history.append(entry)

    def statistical_operations(self):
        """
        Statistical and data analysis operations
        """
        print("\n📊 STATISTICAL OPERATIONS")
        print("=" * 27)
        
        # Sample data sets
        data_sets = {
            'test_scores': [85, 92, 78, 96, 88, 91, 87, 94, 82, 90],
            'temperatures': [23.5, 25.1, 22.8, 26.3, 24.7, 23.9, 25.8, 24.2],
            'sales_data': [1200, 1350, 1180, 1420, 1290, 1380, 1150, 1475, 1320]
        }
        
        statistical_results = {}
        
        for dataset_name, data in data_sets.items():
            print(f"\n     Dataset: {dataset_name.replace('_', ' ').title()}")
            print(f"     Data: {data}")
            
            # Calculate statistics
            stats = {
                'count': len(data),
                'sum': sum(data),
                'mean': sum(data) / len(data),
                'min': min(data),
                'max': max(data),
                'range': max(data) - min(data)
            }
            
            # Calculate median
            sorted_data = sorted(data)
            n = len(sorted_data)
            if n % 2 == 0:
                stats['median'] = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
            else:
                stats['median'] = sorted_data[n//2]
            
            # Calculate standard deviation
            mean = stats['mean']
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            stats['std_dev'] = math.sqrt(variance)
            
            statistical_results[dataset_name] = stats
            
            # Display results
            print(f"       Count: {stats['count']}")
            print(f"       Sum: {stats['sum']:.2f}")
            print(f"       Mean: {stats['mean']:.2f}")
            print(f"       Median: {stats['median']:.2f}")
            print(f"       Min: {stats['min']:.2f}")
            print(f"       Max: {stats['max']:.2f}")
            print(f"       Range: {stats['range']:.2f}")
            print(f"       Std Dev: {stats['std_dev']:.2f}")
        
        return statistical_results

    def interactive_calculator_demo(self):
        """
        Demonstrate interactive calculator functionality
        """
        print("\n🎮 INTERACTIVE CALCULATOR DEMO")
        print("=" * 32)
        
        print("     Calculator Commands Available:")
        commands = [
            "basic <num1> <op> <num2>  - Basic arithmetic",
            "sci <function> <value>    - Scientific function",
            "expr <expression>         - Evaluate expression",
            "history                   - Show calculation history",
            "memory <slot> <value>     - Store in memory",
            "recall <slot>             - Recall from memory",
            "stats <data>              - Statistical analysis",
            "precision <digits>        - Set precision",
            "constants                 - Show mathematical constants"
        ]
        
        for command in commands:
            print(f"       {command}")
        
        # Simulate some interactive commands
        demo_commands = [
            ("basic", [25, "+", 15]),
            ("sci", ["sqrt", 64]),
            ("expr", ["(10 + 5) * 2"]),
            ("constants", [])
        ]
        
        print(f"\n     Demo command execution:")
        
        for command_type, args in demo_commands:
            if command_type == "basic" and len(args) == 3:
                try:
                    result = self.perform_operation(args[0], args[1], args[2])
                    print(f"       > {command_type} {' '.join(map(str, args))} = {result}")
                except Exception as e:
                    print(f"       > {command_type} {' '.join(map(str, args))} = Error: {e}")
            
            elif command_type == "sci" and len(args) == 2:
                func_name, value = args
                if func_name in self.scientific_functions:
                    try:
                        result = self.scientific_functions[func_name](value)
                        print(f"       > {command_type} {func_name}({value}) = {result:.6f}")
                    except Exception as e:
                        print(f"       > {command_type} {func_name}({value}) = Error: {e}")
            
            elif command_type == "expr" and len(args) == 1:
                expression = args[0]
                result = eval(expression)  # In production, use safer evaluation
                print(f"       > {command_type} '{expression}' = {result}")
            
            elif command_type == "constants":
                print(f"       > Available constants: {', '.join(self.constants.keys())}")
        
        return {
            'available_commands': len(commands),
            'demo_executions': len(demo_commands)
        }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive calculator system
    """
    print(__doc__)
    
    # Initialize calculator system
    fundamentals = calculator_fundamentals()
    calculator = AdvancedCalculator(precision=10, history_limit=50)
    
    # Execute comprehensive demonstrations
    basic_operations = calculator.basic_arithmetic_operations()
    scientific_ops = calculator.scientific_operations()
    precision_computing = calculator.precision_computing()
    expression_eval = calculator.expression_evaluation()
    memory_system = calculator.calculator_memory_system()
    statistics = calculator.statistical_operations()
    interactive_demo = calculator.interactive_calculator_demo()
    
    return {
        'fundamentals': fundamentals,
        'calculator_instance': calculator,
        'basic_operations': basic_operations,
        'scientific_operations': scientific_ops,
        'precision_computing': precision_computing,
        'expression_evaluation': expression_eval,
        'memory_system': memory_system,
        'statistical_operations': statistics,
        'interactive_demo': interactive_demo
    }

if __name__ == "__main__":
    """
    Execute comprehensive arithmetic calculator demonstration
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 ADVANCED ARITHMETIC CALCULATOR MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete calculator system with advanced mathematical operations")
    print("✅ Comprehensive error handling and input validation")
    print("✅ High-precision decimal computing for financial applications")
    print("✅ Scientific functions including trigonometry and logarithms")
    print("✅ Expression parsing and complex calculation evaluation")
    print("✅ Memory management and operation history tracking")
    print("✅ Statistical operations and data analysis capabilities")
    print("✅ Interactive command system and user interface design")
    
    print("\n💡 Calculator System Excellence Key Points:")
    key_points = [
        "Robust error handling prevents crashes and provides meaningful feedback",
        "High-precision arithmetic ensures accurate financial and scientific calculations",
        "Comprehensive operation support covers basic to advanced mathematical functions",
        "Memory and history systems enhance user experience and workflow efficiency",
        "Expression parsing enables complex mathematical computations",
        "Statistical functions support data analysis and scientific applications",
        "Modular design allows easy extension and customization",
        "Professional-grade validation ensures reliable computational results"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Professional Calculator Applications:")
    applications = [
        "Financial modeling and investment calculations",
        "Scientific research and engineering computations",
        "Educational tools for mathematics and statistics",
        "Business analytics and data analysis systems",
        "Quality control and measurement applications",
        "Game development and simulation mathematics",
        "Cryptocurrency and blockchain calculations",
        "Academic research and statistical analysis"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master Mathematical Computing with Professional Calculator Systems!")
    print("Advanced calculators are the foundation of computational excellence!")

# =============================================================================
# ORIGINAL SIMPLE CALCULATOR (Enhanced with Context)
# =============================================================================

# Enhanced version of the original simple calculator
print("\n" + "=" * 60)
print("ENHANCED VERSION OF ORIGINAL SIMPLE CALCULATOR")
print("=" * 60)

def enhanced_simple_calculator():
    """Enhanced version of the original basic calculator"""
    
    print("🧮 Enhanced Simple Calculator")
    print("This is the original calculator enhanced with modern practices:")
    
    def get_number(prompt: str) -> float:
        """Get a valid number from user with error handling"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("   ❌ Invalid input! Please enter a valid number.")
                continue
    
    def get_operator() -> str:
        """Get a valid operator from user"""
        valid_operators = ['+', '-', '*', '/']
        while True:
            operator = input("Enter the arithmetic operator (+, -, *, /): ").strip()
            if operator in valid_operators:
                return operator
            else:
                print(f"   ❌ Invalid operator! Please use one of: {', '.join(valid_operators)}")
                continue
    
    def perform_calculation(a: float, operator: str, b: float) -> str:
        """Perform calculation with proper error handling"""
        try:
            if operator == "+":
                result = a + b
                return f"The result of addition is {result}"
            elif operator == "-":
                result = a - b
                return f"The result of subtraction is {result}"
            elif operator == "*":
                result = a * b
                return f"The result of multiplication is {result}"
            elif operator == "/":
                if b == 0:
                    return "❌ Error: Cannot divide by zero!"
                result = a / b
                return f"The result of division is {result}"
        except Exception as e:
            return f"❌ Calculation error: {e}"
        
        return "❌ Unknown operator"
    
    # Demonstrate the enhanced calculator
    print("\n   Demonstration with sample values:")
    test_cases = [
        (25.5, '+', 14.3),
        (50, '-', 23),
        (7.5, '*', 4),
        (100, '/', 8),
        (10, '/', 0)  # Division by zero test
    ]
    
    for a, op, b in test_cases:
        result_message = perform_calculation(a, op, b)
        print(f"     {a} {op} {b}: {result_message}")
    
    print("\n   Key improvements over original version:")
    improvements = [
        "✅ Input validation with error handling",
        "✅ Division by zero protection",
        "✅ Clear error messages and user feedback",
        "✅ Modular function design for maintainability",
        "✅ Type hints for better code documentation",
        "✅ Comprehensive testing with sample cases"
    ]
    
    for improvement in improvements:
        print(f"     {improvement}")

# Execute the enhanced simple calculator
enhanced_simple_calculator()

print("\n" + "=" * 60)
print("From basic calculator to professional computing system!")
print("This demonstrates the evolution from simple scripts to robust applications.")
print("=" * 60)