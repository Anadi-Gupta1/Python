"""
Professional Scatter Plot Examples with Matplotlib
Author: Anadi Gupta
Educational Focus: Data Visualization with Matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

def basic_scatter():
    """Basic scatter plot example"""
    print("Example 1: Basic Scatter Plot")
    
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, s=100, alpha=0.7, color='blue')
    plt.title('Basic Scatter Plot', fontsize=14, fontweight='bold')
    plt.xlabel('X Values', fontsize=12)
    plt.ylabel('Y Values', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Basic scatter plot displayed!")

def color_scatter():
    """Scatter plot with color mapping"""
    print("Example 2: Scatter Plot with Colors")
    
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=colors, cmap='viridis', s=100)
    plt.colorbar(scatter, label='Color Scale')
    plt.title('Scatter Plot with Color Mapping', fontsize=14)
    plt.xlabel('X Values', fontsize=12)
    plt.ylabel('Y Values', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Color scatter plot displayed!")

def size_scatter():
    """Scatter plot with variable sizes"""
    print("Example 3: Variable Size Scatter Plot")
    
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, s=sizes, alpha=0.6, color='green', edgecolors='black')
    plt.title('Variable Size Scatter Plot', fontsize=14)
    plt.xlabel('X Values', fontsize=12)
    plt.ylabel('Y Values', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Variable size scatter plot displayed!")

def advanced_scatter():
    """Advanced scatter plot combining multiple features"""
    print("Example 4: Advanced Multi-Dimensional Scatter Plot")
    
    np.random.seed(42)
    x = np.random.randint(0, 100, size=100)
    y = np.random.randint(0, 100, size=100)
    colors = np.random.randint(0, 100, size=100)
    sizes = 10 * np.random.randint(5, 50, size=100)
    
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, 
                         cmap='nipy_spectral', edgecolors='black')
    plt.colorbar(scatter, label='Color Scale')
    plt.title('Advanced Scatter: Colors + Sizes + Transparency', fontsize=14)
    plt.xlabel('X Coordinates', fontsize=12)
    plt.ylabel('Y Coordinates', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Advanced scatter plot displayed!")

def main():
    """Main demonstration function"""
    print("=" * 50)
    print("MATPLOTLIB SCATTER PLOT EXAMPLES")
    print("=" * 50)
    
    while True:
        print("\nChoose an example:")
        print("1. Basic Scatter Plot")
        print("2. Color Mapping")
        print("3. Variable Sizes")
        print("4. Advanced Multi-Dimensional")
        print("5. Run All Examples")
        print("0. Exit")
        
        choice = input("\nEnter choice (0-5): ").strip()
        
        if choice == "0":
            print("Thank you for learning matplotlib!")
            break
        elif choice == "1":
            basic_scatter()
        elif choice == "2":
            color_scatter()
        elif choice == "3":
            size_scatter()
        elif choice == "4":
            advanced_scatter()
        elif choice == "5":
            print("Running all examples...")
            basic_scatter()
            color_scatter()
            size_scatter()
            advanced_scatter()
            print("All examples completed!")
        else:
            print("Invalid choice. Please select 0-5.")

if __name__ == "__main__":
    main()