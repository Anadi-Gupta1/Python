"""
NumPy Getting Started Guide - Complete Beginner to Advanced Journey
================================================================

Comprehensive getting started guide for NumPy covering installation, setup,
fundamental concepts, practical examples, and step-by-step progression from
beginner to advanced NumPy usage in scientific computing and data analysis.

Author: Python Learning Notes
Date: September 2025
Topic: NumPy Installation, Setup, Beginner Guide, Learning Path
"""

import numpy as np
import sys
import os
import time
import platform
from typing import List, Dict, Any, Optional, Tuple
import warnings

# =============================================================================
# GETTING STARTED WITH NUMPY
# =============================================================================

def check_system_requirements():
    """
    Check system requirements and Python environment for NumPy
    """
    print("🔧 SYSTEM REQUIREMENTS CHECK")
    print("=" * 28)
    
    print(f"\n💻 System Information:")
    print(f"   Operating System: {platform.system()} {platform.release()}")
    print(f"   Architecture: {platform.machine()}")
    print(f"   Python Version: {sys.version}")
    print(f"   Python Executable: {sys.executable}")
    
    # Check Python version compatibility
    python_version = sys.version_info
    print(f"\n🐍 Python Compatibility:")
    
    if python_version >= (3, 8):
        print(f"   ✅ Python {python_version.major}.{python_version.minor} - Fully supported")
    elif python_version >= (3, 6):
        print(f"   ⚠️  Python {python_version.major}.{python_version.minor} - Limited support")
        print(f"      Consider upgrading to Python 3.8+ for best experience")
    else:
        print(f"   ❌ Python {python_version.major}.{python_version.minor} - Not supported")
        print(f"      Please upgrade to Python 3.8 or higher")
        return False
    
    # Check available memory
    try:
        import psutil
        memory = psutil.virtual_memory()
        print(f"\n💾 Memory Information:")
        print(f"   Total RAM: {memory.total / (1024**3):.1f} GB")
        print(f"   Available RAM: {memory.available / (1024**3):.1f} GB")
        
        if memory.available < 1 * (1024**3):  # Less than 1GB
            print(f"   ⚠️  Low available memory - consider closing other applications")
        else:
            print(f"   ✅ Sufficient memory for NumPy operations")
    except ImportError:
        print(f"\n💾 Memory Information:")
        print(f"   Install 'psutil' for detailed memory information")
    
    return True

def installation_guide():
    """
    Comprehensive NumPy installation guide for different environments
    """
    print("\n📦 NUMPY INSTALLATION GUIDE")
    print("=" * 28)
    
    print("\n🛠️  Installation Methods:")
    
    methods = [
        ("pip (recommended)", "pip install numpy", "Standard Python package manager"),
        ("conda", "conda install numpy", "Anaconda/Miniconda package manager"),
        ("pip with extras", "pip install numpy[dev]", "Include development dependencies"),
        ("From source", "pip install --no-binary numpy", "Compile from source code")
    ]
    
    print("   ┌─────────────────┬─────────────────────────────┬─────────────────────────┐")
    print("   │ Method          │ Command                     │ Description             │")
    print("   ├─────────────────┼─────────────────────────────┼─────────────────────────┤")
    for method, command, description in methods:
        print(f"   │ {method:<15} │ {command:<27} │ {description:<23} │")
    print("   └─────────────────┴─────────────────────────────┴─────────────────────────┘")
    
    print(f"\n🔍 Verify Installation:")
    print(f"   Try importing NumPy and checking version:")
    print(f"   >>> import numpy as np")
    print(f"   >>> print(np.__version__)")
    print(f"   >>> print(np.__file__)")
    
    # Check current installation
    try:
        print(f"\n✅ Current NumPy Installation:")
        print(f"   Version: {np.__version__}")
        print(f"   Location: {np.__file__}")
        print(f"   Build info available: {hasattr(np, 'show_config')}")
        
        # Show build configuration if available
        if hasattr(np, 'show_config'):
            print(f"\n🔧 Build Configuration:")
            try:
                np.show_config()
            except:
                print(f"   Build configuration not available")
                
    except Exception as e:
        print(f"   ❌ NumPy not properly installed: {e}")
    
    print(f"\n🚨 Troubleshooting Common Issues:")
    issues = [
        "ImportError: No module named numpy",
        "   Solution: Install numpy using pip install numpy",
        "",
        "Permission denied during installation",
        "   Solution: Use --user flag: pip install --user numpy",
        "",
        "Conflicting package versions",
        "   Solution: Create virtual environment or use conda",
        "",
        "Slow performance on Windows",
        "   Solution: Install Intel MKL optimized version via conda"
    ]
    
    for issue in issues:
        if issue:
            print(f"   {issue}")

