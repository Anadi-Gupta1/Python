"""
NumPy Array Creation Operations - Complete Guide to Array Generation
===================================================================

Master class covering all methods of creating NumPy arrays including basic creation,
specialized functions, random arrays, structured arrays, and advanced techniques
with performance analysis and practical applications.

Author: Python Learning Notes
Date: September 2025
Topic: NumPy Array Creation, Array Generation, Memory Management
"""

import numpy as np
import time
import sys
from typing import List, Tuple, Union, Optional, Any
import warnings

# =============================================================================
# ARRAY CREATION THEORY AND CONCEPTS
# =============================================================================

def explain_array_creation_concepts():
    """
    Educational explanation of NumPy array creation concepts
    """
    print("🎨 NUMPY ARRAY CREATION CONCEPTS")
    print("=" * 35)
    
    print("\n📚 Why Master Array Creation?")
    print("Array creation is fundamental because:")
    print("   • Proper initialization affects performance")
    print("   • Different methods suit different use cases")
    print("   • Memory layout impacts computational efficiency")
    print("   • Data types affect storage and precision")
    print("   • Shape and dimensions determine capabilities")
    
    print("\n🔄 Array Creation Categories:")
    categories = [
        ("From Data", "Lists, tuples, existing arrays", "Direct conversion"),
        ("Intrinsic", "zeros, ones, empty, full", "Built-in patterns"),
        ("Range-based", "arange, linspace, logspace", "Sequence generation"),
        ("Random", "random, normal, uniform", "Statistical distributions"),
        ("Special", "identity, diagonal, meshgrid", "Mathematical structures"),
        ("File-based", "loadtxt, genfromtxt, load", "External data sources")
    ]
    
    print("   ┌─────────────┬─────────────────────┬─────────────────────┐")
    print("   │ Category    │ Methods             │ Primary Use         │")
    print("   ├─────────────┼─────────────────────┼─────────────────────┤")
    for category, methods, use in categories:
        print(f"   │ {category:<11} │ {methods:<19} │ {use:<19} │")
    print("   └─────────────┴─────────────────────┴─────────────────────┘")
    
    print("\n⚡ Performance Considerations:")
    print("   • Memory allocation strategies")
    print("   • Data type selection for efficiency")
    print("   • Contiguous vs non-contiguous arrays")
    print("   • Broadcasting implications")
    print("   • Cache-friendly access patterns")

# =============================================================================
# BASIC ARRAY CREATION METHODS
# =============================================================================

