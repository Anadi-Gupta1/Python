"""
NumPy Getting Started Guide
===========================

This module provides a comprehensive getting started guide for NumPy,
covering installation, importing, basic usage, and essential concepts.

Author: Anadi Gupta
Date: September 2025
Purpose: Complete beginner's guide to getting started with NumPy
"""

import numpy as np
import sys
import subprocess
import platform

def display_system_info():
    """Display system information and Python environment"""
    print("🖥️ System Information")
    print("=" * 30)
    
    print(f"🐍 Python Version: {sys.version}")
    print(f"💻 Operating System: {platform.system()} {platform.release()}")
    print(f"🏗️ Architecture: {platform.architecture()[0]}")
    print(f"🔧 Python Executable: {sys.executable}")

def check_numpy_installation():
    """Check NumPy installation and display version information"""
    print("\n📦 NumPy Installation Check")
    print("=" * 35)
    
    try:
        import numpy as np
        print(f"✅ NumPy is installed successfully!")
        print(f"📊 NumPy Version: {np.__version__}")
        print(f"📁 NumPy Location: {np.__file__}")
        
        # Check NumPy configuration
        print(f"\n🔧 NumPy Configuration:")
        config_info = np.show_config()
        
        return True
        
    except ImportError:
        print("❌ NumPy is not installed!")
        print("\n📥 Installation Instructions:")
        print("   Method 1: pip install numpy")
        print("   Method 2: conda install numpy")
        print("   Method 3: Use Anaconda distribution")
        return False

def demonstrate_installation_methods():
    """Demonstrate different NumPy installation methods"""
    print("\n📥 NumPy Installation Methods")
    print("=" * 40)
    
    print("🔹 Method 1: Using pip (most common)")
    print("   Command: pip install numpy")
    print("   Upgrade: pip install --upgrade numpy")
    print("   Specific version: pip install numpy==1.21.0")
    
    print("\n🔹 Method 2: Using conda")
    print("   Command: conda install numpy")
    print("   From conda-forge: conda install -c conda-forge numpy")
    
    print("\n🔹 Method 3: Pre-installed distributions")
    print("   • Anaconda: Includes NumPy by default")
    print("   • Miniconda: Minimal conda installation")
    print("   • WinPython: Windows-specific distribution")
    
    print("\n🔹 Method 4: From source (advanced)")
    print("   git clone https://github.com/numpy/numpy.git")
    print("   cd numpy && pip install -e .")

def demonstrate_importing():
    """Demonstrate different ways to import NumPy"""
    print("\n📥 Importing NumPy")
    print("=" * 25)
    
    print("🔹 Standard import:")
    print("   import numpy")
    print("   arr = numpy.array([1, 2, 3])")
    
    print("\n🔹 Import with alias (recommended):")
    print("   import numpy as np")
    print("   arr = np.array([1, 2, 3])")
    
    print("\n🔹 Import specific functions:")
    print("   from numpy import array, zeros, ones")
    print("   arr = array([1, 2, 3])")
    
    print("\n🔹 Import all (not recommended):")
    print("   from numpy import *")
    print("   arr = array([1, 2, 3])  # Can cause namespace conflicts")
    
    # Practical demonstration
    print(f"\n✨ Practical Example:")
    basic_array = np.array([1, 2, 3, 4, 5])
    print(f"   np.array([1, 2, 3, 4, 5]) = {basic_array}")

def demonstrate_first_steps():
    """Demonstrate first steps with NumPy arrays"""
    print("\n👶 First Steps with NumPy")
    print("=" * 35)
    
    print("🔹 Creating your first array:")
    first_array = np.array([1, 2, 3, 4, 5])
    print(f"   my_array = np.array([1, 2, 3, 4, 5])")
    print(f"   Result: {first_array}")
    print(f"   Type: {type(first_array)}")
    
    print(f"\n🔹 Array properties:")
    print(f"   Shape: {first_array.shape}")
    print(f"   Size: {first_array.size}")
    print(f"   Data type: {first_array.dtype}")
    
    print(f"\n🔹 Basic operations:")
    print(f"   Array + 10: {first_array + 10}")
    print(f"   Array * 2: {first_array * 2}")
    print(f"   Sum: {np.sum(first_array)}")
    print(f"   Mean: {np.mean(first_array)}")

