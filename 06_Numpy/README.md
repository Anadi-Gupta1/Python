# NumPy Module - Scientific Computing with Python

[![NumPy](https://img.shields.io/badge/NumPy-1.26.4-blue.svg)](https://numpy.org/)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()

This module provides a comprehensive introduction to NumPy (Numerical Python), the fundamental package for scientific computing in Python. All examples are designed for educational purposes and include detailed explanations.

## 📚 Module Contents

### 1. NumPy Introduction (`numpy_intro.py`)
- **Purpose**: Comprehensive introduction to NumPy fundamentals
- **Features**:
  - What is NumPy and why use it?
  - Performance comparison with Python lists (45x faster!)
  - Basic concepts and terminology
  - Version information and system details
  - Interactive demonstrations

### 2. Array Creation Operations (`array_creation_operations.py`)
- **Purpose**: Complete guide to creating NumPy arrays
- **Features**:
  - Basic array creation from lists and tuples
  - Multi-dimensional arrays (0D to 3D+)
  - Array creation functions (zeros, ones, arange, linspace)
  - Custom dimensions and data types
  - Array properties analysis

### 3. Array Indexing and Slicing (`array_indexing_slicing.py`)
- **Purpose**: Master array indexing and slicing techniques
- **Features**:
  - 1D, 2D, and 3D array indexing
  - Basic and advanced slicing operations
  - Boolean indexing for conditional selection
  - Fancy indexing with integer arrays
  - Array modification through indexing
  - Performance comparison (views vs copies)

### 4. Getting Started Guide (`numpy_getting_started_guide.py`)
- **Purpose**: Complete beginner's guide to NumPy
- **Features**:
  - System information and environment check
  - Installation methods and troubleshooting
  - Import conventions and best practices
  - First steps with arrays
  - Help resources and documentation links
  - Performance tips and memory efficiency

## 🚀 Key Learning Outcomes

After completing this module, you will understand:

- ✅ **NumPy Fundamentals**: What NumPy is and why it's essential for data science
- ✅ **Performance Benefits**: How NumPy arrays are 50x faster than Python lists
- ✅ **Array Creation**: Multiple methods to create arrays of various dimensions
- ✅ **Data Types**: Different NumPy data types and when to use them
- ✅ **Indexing & Slicing**: Access and modify array elements efficiently
- ✅ **Broadcasting**: Perform operations on arrays of different shapes
- ✅ **Best Practices**: Professional NumPy coding conventions

## 📋 Prerequisites

- Basic Python knowledge (variables, functions, control structures)
- Understanding of lists and basic data structures
- Python 3.6+ installed on your system

## 🛠️ Installation

```bash
# Install NumPy using pip
pip install numpy

# Install specific version
pip install numpy==1.26.4

# Using conda
conda install numpy
```

## 🏃‍♂️ Quick Start

```python
import numpy as np

# Create your first array
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Type: {type(arr)}")

# Basic operations
print(f"Sum: {np.sum(arr)}")
print(f"Mean: {np.mean(arr)}")
```

## 📖 Usage Examples

### Running Individual Modules

```bash
# Navigate to the NumPy directory
cd 06_Numpy

# Run the introduction module
python numpy_intro.py

# Run array creation examples
python array_creation_operations.py

# Run indexing and slicing examples
python array_indexing_slicing.py

# Run the getting started guide
python numpy_getting_started_guide.py
```

### Interactive Learning

Each module is designed to be:
- **Self-contained**: Run independently without dependencies
- **Interactive**: Provides immediate feedback and examples
- **Educational**: Includes explanations and best practices
- **Progressive**: Builds from basic to advanced concepts

## 🔧 Troubleshooting

### Common Issues

1. **ImportError: No module named 'numpy'**
   ```bash
   pip install numpy
   ```

2. **Version conflicts**
   ```bash
   pip install --upgrade numpy
   ```

3. **Permission errors**
   ```bash
   pip install --user numpy
   ```

### Getting Help

- 📖 [Official NumPy Documentation](https://numpy.org/doc/)
- 🎓 [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- 💬 [Stack Overflow - NumPy Tag](https://stackoverflow.com/questions/tagged/numpy)
- 🐛 [NumPy GitHub Issues](https://github.com/numpy/numpy/issues)

## 🎯 Next Steps

After mastering this module, consider exploring:

1. **Pandas**: Data manipulation and analysis
2. **Matplotlib**: Data visualization
3. **SciPy**: Scientific computing
4. **Scikit-learn**: Machine learning
5. **TensorFlow/PyTorch**: Deep learning

## 📊 Performance Notes

- **Memory Efficiency**: NumPy arrays use contiguous memory layout
- **Vectorization**: Operations are applied to entire arrays at once
- **Broadcasting**: Enables operations between arrays of different shapes
- **Views vs Copies**: Understanding when arrays share memory

## 🤝 Contributing

This is an educational project. Feel free to:
- Add more examples
- Improve documentation
- Fix bugs or typos
- Suggest new topics

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning.

## 👨‍💻 Author

**Anadi Gupta**
- Focus: Educational Python programming
- Specialization: Scientific computing and data science fundamentals

---

⭐ **Star this repository if you find it helpful for learning NumPy!**
