"""
Matplotlib Subplots and Customizations - Comprehensive Visualization Guide
============================================================================

Educational guide to creating subplots, customizing plots, and using different plot types in Matplotlib.
Includes layout management, styling, legends, annotations, and best practices for data visualization.

Author: Python Learning Notes
Date: September 2025
Topic: Matplotlib, Subplots, Customization, Visualization
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# SUBPLOTS AND LAYOUTS
# =============================================================================

def subplots_demo():
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.exp(-x)
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs[0, 0].plot(x, y1, 'r-', label='sin(x)')
    axs[0, 0].set_title('Sine')
    axs[0, 1].plot(x, y2, 'b--', label='cos(x)')
    axs[0, 1].set_title('Cosine')
    axs[1, 0].plot(x, y3, 'g-.', label='tan(x)')
    axs[1, 0].set_title('Tangent')
    axs[1, 1].plot(x, y4, 'm:', label='exp(-x)')
    axs[1, 1].set_title('Exponential Decay')
    for ax in axs.flat:
        ax.legend()
        ax.grid(True)
    plt.tight_layout()
    plt.savefig('07_Matplotlib_Visualization_Notes/subplots_demo.png')
    plt.close(fig)

# =============================================================================
# CUSTOMIZATIONS AND ANNOTATIONS
# =============================================================================

def customizations_demo():
    x = np.linspace(0, 10, 100)
    y = np.log(x + 1)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color='purple', linewidth=2, marker='o', label='log(x+1)')
    ax.set_title('Logarithmic Growth', fontsize=14, fontweight='bold')
    ax.set_xlabel('X Value', fontsize=12)
    ax.set_ylabel('Y Value', fontsize=12)
    ax.legend(loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.7)
    # Annotation
    ax.annotate('Start Point', xy=(0, 0), xytext=(2, 1), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.savefig('07_Matplotlib_Visualization_Notes/customizations_demo.png')
    plt.close(fig)

# =============================================================================
# MULTIPLE PLOT TYPES
# =============================================================================

def multiple_plot_types_demo():
    categories = ['A', 'B', 'C', 'D']
    values = [23, 45, 12, 37]
    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    # Bar plot
    axs[0].bar(categories, values, color='skyblue')
    axs[0].set_title('Bar Plot')
    # Pie chart
    axs[1].pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    axs[1].set_title('Pie Chart')
    # Scatter plot
    x = np.random.rand(50)
    y = np.random.rand(50)
    axs[2].scatter(x, y, color='orange', alpha=0.7)
    axs[2].set_title('Scatter Plot')
    plt.tight_layout()
    plt.savefig('07_Matplotlib_Visualization_Notes/multiple_plot_types_demo.png')
    plt.close(fig)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    subplots_demo()
    customizations_demo()
    multiple_plot_types_demo()
    print("Matplotlib subplots and customizations demo images saved.")

if __name__ == "__main__":
    main()