def demonstrate_common_functions():
    """Demonstrate common NumPy functions for beginners"""
    print("\n🛠️ Common NumPy Functions")
    print("=" * 35)
    
    print("🔹 Array creation functions:")
    zeros_arr = np.zeros(5)
    ones_arr = np.ones(5)
    range_arr = np.arange(5)
    
    print(f"   np.zeros(5): {zeros_arr}")
    print(f"   np.ones(5): {ones_arr}")
    print(f"   np.arange(5): {range_arr}")
    
    print(f"\n🔹 Mathematical functions:")
    sample_arr = np.array([1, 4, 9, 16, 25])
    print(f"   Original: {sample_arr}")
    print(f"   Square root: {np.sqrt(sample_arr)}")
    print(f"   Maximum: {np.max(sample_arr)}")
    print(f"   Minimum: {np.min(sample_arr)}")
    
    print(f"\n🔹 2D array example:")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"   2D array:\n{matrix}")
    print(f"   Shape: {matrix.shape}")

def demonstrate_help_resources():
    """Show available help resources for NumPy"""
    print("\n📚 Getting Help and Resources")
    print("=" * 40)
    
    print("🔹 Built-in help:")
    print("   help(np.array)       # Function help")
    print("   np.info(np.array)    # Detailed info")
    print("   np.array?            # IPython/Jupyter help")
    
    print("\n🔹 Documentation:")
    print("   Official docs: https://numpy.org/doc/")
    print("   User guide: https://numpy.org/doc/stable/user/")
    print("   API reference: https://numpy.org/doc/stable/reference/")
    
    print("\n🔹 Learning resources:")
    print("   NumPy quickstart: https://numpy.org/doc/stable/user/quickstart.html")
    print("   NumPy tutorials: https://numpy.org/numpy-tutorials/")
    print("   SciPy lectures: https://scipy-lectures.org/")
    
    print("\n🔹 Community:")
    print("   Stack Overflow: [numpy] tag")
    print("   GitHub issues: https://github.com/numpy/numpy/issues")
    print("   Mailing list: numpy-discussion@python.org")

def demonstrate_best_practices():
    """Demonstrate NumPy best practices for beginners"""
    print("\n⭐ NumPy Best Practices")
    print("=" * 30)
    
    print("🔹 Import conventions:")
    print("   ✅ import numpy as np (standard)")
    print("   ❌ from numpy import * (avoid)")
    
    print("\n🔹 Array creation:")
    print("   ✅ Use np.array() for small arrays")
    print("   ✅ Use np.zeros(), np.ones() for large arrays")
    print("   ✅ Specify dtype when needed: np.array([1, 2], dtype=float)")
    
    print("\n🔹 Performance tips:")
    print("   ✅ Use vectorized operations instead of loops")
    print("   ✅ Avoid creating unnecessary copies")
    print("   ✅ Use views when possible")
    
    print("\n🔹 Memory efficiency:")
    print("   ✅ Use appropriate data types (int32 vs int64)")
    print("   ✅ Use np.float32 for GPU compatibility")
    print("   ✅ Use np.copy() when you need explicit copies")

def run_installation_check():
    """Interactive installation check and troubleshooting"""
    print("\n🔧 Installation Troubleshooting")
    print("=" * 40)
    
    try:
        # Check if NumPy can be imported
        import numpy as test_np
        print("✅ NumPy import successful")
        
        # Test basic functionality
        test_array = test_np.array([1, 2, 3])
        test_result = test_np.sum(test_array)
        print(f"✅ Basic operations working: sum([1,2,3]) = {test_result}")
        
        # Check for common issues
        print(f"✅ NumPy version: {test_np.__version__}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\n🚨 Troubleshooting steps:")
        print("1. Check Python installation: python --version")
        print("2. Check pip installation: pip --version")
        print("3. Install NumPy: pip install numpy")
        print("4. Try restarting your IDE/terminal")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function to run the NumPy getting started guide"""
    print("🚀 NumPy Getting Started Guide")
    print("=" * 40)
    
    display_system_info()
    
    if check_numpy_installation():
        demonstrate_importing()
        demonstrate_first_steps()
        demonstrate_common_functions()
        demonstrate_help_resources()
        demonstrate_best_practices()
        run_installation_check()
        
        print("\n🎉 Congratulations! You're ready to use NumPy!")
        print("\n📝 Next Steps:")
        print("• Explore NumPy array creation methods")
        print("• Learn about array indexing and slicing")
        print("• Practice with mathematical operations")
        print("• Try broadcasting and vectorization")
        print("• Explore advanced NumPy features")
        
    else:
        demonstrate_installation_methods()
        print("\n⚠️ Please install NumPy first, then run this script again.")

if __name__ == "__main__":
    main()
