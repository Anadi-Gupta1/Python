# Matplotlib Module - Data Visualization with Python

[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.0-orange.svg)](https://matplotlib.org/)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)]()

This module provides comprehensive examples and tutorials for Matplotlib, the most popular plotting library in Python. All examples are designed for educational purposes with detailed explanations.

## 📚 Module Contents

### 1. Basic Plotting Examples (`basic_plotting_examples.py`)
- **Purpose**: Introduction to fundamental plotting techniques
- **Features**:
  - Line plots with basic customization
  - Bar charts and histograms
  - Pie charts for data distribution
  - Basic plot formatting and display

### 2. Plot Markers Guide (`plot_markers_guide.py`)
- **Purpose**: Comprehensive guide to plot markers and symbols
- **Features**:
  - Complete marker reference guide
  - Different marker shapes and sizes
  - Marker customization examples
  - Visual marker comparison

### 3. Advanced Plotting Styles (`advanced_plotting_styles.py`)
- **Purpose**: Advanced styling and formatting techniques
- **Features**:
  - Multiple marker types and combinations
  - Line styles (solid, dashed, dotted, dash-dot)
  - Color customization (named colors, hex values)
  - Line width variations
  - Performance comparisons and examples

### 4. Labels and Titles (`labels_and_titles.py`)
- **Purpose**: Professional labeling and title formatting
- **Features**:
  - Axis labels and plot titles
  - Font customization (family, size, weight, style)
  - Text positioning and alignment
  - Professional presentation techniques

### 5. Subplot Layout Examples (`subplot_layout_examples.py`)
- **Purpose**: Creating multiple plots in organized layouts
- **Features**:
  - Grid-based subplot arrangements
  - Figure size and spacing management
  - Individual subplot customization
  - Professional multi-plot presentations

### 6. Scatter Plot Examples (`scatter_plot_examples.py`)
- **Purpose**: Comprehensive scatter plot demonstrations
- **Features**:
  - Basic and advanced scatter plots
  - Color mapping and size variations
  - Data correlation visualization
  - Professional scatter plot styling

### 7. Pie Chart Examples (`pie_chart_examples.py`)
- **Purpose**: Professional pie chart creation and customization
- **Features**:
  - Basic pie chart creation
  - Custom colors and styling
  - Labels and percentage display
  - Exploded pie chart effects

### 8. Grid Customization (`grid_customization.py`)
  - Title positioning (left, center, right)
  - Advanced text formatting
  - Multiple font families demonstration

### 5. Subplot Layouts (`matplotlib_subplot.py`)
- **Purpose**: Creating multiple plots in single figures
- **Features**:
  - Grid layouts (1x2, 2x1, 2x3, 2x2)
  - Individual subplot titles
  - Super titles for entire figures
  - Different plot types in subplots
  - Mathematical function examples

### 6. Grid Customization (`grid_customization.py`)
- **Purpose**: Grid styling and customization
- **Features**:
  - Grid line customization
  - Grid transparency and styling
  - Different grid patterns
  - Professional plot appearance

## 🚀 Key Learning Outcomes

After completing this module, you will master:

- ✅ **Basic Plotting**: Line plots, bar charts, histograms, pie charts
- ✅ **Plot Customization**: Markers, colors, line styles, fonts
- ✅ **Professional Layouts**: Subplots, grids, multiple figures
- ✅ **Text and Labels**: Titles, axis labels, legends, annotations
- ✅ **Advanced Styling**: Custom fonts, colors, transparency
- ✅ **Best Practices**: Clean, readable, publication-ready plots

## 📋 Prerequisites

- Basic Python knowledge
- NumPy fundamentals (arrays and basic operations)
- Understanding of mathematical concepts (optional for advanced examples)

## 🛠️ Installation

```bash
# Install required packages
pip install matplotlib numpy

# For interactive plots (optional)
pip install ipywidgets

# For enhanced backends (optional)
pip install tk
```

## 🏃‍♂️ Quick Start

```python
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create basic plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.title('My First Matplotlib Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## 📖 Usage Examples

### Running Individual Modules

```bash
# Navigate to the Matplotlib directory
cd 07_Matplotlib

# Run basic plotting examples
python basic_plotting_examples.py

# Learn about markers
python plot_markers_guide.py

# Explore advanced styling
python advanced_plotting_styles.py

# Master labels and titles
python labels_and_titles.py

# Create subplot layouts
python matplotlib_subplot.py

# Customize grids
python grid_customization.py
```

## 🎨 Plot Types Covered

| Plot Type | Purpose | Example Use Cases |
|-----------|---------|-------------------|
| **Line Plot** | Show trends over time | Stock prices, temperature changes |
| **Bar Chart** | Compare categories | Sales by region, survey results |
| **Histogram** | Show data distribution | Test scores, height distribution |
| **Pie Chart** | Show proportions | Market share, budget breakdown |
| **Scatter Plot** | Show relationships | Correlation analysis, clustering |
| **Subplot** | Multiple comparisons | Dashboard layouts, comparative analysis |

## 🔧 Advanced Features

### Customization Options
- **Colors**: Named colors, hex codes, RGB values, transparency
- **Markers**: 20+ marker types with size and edge customization
- **Lines**: Solid, dashed, dotted, dash-dot styles with width control
- **Fonts**: Multiple families (serif, sans-serif, monospace) with weight/style
- **Layouts**: Flexible subplot grids with individual and super titles

### Professional Styling
- Grid customization for clean appearance
- Color schemes for accessibility
- Font selection for readability
- Layout optimization for presentations

## 🤝 Contributing

This is an educational project. Contributions welcome:
- Add new plot types or examples
- Improve documentation
- Fix bugs or enhance existing examples
- Suggest new visualization techniques

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning.

## 👨‍💻 Author

**Anadi Gupta**
- Focus: Data visualization and scientific computing education
- Specialization: Python plotting libraries and best practices

---

⭐ **Star this repository if you find it helpful for learning Matplotlib!**