class ArrayCreator:
    """
    Comprehensive array creation utility with performance tracking
    """
    
    def __init__(self):
        """Initialize array creator with performance tracking"""
        self.creation_log = []
        self.total_operations = 0
    
    def log_creation(self, method: str, shape: tuple, dtype: str, time_ms: float):
        """Log array creation for performance analysis"""
        self.creation_log.append({
            'method': method,
            'shape': shape,
            'dtype': dtype,
            'time_ms': time_ms,
            'memory_mb': self._calculate_memory(shape, dtype)
        })
        self.total_operations += 1
    
    def _calculate_memory(self, shape: tuple, dtype: str) -> float:
        """Calculate memory usage in MB"""
        try:
            size = np.prod(shape)
            dtype_size = np.dtype(dtype).itemsize
            return (size * dtype_size) / (1024 * 1024)
        except:
            return 0.0
    
    # =========================================================================
    # FROM EXISTING DATA
    # =========================================================================
    
    def from_python_data(self) -> None:
        """
        Create arrays from Python data structures
        """
        print("\n🔄 CREATING ARRAYS FROM PYTHON DATA")
        print("=" * 40)
        
        # From Python lists
        print("\n1️⃣  From Python Lists:")
        
        # 1D array
        list_1d = [1, 2, 3, 4, 5]
        start_time = time.time()
        array_1d = np.array(list_1d)
        creation_time = (time.time() - start_time) * 1000
        
        print(f"   Original list: {list_1d}")
        print(f"   NumPy array: {array_1d}")
        print(f"   Shape: {array_1d.shape}, Dtype: {array_1d.dtype}")
        print(f"   Creation time: {creation_time:.3f} ms")
        
        self.log_creation('array_from_list_1d', array_1d.shape, str(array_1d.dtype), creation_time)
        
        # 2D array
        list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        start_time = time.time()
        array_2d = np.array(list_2d)
        creation_time = (time.time() - start_time) * 1000
        
        print(f"\n   Original 2D list: {list_2d}")
        print(f"   NumPy 2D array:\n{array_2d}")
        print(f"   Shape: {array_2d.shape}, Dtype: {array_2d.dtype}")
        print(f"   Creation time: {creation_time:.3f} ms")
        
        self.log_creation('array_from_list_2d', array_2d.shape, str(array_2d.dtype), creation_time)
        
        # From tuples
        print("\n2️⃣  From Tuples:")
        tuple_data = (10, 20, 30, 40)
        array_from_tuple = np.array(tuple_data)
        print(f"   Tuple: {tuple_data}")
        print(f"   Array: {array_from_tuple}")
        
        # Mixed data types
        print("\n3️⃣  Mixed Data Types:")
        mixed_list = [1, 2.5, 3]
        mixed_array = np.array(mixed_list)
        print(f"   Mixed list: {mixed_list}")
        print(f"   Array (auto dtype): {mixed_array}")
        print(f"   Dtype: {mixed_array.dtype}")
        
        # Explicit dtype specification
        int_array = np.array(mixed_list, dtype=np.int32)
        print(f"   Forced int32: {int_array}")
        print(f"   Dtype: {int_array.dtype}")
        
        # String arrays
        print("\n4️⃣  String Arrays:")
        string_list = ['apple', 'banana', 'cherry']
        string_array = np.array(string_list)
        print(f"   String list: {string_list}")
        print(f"   String array: {string_array}")
        print(f"   Dtype: {string_array.dtype}")
    
    def from_ranges(self) -> None:
        """
        Create arrays using range-based functions
        """
        print("\n📐 RANGE-BASED ARRAY CREATION")
        print("=" * 30)
        
        # arange - like Python range
        print("\n1️⃣  Using np.arange():")
        
        ranges = [
            ("Basic range", lambda: np.arange(10)),
            ("Start-stop", lambda: np.arange(5, 15)),
            ("With step", lambda: np.arange(0, 20, 3)),
            ("Float step", lambda: np.arange(0, 1, 0.1)),
            ("Reverse", lambda: np.arange(10, 0, -1))
        ]
        
        for name, func in ranges:
            start_time = time.time()
            result = func()
            creation_time = (time.time() - start_time) * 1000
            
            print(f"   {name}: {result}")
            print(f"   Shape: {result.shape}, Dtype: {result.dtype}")
            
            self.log_creation(f'arange_{name.lower().replace(" ", "_")}', 
                            result.shape, str(result.dtype), creation_time)
        
        # linspace - linear spacing
        print("\n2️⃣  Using np.linspace():")
        
        linspace_examples = [
            ("10 points 0-1", lambda: np.linspace(0, 1, 10)),
            ("5 points 0-100", lambda: np.linspace(0, 100, 5)),
            ("Exclude endpoint", lambda: np.linspace(0, 1, 5, endpoint=False)),
            ("Return step", lambda: np.linspace(0, 1, 5, retstep=True))
        ]
        
        for name, func in linspace_examples:
            start_time = time.time()
            result = func()
            creation_time = (time.time() - start_time) * 1000
            
            if isinstance(result, tuple):  # retstep=True case
                array, step = result
                print(f"   {name}: array={array}, step={step:.3f}")
                result = array
            else:
                print(f"   {name}: {result}")
            
            self.log_creation(f'linspace_{name.lower().replace(" ", "_")}', 
                            result.shape, str(result.dtype), creation_time)
        
        # logspace - logarithmic spacing
        print("\n3️⃣  Using np.logspace():")
        
        # Base 10 logarithmic spacing
        log_array = np.logspace(0, 2, 5)  # 10^0 to 10^2
        print(f"   Base 10 (10^0 to 10^2): {log_array}")
        
        # Base 2 logarithmic spacing
        log_base2 = np.logspace(0, 4, 5, base=2)  # 2^0 to 2^4
        print(f"   Base 2 (2^0 to 2^4): {log_base2}")
        
        # geomspace - geometric progression
        print("\n4️⃣  Using np.geomspace():")
        geom_array = np.geomspace(1, 1000, 5)
        print(f"   Geometric (1 to 1000): {geom_array}")
    
    def intrinsic_creation(self) -> None:
        """
        Create arrays using intrinsic NumPy functions
        """
        print("\n🏗️  INTRINSIC ARRAY CREATION")
        print("=" * 28)
        
        # Zeros arrays
        print("\n1️⃣  Zero Arrays:")
        
        zero_examples = [
            ("1D zeros", lambda: np.zeros(5)),
            ("2D zeros", lambda: np.zeros((3, 4))),
            ("3D zeros", lambda: np.zeros((2, 3, 4))),
            ("Float32 zeros", lambda: np.zeros(5, dtype=np.float32)),
            ("Integer zeros", lambda: np.zeros(5, dtype=np.int32))
        ]
        
        for name, func in zero_examples:
            start_time = time.time()
            result = func()
            creation_time = (time.time() - start_time) * 1000
            
            print(f"   {name}:")
            if result.ndim <= 2:
                print(f"     {result}")
            else:
                print(f"     Shape: {result.shape}")
            print(f"     Dtype: {result.dtype}")
            
            self.log_creation(f'zeros_{name.lower().replace(" ", "_")}', 
                            result.shape, str(result.dtype), creation_time)
        
        # Ones arrays
        print("\n2️⃣  Ones Arrays:")
        
        ones_1d = np.ones(4)
        ones_2d = np.ones((2, 5))
        ones_complex = np.ones(3, dtype=np.complex128)
        
        print(f"   1D ones: {ones_1d}")
        print(f"   2D ones:\n{ones_2d}")
        print(f"   Complex ones: {ones_complex}")
        
        # Full arrays (filled with specific value)
        print("\n3️⃣  Full Arrays:")
        
        full_examples = [
            ("Fill with 7", lambda: np.full(5, 7)),
            ("Fill with π", lambda: np.full((2, 3), np.pi)),
            ("Fill with string", lambda: np.full(3, 'hello', dtype='U10'))
        ]
        
        for name, func in full_examples:
            result = func()
            print(f"   {name}: {result}")
            print(f"   Shape: {result.shape}, Dtype: {result.dtype}")
        
        # Empty arrays (uninitialized)
        print("\n4️⃣  Empty Arrays:")
        print("   ⚠️  Warning: Empty arrays contain uninitialized data!")
        
        empty_array = np.empty(3)
        print(f"   Empty array: {empty_array}")
        print("   Note: Values are random (uninitialized memory)")
        
        # Array-like creation (copying shape and optionally data)
        print("\n5️⃣  Array-like Creation:")
        
        base_array = np.array([[1, 2], [3, 4]])
        
        zeros_like = np.zeros_like(base_array)
        ones_like = np.ones_like(base_array)
        full_like = np.full_like(base_array, 99)
        
        print(f"   Base array:\n{base_array}")
        print(f"   zeros_like:\n{zeros_like}")
        print(f"   ones_like:\n{ones_like}")
        print(f"   full_like (99):\n{full_like}")
    
    # =========================================================================
    # SPECIAL AND MATHEMATICAL ARRAYS
    # =========================================================================
    
    def special_arrays(self) -> None:
        """
        Create special mathematical and utility arrays
        """
        print("\n🔮 SPECIAL AND MATHEMATICAL ARRAYS")
        print("=" * 35)
        
        # Identity matrices
        print("\n1️⃣  Identity Matrices:")
        
        identity_examples = [
            ("3x3 Identity", lambda: np.eye(3)),
            ("4x4 Identity", lambda: np.eye(4)),
            ("Non-square (3x5)", lambda: np.eye(3, 5)),
            ("Offset diagonal", lambda: np.eye(4, k=1)),
            ("Below diagonal", lambda: np.eye(4, k=-1))
        ]
        
        for name, func in identity_examples:
            result = func()
            print(f"   {name}:")
            print(f"{result}")
            print(f"     Shape: {result.shape}")
        
        # Diagonal arrays
        print("\n2️⃣  Diagonal Arrays:")
        
        # From diagonal elements
        diag_elements = [1, 4, 9, 16]
        diag_matrix = np.diag(diag_elements)
        print(f"   From elements {diag_elements}:")
        print(f"{diag_matrix}")
        
        # Extract diagonal from matrix
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        extracted_diag = np.diag(matrix)
        print(f"   Extract from matrix:")
        print(f"   Matrix:\n{matrix}")
        print(f"   Diagonal: {extracted_diag}")
        
        # Meshgrid for coordinate arrays
        print("\n3️⃣  Meshgrid Arrays:")
        
        x = np.array([1, 2, 3])
        y = np.array([4, 5])
        
        X, Y = np.meshgrid(x, y)
        
        print(f"   X coordinates: {x}")
        print(f"   Y coordinates: {y}")
        print(f"   Meshgrid X:\n{X}")
        print(f"   Meshgrid Y:\n{Y}")
        
        # Coordinate arrays
        print(f"   Use case: Create coordinate grids for plotting")
        
        # Triangular arrays
        print("\n4️⃣  Triangular Arrays:")
        
        size = 4
        
        # Upper triangular
        upper_tri = np.tri(size, k=0)  # k=0 includes diagonal
        lower_tri = np.tri(size, k=-1)  # k=-1 excludes diagonal
        
        print(f"   Upper triangular (include diagonal):\n{upper_tri}")
        print(f"   Lower triangular (exclude diagonal):\n{lower_tri}")
        
        # Vandermonde matrix
        print("\n5️⃣  Vandermonde Matrix:")
        
        x_vals = np.array([1, 2, 3])
        vander = np.vander(x_vals, N=4)
        
        print(f"   Input: {x_vals}")
        print(f"   Vandermonde matrix:\n{vander}")
        print("   Each row: [x^(N-1), x^(N-2), ..., x^1, x^0]")
    
    # =========================================================================
    # RANDOM ARRAY CREATION
    # =========================================================================
    
    def random_arrays(self) -> None:
        """
        Create arrays using random number generation
        """
        print("\n🎲 RANDOM ARRAY CREATION")
        print("=" * 24)
        
        # Set seed for reproducible results
        np.random.seed(42)
        print("🔧 Random seed set to 42 for reproducible results")
        
        # Basic random arrays
        print("\n1️⃣  Basic Random Arrays:")
        
        random_examples = [
            ("Random floats [0,1)", lambda: np.random.random(5)),
            ("Random 2D", lambda: np.random.random((2, 3))),
            ("Random integers", lambda: np.random.randint(1, 10, 5)),
            ("Random choice", lambda: np.random.choice(['A', 'B', 'C'], 5))
        ]
        
        for name, func in random_examples:
            start_time = time.time()
            result = func()
            creation_time = (time.time() - start_time) * 1000
            
            print(f"   {name}: {result}")
            
            if hasattr(result, 'shape'):
                self.log_creation(f'random_{name.lower().replace(" ", "_")}', 
                                result.shape, str(result.dtype), creation_time)
        
        # Statistical distributions
        print("\n2️⃣  Statistical Distributions:")
        
        distributions = [
            ("Normal (μ=0, σ=1)", lambda: np.random.normal(0, 1, 5)),
            ("Uniform [2, 8)", lambda: np.random.uniform(2, 8, 5)),
            ("Exponential (λ=2)", lambda: np.random.exponential(2, 5)),
            ("Binomial (n=10, p=0.3)", lambda: np.random.binomial(10, 0.3, 5)),
            ("Poisson (λ=3)", lambda: np.random.poisson(3, 5))
        ]
        
        for name, func in distributions:
            result = func()
            print(f"   {name}: {result}")
            print(f"     Mean: {np.mean(result):.2f}, Std: {np.std(result):.2f}")
        
        # Random sampling and permutations
        print("\n3️⃣  Sampling and Permutations:")
        
        # Shuffle existing array
        arr_to_shuffle = np.arange(10)
        original = arr_to_shuffle.copy()
        np.random.shuffle(arr_to_shuffle)
        
        print(f"   Original: {original}")
        print(f"   Shuffled: {arr_to_shuffle}")
        
        # Random permutation
        perm = np.random.permutation(8)
        print(f"   Permutation of 0-7: {perm}")
        
        # Sample without replacement
        population = np.arange(100)
        sample = np.random.choice(population, 5, replace=False)
        print(f"   Sample of 5 from 0-99: {sample}")
    
    # =========================================================================
    # PERFORMANCE ANALYSIS
    # =========================================================================
    
    def analyze_performance(self) -> None:
        """
        Analyze performance of different array creation methods
        """
        print("\n⏱️  ARRAY CREATION PERFORMANCE ANALYSIS")
        print("=" * 40)
        
        sizes = [1000, 10000, 100000]
        methods = [
            ("np.zeros", lambda size: np.zeros(size)),
            ("np.ones", lambda size: np.ones(size)),
            ("np.empty", lambda size: np.empty(size)),
            ("np.arange", lambda size: np.arange(size)),
            ("np.random", lambda size: np.random.random(size))
        ]
        
        print("   📊 Performance Comparison (milliseconds):")
        print("   ┌─────────────┬─────────────┬─────────────┬─────────────┐")
        print("   │ Method      │ 1K elements │ 10K elements│ 100K elements│")
        print("   ├─────────────┼─────────────┼─────────────┼─────────────┤")
        
        for method_name, method_func in methods:
            times = []
            
            for size in sizes:
                # Warm up
                _ = method_func(size)
                
                # Measure
                start_time = time.time()
                _ = method_func(size)
                elapsed = (time.time() - start_time) * 1000
                times.append(elapsed)
            
            print(f"   │ {method_name:<11} │ {times[0]:>9.3f} ms │ {times[1]:>9.3f} ms │ {times[2]:>9.3f} ms │")
        
        print("   └─────────────┴─────────────┴─────────────┴─────────────┘")
        
        # Memory usage comparison
        print(f"\n   💾 Memory Usage Comparison:")
        
        size = 100000
        
        memory_tests = [
            ("float64", lambda: np.zeros(size, dtype=np.float64)),
            ("float32", lambda: np.zeros(size, dtype=np.float32)),
            ("int64", lambda: np.zeros(size, dtype=np.int64)),
            ("int32", lambda: np.zeros(size, dtype=np.int32)),
            ("int8", lambda: np.zeros(size, dtype=np.int8))
        ]
        
        for dtype_name, func in memory_tests:
            array = func()
            memory_mb = array.nbytes / (1024 * 1024)
            print(f"   {dtype_name}: {memory_mb:.2f} MB ({array.itemsize} bytes per element)")
    
    def get_creation_summary(self) -> None:
        """
        Display summary of array creation operations performed
        """
        print(f"\n📋 ARRAY CREATION SUMMARY")
        print("=" * 25)
        
        if not self.creation_log:
            print("   No operations logged yet.")
            return
        
        total_time = sum(entry['time_ms'] for entry in self.creation_log)
        total_memory = sum(entry['memory_mb'] for entry in self.creation_log)
        
        print(f"   Total operations: {len(self.creation_log)}")
        print(f"   Total time: {total_time:.2f} ms")
        print(f"   Total memory allocated: {total_memory:.2f} MB")
        print(f"   Average time per operation: {total_time / len(self.creation_log):.3f} ms")
        
        # Most common methods
        method_counts = {}
        for entry in self.creation_log:
            method = entry['method'].split('_')[0]
            method_counts[method] = method_counts.get(method, 0) + 1
        
        print(f"\n   📊 Method usage:")
        for method, count in sorted(method_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   • {method}: {count} times")

# =============================================================================
# INTERACTIVE LEARNING AND DEMONSTRATION
# =============================================================================

def interactive_array_creation_lab():
    """
    Interactive laboratory for experimenting with array creation
    """
    print("\n🧪 INTERACTIVE ARRAY CREATION LAB")
    print("=" * 33)
    
    creator = ArrayCreator()
    
    while True:
        try:
            print("\n🎯 Choose array creation method:")
            print("   1. From Python data")
            print("   2. Range-based arrays")
            print("   3. Intrinsic creation (zeros, ones, etc.)")
            print("   4. Special mathematical arrays")
            print("   5. Random arrays")
            print("   6. Performance analysis")
            print("   7. Creation summary")
            print("   8. Custom array creator")
            print("   9. Exit lab")
            
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if choice == "1":
                creator.from_python_data()
            elif choice == "2":
                creator.from_ranges()
            elif choice == "3":
                creator.intrinsic_creation()
            elif choice == "4":
                creator.special_arrays()
            elif choice == "5":
                creator.random_arrays()
            elif choice == "6":
                creator.analyze_performance()
            elif choice == "7":
                creator.get_creation_summary()
            elif choice == "8":
                custom_array_creator()
            elif choice == "9":
                print("\n👋 Thanks for exploring array creation!")
                break
            else:
                print("❌ Invalid choice. Please choose 1-9.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def custom_array_creator():
    """
    Interactive tool for creating custom arrays
    """
    print("\n🛠️  Custom Array Creator")
    print("=" * 20)
    
    try:
        # Get array specifications
        print("Specify your array:")
        
        method = input("Creation method (zeros/ones/random/arange/linspace): ").strip().lower()
        
        if method in ['zeros', 'ones', 'empty', 'random']:
            shape_input = input("Enter shape (e.g., '5' for 1D or '3,4' for 2D): ").strip()
            
            try:
                if ',' in shape_input:
                    shape = tuple(map(int, shape_input.split(',')))
                else:
                    shape = (int(shape_input),)
                
                dtype = input("Data type (float64/int32/etc., or press Enter for default): ").strip()
                if not dtype:
                    dtype = None
                
                # Create array based on method
                start_time = time.time()
                
                if method == 'zeros':
                    if dtype:
                        array = np.zeros(shape, dtype=dtype)
                    else:
                        array = np.zeros(shape)
                elif method == 'ones':
                    if dtype:
                        array = np.ones(shape, dtype=dtype)
                    else:
                        array = np.ones(shape)
                elif method == 'empty':
                    if dtype:
                        array = np.empty(shape, dtype=dtype)
                    else:
                        array = np.empty(shape)
                elif method == 'random':
                    array = np.random.random(shape)
                    if dtype and dtype != 'float64':
                        array = array.astype(dtype)
                
                creation_time = (time.time() - start_time) * 1000
                
                print(f"\n✅ Array created successfully!")
                print(f"   Shape: {array.shape}")
                print(f"   Dtype: {array.dtype}")
                print(f"   Size: {array.size} elements")
                print(f"   Memory: {array.nbytes / 1024:.2f} KB")
                print(f"   Creation time: {creation_time:.3f} ms")
                
                # Show array content (limited for large arrays)
                if array.size <= 50:
                    print(f"   Content: {array}")
                else:
                    print(f"   Sample: {array.flat[:10]}... (showing first 10 elements)")
                
            except ValueError:
                print("❌ Invalid shape format. Use numbers separated by commas.")
                
        elif method in ['arange', 'linspace']:
            if method == 'arange':
                start = float(input("Start value: "))
                stop = float(input("Stop value: "))
                step = input("Step (press Enter for default): ").strip()
                step = float(step) if step else 1
                
                array = np.arange(start, stop, step)
                
            elif method == 'linspace':
                start = float(input("Start value: "))
                stop = float(input("Stop value: "))
                num = int(input("Number of points: "))
                
                array = np.linspace(start, stop, num)
            
            print(f"\n✅ Array created: {array}")
            print(f"   Shape: {array.shape}")
            print(f"   Dtype: {array.dtype}")
        
        else:
            print("❌ Unsupported method. Try: zeros, ones, random, arange, linspace")
    
    except Exception as e:
        print(f"❌ Error creating array: {e}")

# =============================================================================
# DEMONSTRATION AND MAIN EXECUTION
# =============================================================================

def demonstrate_all_creation_methods():
    """
    Comprehensive demonstration of all array creation methods
    """
    print("\n" + "="*60)
    print("COMPREHENSIVE ARRAY CREATION DEMONSTRATION")
    print("="*60)
    
    creator = ArrayCreator()
    
    # Demonstrate all methods
    methods = [
        ("Python Data Conversion", creator.from_python_data),
        ("Range-based Creation", creator.from_ranges),
        ("Intrinsic Functions", creator.intrinsic_creation),
        ("Special Arrays", creator.special_arrays),
        ("Random Arrays", creator.random_arrays),
        ("Performance Analysis", creator.analyze_performance),
        ("Creation Summary", creator.get_creation_summary)
    ]
    
    for method_name, method_func in methods:
        print(f"\n{'='*50}")
        print(f"DEMONSTRATING: {method_name.upper()}")
        print('='*50)
        
        try:
            method_func()
            print("✅ Method demonstrated successfully")
        except Exception as e:
            print(f"❌ Error in {method_name}: {e}")

if __name__ == "__main__":
    """
    Main execution demonstrating NumPy array creation concepts
    """
    print(__doc__)
    
    # Educational content
    explain_array_creation_concepts()
    
    # Comprehensive demonstration
    demonstrate_all_creation_methods()
    
    # Interactive lab
    interactive_array_creation_lab()
    
    print("\n" + "=" * 50)
    print("🎓 ARRAY CREATION MASTERY SUMMARY")
    print("=" * 50)
    print("✅ All array creation methods mastered")
    print("✅ Performance characteristics understood")
    print("✅ Memory management principles learned")
    print("✅ Special array types and applications")
    print("✅ Random array generation techniques")
    print("✅ Interactive creation tools developed")
    
    print("\n💡 Key Concepts Mastered:")
    print("• Comprehensive array creation methodology")
    print("• Performance optimization for different use cases")
    print("• Memory-efficient array initialization")
    print("• Data type selection and conversion")
    print("• Mathematical and special array structures")
    print("• Random number generation and statistical distributions")
    
    print("\n🎯 Next Steps in NumPy:")
    print("• Array indexing and slicing mastery")
    print("• Mathematical operations and broadcasting")
    print("• Linear algebra operations")
    print("• Array reshaping and manipulation")
    print("• Integration with other scientific libraries")
    print("• Advanced performance optimization techniques")