def verify_numpy_functionality():
    """
    Verify that NumPy is working correctly with basic functionality tests
    """
    print("\n🧪 NUMPY FUNCTIONALITY VERIFICATION")
    print("=" * 35)
    
    tests = []
    
    # Test 1: Basic array creation
    try:
        arr = np.array([1, 2, 3, 4, 5])
        tests.append(("Basic array creation", True, f"Created array: {arr}"))
    except Exception as e:
        tests.append(("Basic array creation", False, f"Error: {e}"))
    
    # Test 2: Mathematical operations
    try:
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        result = a + b
        tests.append(("Mathematical operations", True, f"Addition result: {result}"))
    except Exception as e:
        tests.append(("Mathematical operations", False, f"Error: {e}"))
    
    # Test 3: Array properties
    try:
        arr_2d = np.random.random((3, 4))
        shape_info = f"Shape: {arr_2d.shape}, Size: {arr_2d.size}, Dtype: {arr_2d.dtype}"
        tests.append(("Array properties", True, shape_info))
    except Exception as e:
        tests.append(("Array properties", False, f"Error: {e}"))
    
    # Test 4: Linear algebra (if available)
    try:
        matrix = np.array([[1, 2], [3, 4]])
        det = np.linalg.det(matrix)
        tests.append(("Linear algebra", True, f"Determinant: {det:.2f}"))
    except Exception as e:
        tests.append(("Linear algebra", False, f"Error: {e}"))
    
    # Test 5: Random number generation
    try:
        np.random.seed(42)
        random_arr = np.random.random(5)
        tests.append(("Random generation", True, f"Random array: {random_arr[:3]}..."))
    except Exception as e:
        tests.append(("Random generation", False, f"Error: {e}"))
    
    # Test 6: Performance test
    try:
        start_time = time.time()
        large_arr = np.random.random(10000)
        result = np.sum(large_arr)
        elapsed = (time.time() - start_time) * 1000
        tests.append(("Performance test", True, f"Sum of 10k elements: {elapsed:.2f} ms"))
    except Exception as e:
        tests.append(("Performance test", False, f"Error: {e}"))
    
    # Display results
    print("   🧪 Test Results:")
    print("   ┌─────────────────────┬────────┬─────────────────────────────────┐")
    print("   │ Test                │ Status │ Details                         │")
    print("   ├─────────────────────┼────────┼─────────────────────────────────┤")
    
    passed = 0
    for test_name, success, details in tests:
        status = "✅ PASS" if success else "❌ FAIL"
        details_short = details[:31] + "..." if len(details) > 31 else details
        print(f"   │ {test_name:<19} │ {status} │ {details_short:<31} │")
        if success:
            passed += 1
    
    print("   └─────────────────────┴────────┴─────────────────────────────────┘")
    
    print(f"\n   📊 Summary: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("   🎉 All tests passed! NumPy is working correctly.")
    elif passed >= len(tests) * 0.8:
        print("   👍 Most tests passed. NumPy is mostly functional.")
    else:
        print("   ⚠️  Several tests failed. Check your NumPy installation.")
    
    return passed == len(tests)

# =============================================================================
# LEARNING PATH AND PROGRESSION
# =============================================================================

class NumpyLearningPath:
    """
    Structured learning path for mastering NumPy
    """
    
    def __init__(self):
        """Initialize the learning path with structured modules"""
        self.modules = {
            "beginner": [
                "What is NumPy and why use it?",
                "Installing and importing NumPy",
                "Creating basic arrays",
                "Array attributes and properties",
                "Basic indexing and slicing",
                "Simple mathematical operations",
                "Array creation functions",
                "Data types in NumPy"
            ],
            "intermediate": [
                "Advanced indexing (boolean, fancy)",
                "Array broadcasting",
                "Shape manipulation and reshaping",
                "Mathematical and statistical functions",
                "Linear algebra operations",
                "File I/O operations",
                "Working with missing data",
                "Performance optimization basics"
            ],
            "advanced": [
                "Custom ufuncs and vectorization",
                "Memory layout and performance tuning",
                "Advanced broadcasting techniques",
                "Structured arrays and record arrays",
                "NumPy C API basics",
                "Integration with other libraries",
                "Parallel computing considerations",
                "Contributing to NumPy ecosystem"
            ]
        }
        
        self.current_level = "beginner"
        self.completed_topics = set()
    
    def display_learning_path(self):
        """Display the complete learning path"""
        print("\n🎓 NUMPY LEARNING PATH")
        print("=" * 22)
        
        levels = ["beginner", "intermediate", "advanced"]
        level_icons = {"beginner": "🌱", "intermediate": "🌿", "advanced": "🌳"}
        
        for level in levels:
            print(f"\n{level_icons[level]} {level.upper()} LEVEL:")
            print(f"   {'='*30}")
            
            for i, topic in enumerate(self.modules[level], 1):
                status = "✅" if topic in self.completed_topics else "⬜"
                print(f"   {status} {i:2d}. {topic}")
        
        # Show progression
        total_topics = sum(len(topics) for topics in self.modules.values())
        completed_count = len(self.completed_topics)
        progress = (completed_count / total_topics) * 100
        
        print(f"\n📊 Overall Progress: {completed_count}/{total_topics} ({progress:.1f}%)")
        
        # Show next recommended topic
        next_topic = self.get_next_topic()
        if next_topic:
            print(f"🎯 Next Recommended: {next_topic}")
    
    def get_next_topic(self):
        """Get the next recommended topic to study"""
        for level in ["beginner", "intermediate", "advanced"]:
            for topic in self.modules[level]:
                if topic not in self.completed_topics:
                    return topic
        return None
    
    def mark_completed(self, topic: str):
        """Mark a topic as completed"""
        self.completed_topics.add(topic)
        
        # Update current level based on progress
        beginner_completed = all(topic in self.completed_topics for topic in self.modules["beginner"])
        intermediate_completed = all(topic in self.completed_topics for topic in self.modules["intermediate"])
        
        if intermediate_completed:
            self.current_level = "advanced"
        elif beginner_completed:
            self.current_level = "intermediate"
        else:
            self.current_level = "beginner"
    
    def get_resources_for_topic(self, topic: str) -> Dict[str, List[str]]:
        """Get learning resources for a specific topic"""
        resources = {
            "What is NumPy and why use it?": {
                "practice": ["Compare Python lists vs NumPy arrays", "Performance benchmarking"],
                "examples": ["Scientific computing use cases", "Real-world applications"]
            },
            "Creating basic arrays": {
                "practice": ["Array creation methods", "Different data types"],
                "examples": ["1D, 2D, 3D arrays", "Array from lists and tuples"]
            },
            "Basic indexing and slicing": {
                "practice": ["Single element access", "Slice notation"],
                "examples": ["Row and column selection", "Subarray extraction"]
            },
            "Array broadcasting": {
                "practice": ["Broadcasting rules", "Shape compatibility"],
                "examples": ["Scalar operations", "Array arithmetic"]
            }
        }
        
        return resources.get(topic, {
            "practice": ["Hands-on exercises", "Code implementation"],
            "examples": ["Practical applications", "Real-world scenarios"]
        })
    
    def interactive_topic_selection(self):
        """Interactive topic selection and learning"""
        while True:
            try:
                print(f"\n🎯 INTERACTIVE LEARNING")
                print("=" * 20)
                
                print(f"Current Level: {self.current_level.title()}")
                
                # Show available topics for current level
                available_topics = [
                    topic for topic in self.modules[self.current_level]
                    if topic not in self.completed_topics
                ]
                
                if not available_topics:
                    print("🎉 All topics in current level completed!")
                    
                    # Check if can advance to next level
                    levels = ["beginner", "intermediate", "advanced"]
                    current_index = levels.index(self.current_level)
                    
                    if current_index < len(levels) - 1:
                        next_level = levels[current_index + 1]
                        print(f"Ready to advance to {next_level} level!")
                        available_topics = self.modules[next_level][:3]  # Show first 3 topics
                    else:
                        print("🏆 Congratulations! You've completed the entire NumPy learning path!")
                        break
                
                print(f"\n📚 Available Topics:")
                for i, topic in enumerate(available_topics[:5], 1):  # Show max 5 topics
                    print(f"   {i}. {topic}")
                
                print(f"   6. View learning path")
                print(f"   7. Exit")
                
                choice = input(f"\nSelect topic to study (1-7): ").strip()
                
                if choice in ['1', '2', '3', '4', '5']:
                    topic_index = int(choice) - 1
                    if topic_index < len(available_topics):
                        selected_topic = available_topics[topic_index]
                        self.study_topic(selected_topic)
                elif choice == '6':
                    self.display_learning_path()
                elif choice == '7':
                    break
                else:
                    print("❌ Invalid choice. Please select 1-7.")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
            except KeyboardInterrupt:
                print("\n👋 Learning session ended!")
                break
    
    def study_topic(self, topic: str):
        """Study a specific topic with guided learning"""
        print(f"\n📖 STUDYING: {topic}")
        print("=" * (12 + len(topic)))
        
        # Get resources for the topic
        resources = self.get_resources_for_topic(topic)
        
        # Provide topic-specific guidance
        self.provide_topic_guidance(topic)
        
        # Mark as studied (simplified - in real app would track actual completion)
        confirm = input(f"\nHave you completed studying '{topic}'? (y/n): ").strip().lower()
        if confirm == 'y':
            self.mark_completed(topic)
            print(f"✅ Topic marked as completed!")
            
            # Show progress
            level_topics = self.modules[self.current_level]
            level_completed = sum(1 for t in level_topics if t in self.completed_topics)
            print(f"📊 Level Progress: {level_completed}/{len(level_topics)} topics completed")
    
    def provide_topic_guidance(self, topic: str):
        """Provide specific guidance for studying a topic"""
        guidance_map = {
            "What is NumPy and why use it?": self.guide_numpy_introduction,
            "Creating basic arrays": self.guide_array_creation,
            "Basic indexing and slicing": self.guide_basic_indexing,
            "Array attributes and properties": self.guide_array_properties,
            "Simple mathematical operations": self.guide_mathematical_operations
        }
        
        if topic in guidance_map:
            guidance_map[topic]()
        else:
            print(f"💡 Study Focus Areas:")
            print(f"   • Understand the core concepts")
            print(f"   • Practice with code examples")
            print(f"   • Apply to real-world scenarios")
            print(f"   • Test your understanding")
    
    def guide_numpy_introduction(self):
        """Guide for NumPy introduction topic"""
        print(f"📚 NumPy Introduction Study Guide:")
        print(f"   • Understand what NumPy is and its role in Python ecosystem")
        print(f"   • Learn about performance benefits over pure Python")
        print(f"   • Explore scientific computing applications")
        print(f"   • Compare NumPy arrays with Python lists")
        
        # Simple demonstration
        print(f"\n🧪 Quick Demo - Performance Comparison:")
        
        # Python list operation
        python_list = list(range(1000))
        start_time = time.time()
        python_result = [x * 2 for x in python_list]
        python_time = (time.time() - start_time) * 1000
        
        # NumPy array operation
        numpy_array = np.arange(1000)
        start_time = time.time()
        numpy_result = numpy_array * 2
        numpy_time = (time.time() - start_time) * 1000
        
        print(f"   Python list (1000 elements): {python_time:.3f} ms")
        print(f"   NumPy array (1000 elements): {numpy_time:.3f} ms")
        
        if numpy_time > 0:
            speedup = python_time / numpy_time
            print(f"   NumPy is {speedup:.1f}x faster!")
    
    def guide_array_creation(self):
        """Guide for array creation topic"""
        print(f"🎨 Array Creation Study Guide:")
        print(f"   • Master different array creation methods")
        print(f"   • Understand data types and their impact")
        print(f"   • Practice with various array shapes")
        print(f"   • Learn memory-efficient creation techniques")
        
        print(f"\n🧪 Practice Examples:")
        
        # Basic creation methods
        examples = [
            ("From list", lambda: np.array([1, 2, 3, 4, 5])),
            ("Zeros array", lambda: np.zeros((2, 3))),
            ("Range array", lambda: np.arange(0, 10, 2)),
            ("Random array", lambda: np.random.random((2, 2)))
        ]
        
        for name, create_func in examples:
            array = create_func()
            print(f"   {name}: {array}")
    
    def guide_basic_indexing(self):
        """Guide for basic indexing topic"""
        print(f"🎯 Basic Indexing Study Guide:")
        print(f"   • Master single element access")
        print(f"   • Understand negative indexing")
        print(f"   • Practice with multi-dimensional arrays")
        print(f"   • Learn slice notation and syntax")
        
        print(f"\n🧪 Indexing Examples:")
        
        # Create sample array
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(f"   Sample array:\n{arr}")
        print(f"   First element [0, 0]: {arr[0, 0]}")
        print(f"   Last element [-1, -1]: {arr[-1, -1]}")
        print(f"   First row [0, :]: {arr[0, :]}")
        print(f"   First column [:, 0]: {arr[:, 0]}")
    
    def guide_array_properties(self):
        """Guide for array properties topic"""
        print(f"📏 Array Properties Study Guide:")
        print(f"   • Understand shape, size, and ndim")
        print(f"   • Learn about data types (dtype)")
        print(f"   • Explore memory layout concepts")
        print(f"   • Practice with different array dimensions")
        
        print(f"\n🧪 Properties Example:")
        
        sample_array = np.random.random((3, 4, 2))
        print(f"   Array shape: {sample_array.shape}")
        print(f"   Array size: {sample_array.size}")
        print(f"   Array dimensions: {sample_array.ndim}")
        print(f"   Array dtype: {sample_array.dtype}")
        print(f"   Memory usage: {sample_array.nbytes} bytes")
    
    def guide_mathematical_operations(self):
        """Guide for mathematical operations topic"""
        print(f"🧮 Mathematical Operations Study Guide:")
        print(f"   • Master element-wise operations")
        print(f"   • Understand broadcasting rules")
        print(f"   • Practice with statistical functions")
        print(f"   • Learn about universal functions (ufuncs)")
        
        print(f"\n🧪 Operations Examples:")
        
        a = np.array([1, 2, 3, 4])
        b = np.array([5, 6, 7, 8])
        
        print(f"   Array a: {a}")
        print(f"   Array b: {b}")
        print(f"   Addition: {a + b}")
        print(f"   Multiplication: {a * b}")
        print(f"   Square root of a: {np.sqrt(a)}")
        print(f"   Sum of a: {np.sum(a)}")
        print(f"   Mean of a: {np.mean(a)}")

# =============================================================================
# PRACTICAL GETTING STARTED EXAMPLES
# =============================================================================

def beginner_friendly_examples():
    """
    Beginner-friendly examples to get started with NumPy
    """
    print("\n🚀 BEGINNER-FRIENDLY EXAMPLES")
    print("=" * 29)
    
    # Example 1: Your first NumPy array
    print("\n1️⃣  Your First NumPy Array:")
    print("   Creating arrays is the foundation of NumPy!")
    
    # From a list
    my_list = [1, 2, 3, 4, 5]
    my_array = np.array(my_list)
    
    print(f"   Python list: {my_list}")
    print(f"   NumPy array: {my_array}")
    print(f"   Array type: {type(my_array)}")
    
    # Example 2: Array math is easy!
    print("\n2️⃣  Array Math Made Easy:")
    print("   Mathematical operations work on entire arrays!")
    
    numbers = np.array([1, 2, 3, 4, 5])
    doubled = numbers * 2
    squared = numbers ** 2
    
    print(f"   Original: {numbers}")
    print(f"   Doubled:  {doubled}")
    print(f"   Squared:  {squared}")
    
    # Example 3: Useful array creation
    print("\n3️⃣  Useful Array Creation:")
    print("   NumPy has built-in functions for common arrays!")
    
    zeros = np.zeros(5)
    ones = np.ones(5)
    range_array = np.arange(0, 10, 2)
    
    print(f"   Five zeros: {zeros}")
    print(f"   Five ones:  {ones}")
    print(f"   Even nums:  {range_array}")
    
    # Example 4: 2D arrays (matrices)
    print("\n4️⃣  Working with 2D Arrays:")
    print("   2D arrays are like spreadsheets or matrices!")
    
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(f"   2D Array:\n{matrix}")
    print(f"   Shape: {matrix.shape} (rows, columns)")
    print(f"   First row: {matrix[0]}")
    print(f"   First column: {matrix[:, 0]}")
    
    # Example 5: Array statistics
    print("\n5️⃣  Quick Statistics:")
    print("   Get insights from your data instantly!")
    
    data = np.array([85, 90, 78, 92, 88, 76, 95, 89])
    
    print(f"   Test scores: {data}")
    print(f"   Average: {np.mean(data):.1f}")
    print(f"   Highest: {np.max(data)}")
    print(f"   Lowest:  {np.min(data)}")
    print(f"   Std dev: {np.std(data):.1f}")

def common_beginner_mistakes():
    """
    Highlight common beginner mistakes and how to avoid them
    """
    print("\n⚠️  COMMON BEGINNER MISTAKES")
    print("=" * 27)
    
    mistakes = [
        {
            "mistake": "Using Python lists instead of NumPy arrays for math",
            "wrong": "[1, 2, 3] * 2  # This repeats the list!",
            "correct": "np.array([1, 2, 3]) * 2  # This multiplies elements",
            "explanation": "Python lists and NumPy arrays behave differently with operators"
        },
        {
            "mistake": "Forgetting to import NumPy",
            "wrong": "array([1, 2, 3])  # NameError!",
            "correct": "import numpy as np; np.array([1, 2, 3])",
            "explanation": "Always import NumPy before using it"
        },
        {
            "mistake": "Mixing up array indexing",
            "wrong": "arr[1, 2, 3]  # Wrong for 2D array!",
            "correct": "arr[1, 2]  # Correct for 2D array",
            "explanation": "Use comma-separated indices for multi-dimensional arrays"
        },
        {
            "mistake": "Not understanding array shape",
            "wrong": "Assuming all arrays are 1D",
            "correct": "Check array.shape before operations",
            "explanation": "Always be aware of your array's dimensions"
        }
    ]
    
    for i, mistake_info in enumerate(mistakes, 1):
        print(f"\n{i}️⃣  {mistake_info['mistake']}:")
        print(f"   ❌ Wrong: {mistake_info['wrong']}")
        print(f"   ✅ Right: {mistake_info['correct']}")
        print(f"   💡 Why: {mistake_info['explanation']}")

def next_steps_guide():
    """
    Guide users on what to learn next after getting started
    """
    print("\n🎯 WHAT TO LEARN NEXT")
    print("=" * 21)
    
    next_steps = [
        {
            "topic": "Array Indexing & Slicing",
            "description": "Master advanced ways to select and modify array elements",
            "priority": "High",
            "estimated_time": "2-3 hours"
        },
        {
            "topic": "Mathematical Functions",
            "description": "Explore NumPy's vast library of mathematical operations",
            "priority": "High",
            "estimated_time": "3-4 hours"
        },
        {
            "topic": "Array Broadcasting",
            "description": "Understand how NumPy handles operations on different shaped arrays",
            "priority": "Medium",
            "estimated_time": "2-3 hours"
        },
        {
            "topic": "Linear Algebra",
            "description": "Learn matrix operations for scientific computing",
            "priority": "Medium",
            "estimated_time": "4-5 hours"
        },
        {
            "topic": "File I/O",
            "description": "Save and load NumPy arrays from files",
            "priority": "Low",
            "estimated_time": "1-2 hours"
        }
    ]
    
    print("   📚 Recommended Learning Sequence:")
    print("   ┌─────────────────────────┬─────────────────────────────────┬──────────┬──────────────┐")
    print("   │ Topic                   │ Description                     │ Priority │ Time Est.    │")
    print("   ├─────────────────────────┼─────────────────────────────────┼──────────┼──────────────┤")
    
    for step in next_steps:
        topic = step["topic"][:23]
        desc = step["description"][:31]
        priority = step["priority"]
        time = step["estimated_time"]
        
        print(f"   │ {topic:<23} │ {desc:<31} │ {priority:<8} │ {time:<12} │")
    
    print("   └─────────────────────────┴─────────────────────────────────┴──────────┴──────────────┘")
    
    print(f"\n🔗 Additional Resources:")
    resources = [
        ("Official NumPy Documentation", "https://numpy.org/doc/"),
        ("NumPy Tutorials", "https://numpy.org/learn/"),
        ("SciPy Lecture Notes", "https://scipy-lectures.org/"),
        ("Python Data Science Handbook", "Online book with NumPy chapters")
    ]
    
    for resource, link in resources:
        print(f"   • {resource}: {link}")

# =============================================================================
# INTERACTIVE GETTING STARTED SESSION
# =============================================================================

def interactive_getting_started():
    """
    Interactive getting started session for new NumPy users
    """
    print("\n🎮 INTERACTIVE GETTING STARTED SESSION")
    print("=" * 37)
    
    learning_path = NumpyLearningPath()
    
    while True:
        try:
            print(f"\n🎯 Choose your learning activity:")
            print("   1. Check system requirements")
            print("   2. Verify NumPy installation") 
            print("   3. View learning path")
            print("   4. Start guided learning")
            print("   5. Try beginner examples")
            print("   6. Learn about common mistakes")
            print("   7. Get next steps guidance")
            print("   8. Exit")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                check_system_requirements()
                
            elif choice == "2":
                verify_numpy_functionality()
                
            elif choice == "3":
                learning_path.display_learning_path()
                
            elif choice == "4":
                learning_path.interactive_topic_selection()
                
            elif choice == "5":
                beginner_friendly_examples()
                
            elif choice == "6":
                common_beginner_mistakes()
                
            elif choice == "7":
                next_steps_guide()
                
            elif choice == "8":
                print("\n👋 Happy learning with NumPy!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-8.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# =============================================================================
# MAIN EXECUTION AND DEMONSTRATION
# =============================================================================

def main():
    """
    Main function for the NumPy getting started guide
    """
    print(__doc__)
    
    # Check system and installation
    print("🔍 Initial Setup Check")
    print("=" * 20)
    
    if not check_system_requirements():
        print("❌ System requirements not met. Please upgrade your Python installation.")
        return
    
    # Installation guide
    installation_guide()
    
    # Verify functionality
    if not verify_numpy_functionality():
        print("⚠️  Some NumPy functionality may not work correctly.")
        
    # Learning path overview
    learning_path = NumpyLearningPath()
    learning_path.display_learning_path()
    
    # Beginner examples
    beginner_friendly_examples()
    
    # Common mistakes
    common_beginner_mistakes()
    
    # Next steps
    next_steps_guide()
    
    # Interactive session
    interactive_getting_started()

if __name__ == "__main__":
    """
    Execute the complete NumPy getting started guide
    """
    main()
    
    print("\n" + "=" * 50)
    print("🎓 NUMPY GETTING STARTED SUMMARY")
    print("=" * 50)
    print("✅ System requirements and installation verified")
    print("✅ Basic NumPy functionality demonstrated")
    print("✅ Structured learning path provided")
    print("✅ Beginner-friendly examples completed")
    print("✅ Common mistakes and solutions covered")
    print("✅ Next steps and resources identified")
    
    print("\n💡 Key Takeaways:")
    print("• NumPy is the foundation of scientific Python")
    print("• Arrays are more efficient than Python lists")
    print("• Mathematical operations work element-wise")
    print("• Understanding array shape is crucial")
    print("• Practice with real examples builds expertise")
    print("• Community resources support continued learning")
    
    print("\n🚀 Ready for Your NumPy Journey!")
    print("• Start with basic array operations")
    print("• Practice regularly with small examples")
    print("• Gradually tackle more complex problems")
    print("• Join the NumPy community for support")
    print("• Build projects that interest you")
    print("• Keep exploring the vast NumPy ecosystem!")
