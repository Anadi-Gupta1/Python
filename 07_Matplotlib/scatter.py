"""1. Colors array

📊 Matplotlib Scatter Plot Guidecolors = np.random.randint(100, size=(100))

================================



This module demonstrates comprehensive scatter plot techniques using matplotlib.np.random.randint(100, size=(100)) → same as before, creates 100 random integers between 0 and 99.

Perfect for learning data visualization fundamentals and advanced scatter plot customization.

These numbers don’t go on the plot directly; instead, they are mapped to colors.

Author: Anadi Gupta

Date: September 2025Example:

Educational Focus: Data Visualization with Matplotlib

"""colors = [12, 87, 5, 43, ... 100 values ...]



import matplotlib.pyplot as plt

import numpy as npEach number corresponds to a color in the chosen colormap (nipy_spectral).

import warnings

warnings.filterwarnings('ignore')2. Sizes array

sizes = 10 * np.random.randint(100, size=(100))

# Set style for better-looking plots

plt.style.use('default')

Creates another 100 random integers (0–99).

def basic_scatter_plot():

    """Then multiplies each by 10 so the sizes aren’t too tiny.

    Example 1: Basic Scatter Plot

    Creates a simple scatter plot with fixed data points.sizes = [320, 40, 700, 150, ...]

    """

    print("🎯 Example 1: Basic Scatter Plot")

    Each value is used as the area of a circle in the scatter plot.

    # Sample data

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])So some points look small (40) and some huge (700).

    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

    3. Scatter plot

    plt.figure(figsize=(8, 6))plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

    plt.scatter(x, y)

    plt.title('Basic Scatter Plot', fontsize=14, fontweight='bold')

    plt.xlabel('X Values', fontsize=12)plt.scatter → creates a scatter plot.

    plt.ylabel('Y Values', fontsize=12)

    plt.grid(True, alpha=0.3)x, y → positions of each point (100 points total).

    plt.tight_layout()

    plt.show()c=colors → assigns a color to each point based on the colors array.

    print("✅ Basic scatter plot displayed!\n")

s=sizes → assigns a size to each point based on the sizes array.

def scatter_with_colors():

    """alpha=0.5 → makes each point semi-transparent (so overlapping points are visible).

    Example 2: Scatter Plot with Color Mapping

    Demonstrates how to use colors to represent a third dimension of data.cmap='nipy_spectral' → tells matplotlib how to map numbers in colors into actual colors.

    """

    print("🌈 Example 2: Scatter Plot with Color Mapping")Example: low numbers (0–20) → dark colors

    

    # Sample dataHigh numbers (80–99) → bright/vivid colors

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])

    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])4. Colorbar

    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])plt.colorbar()

    

    plt.figure(figsize=(10, 6))

    scatter = plt.scatter(x, y, c=colors, cmap='viridis', s=50)Adds a color scale bar on the side of the figure.

    plt.colorbar(scatter, label='Color Scale')

    plt.title('Scatter Plot with Color Mapping (Viridis)', fontsize=14, fontweight='bold')It shows the mapping between the numeric values in colors and their actual colors in nipy_spectral.

    plt.xlabel('X Values', fontsize=12)

    plt.ylabel('Y Values', fontsize=12)So if a point has colors[i] = 80, you can check the bar and know it’ll appear in the bright-yellow/pink region of that colormap.

    plt.grid(True, alpha=0.3)

    plt.tight_layout()5. Show

    plt.show()plt.show()

    print("✅ Color-mapped scatter plot displayed!\n")



def scatter_with_variable_sizes():Finally displays the figure with:

    """

    Example 3: Scatter Plot with Variable Sizes100 points

    Shows how to represent data magnitude using different point sizes.

    """Random positions (x, y)

    print("📏 Example 3: Scatter Plot with Variable Sizes")

    Random colors (colors)

    # Sample data

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])Random sizes (sizes)

    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

    sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])A colorbar legend

    

    plt.figure(figsize=(8, 6))

    plt.scatter(x, y, s=sizes, alpha=0.6, edgecolors='black', linewidth=0.5)

    plt.title('Scatter Plot with Variable Sizes', fontsize=14, fontweight='bold')this is called love 

    plt.xlabel('X Values', fontsize=12)ombine Color Size and Alpha

    plt.ylabel('Y Values', fontsize=12)You can combine a colormap with different sizes of the dots. This is best visualized if the dots are transparent:

    plt.grid(True, alpha=0.3)

    plt.tight_layout()Example

    plt.show()Create random arrays with 100 values for x-points, y-points, colors and sizes:

    print("✅ Variable-size scatter plot displayed!\n")

import matplotlib.pyplot as plt

def scatter_with_transparency():import numpy as np

    """

    Example 4: Scatter Plot with Transparency (Alpha)x = np.random.randint(100, size=(100))

    Demonstrates how transparency helps with overlapping data points.y = np.random.randint(100, size=(100))

    """colors = np.random.randint(100, size=(100))

    print("🔍 Example 4: Scatter Plot with Transparency")sizes = 10 * np.random.randint(100, size=(100))

    

    # Sample dataplt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])

    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])plt.colorbar()

    sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])

    plt.show()

    plt.figure(figsize=(8, 6))

    plt.scatter(x, y, s=sizes, alpha=0.5, color='red', edgecolors='darkred')can you explain each word of it x = np.random.randint(100, size=(100))

    plt.title('Scatter Plot with Transparency (Alpha=0.5)', fontsize=14, fontweight='bold')y = np.random.randint(100, size=(100))

    plt.xlabel('X Values', fontsize=12)ChatGPT said:

    plt.ylabel('Y Values', fontsize=12)

    plt.grid(True, alpha=0.3)Perfect 👍 Let’s take it word by word so nothing is confusing.

    plt.tight_layout()

    plt.show()Line:

    print("✅ Transparent scatter plot displayed!\n")x = np.random.randint(100, size=(100))



def advanced_scatter_plot():Break it down:

    """

    Example 5: Advanced Scatter Plot - Combining Colors, Sizes, and Alphanp

    Comprehensive example showing multiple visual dimensions simultaneously.

    """This is just the alias for NumPy, since earlier you wrote:

    print("🚀 Example 5: Advanced Multi-Dimensional Scatter Plot")

    import numpy as np

    # Generate random data

    np.random.seed(42)  # For reproducible results

    n_points = 100So whenever you write np, you’re using NumPy’s functions.

    

    x = np.random.randint(0, 100, size=n_points)np.random

    y = np.random.randint(0, 100, size=n_points)

    colors = np.random.randint(0, 100, size=n_points)This is NumPy’s random module.

    sizes = 10 * np.random.randint(5, 50, size=n_points)

    It contains functions for generating random numbers (integers, floats, normal distributions, etc.).

    plt.figure(figsize=(12, 8))

    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, np.random.randint(...)

                         cmap='nipy_spectral', edgecolors='black', linewidth=0.5)

    randint means random integer.

    # Add colorbar

    cbar = plt.colorbar(scatter)It generates random integers in a given range.

    cbar.set_label('Color Scale', fontsize=12)

    By default:

    plt.title('Advanced Scatter Plot: Colors + Sizes + Transparency', 

              fontsize=16, fontweight='bold', pad=20)np.random.randint(high, size=n)

    plt.xlabel('X Coordinates', fontsize=14)

    plt.ylabel('Y Coordinates', fontsize=14)

    plt.grid(True, alpha=0.3)generates random integers from 0 (inclusive) up to high (exclusive).

    

    # Add legend for sizes100 (the first argument)

    legend_sizes = [100, 300, 500]

    legend_labels = ['Small', 'Medium', 'Large']This is the upper limit (exclusive).

    for size, label in zip(legend_sizes, legend_labels):

        plt.scatter([], [], s=size, alpha=0.6, color='gray', So numbers will be chosen randomly from 0 to 99.

                   edgecolors='black', label=label)

    plt.legend(title='Point Sizes', loc='upper right', bbox_to_anchor=(1.15, 1))Example: it might give 23, 87, etc. but never 100.

    

    plt.tight_layout()size=(100)

    plt.show()

    print("✅ Advanced multi-dimensional scatter plot displayed!\n")This tells NumPy how many random numbers to generate.



def colormap_comparison():size=(100) means: "Give me an array of 100 random integers."

    """

    Example 6: Colormap ComparisonSo instead of one number, you get something like:

    Shows different colormap options available in matplotlib.

    """[34, 78, 12, 56, ... 100 values total ...]

    print("🎨 Example 6: Colormap Comparison")

    

    # Sample datax = ...

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])

    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])Assigns the generated array to the variable x.

    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

    So now x is a NumPy array of 100 random integers between 0 and 99.

    # Popular colormaps

    colormaps = ['viridis', 'plasma', 'inferno', 'magma', 'coolwarm', 'nipy_spectral']Same for y:

    y = np.random.randint(100, size=(100))

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    axes = axes.flatten()

    Exactly the same logic.

    for i, cmap in enumerate(colormaps):

        scatter = axes[i].scatter(x, y, c=colors, cmap=cmap, s=100)Just creates another independent array of 100 random integers (also from 0–99).

        axes[i].set_title(f'Colormap: {cmap}', fontsize=12, fontweight='bold')

        axes[i].grid(True, alpha=0.3)These become the y-coordinates for your scatter plot.

        plt.colorbar(scatter, ax=axes[i])

    ✅ After both lines:

    plt.suptitle('Popular Matplotlib Colormaps Comparison', 

                 fontsize=16, fontweight='bold', y=1.02)x = [23, 4, 88, 15, ...] (100 values)

    plt.tight_layout()

    plt.show()y = [67, 90, 12, 34, ...] (100 values)

    print("✅ Colormap comparison displayed!\n")



def interactive_demonstration():

    """

    Main function to run all scatter plot examples with user interaction.This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, up to 100, which is a yellow color.

    """

    print("=" * 60)How to Use the ColorMap

    print("🎯 MATPLOTLIB SCATTER PLOT COMPREHENSIVE GUIDE")You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

    print("=" * 60)

    print("This demonstration will show various scatter plot techniques.")In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot:

    print("Each example builds upon the previous one, teaching new concepts.")

    print("=" * 60)Example

    Create a color array, and specify a colormap in the scatter plot:

    examples = [

        ("1", "Basic Scatter Plot", basic_scatter_plot),import matplotlib.pyplot as plt

        ("2", "Color Mapping", scatter_with_colors),import numpy as np

        ("3", "Variable Sizes", scatter_with_variable_sizes),

        ("4", "Transparency Effects", scatter_with_transparency),x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

        ("5", "Advanced Multi-Dimensional", advanced_scatter_plot),y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

        ("6", "Colormap Comparison", colormap_comparison),colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

        ("7", "Run All Examples", lambda: run_all_examples())

    ]plt.scatter(x, y, c=colors, cmap='viridis')

    

    while True:plt.show()

        print("\n📊 Available Examples:")

        for num, desc, _ in examples:

            print(f"   {num}. {desc}")

        print("   0. Exit")Available ColorMaps

        You can choose any of the built-in colormaps:

        choice = input("\n🔍 Choose an example (0-7): ").strip()

        Name		 	Reverse	

        if choice == "0":Accent		 	Accent_r	

            print("\n👋 Thank you for exploring matplotlib scatter plots!")Blues		 	Blues_r	

            print("🎓 Keep practicing data visualization!")BrBG		 	BrBG_r	

            breakBuGn		 	BuGn_r	

        elif choice in [ex[0] for ex in examples]:BuPu		 	BuPu_r	

            example = next(ex for ex in examples if ex[0] == choice)CMRmap		 	CMRmap_r	

            print(f"\n🚀 Running: {example[1]}")Dark2		 	Dark2_r	

            example[2]()GnBu		 	GnBu_r	

        else:Greens		 	Greens_r	

            print("\n❌ Invalid choice. Please select 0-7.")Greys		 	Greys_r	

OrRd		 	OrRd_r	

def run_all_examples():Oranges		 	Oranges_r	

    """Run all scatter plot examples in sequence."""PRGn		 	PRGn_r	

    print("🎬 Running all examples in sequence...\n")Paired		 	Paired_r	

    basic_scatter_plot()Pastel1		 	Pastel1_r	

    scatter_with_colors()Pastel2		 	Pastel2_r	

    scatter_with_variable_sizes()PiYG		 	PiYG_r	

    scatter_with_transparency()PuBu		 	PuBu_r	

    advanced_scatter_plot()PuBuGn		 	PuBuGn_r	

    colormap_comparison()PuOr		 	PuOr_r	

    print("🎉 All examples completed successfully!")PuRd		 	PuRd_r	

Purples		 	Purples_r	

# Educational DocumentationRdBu		 	RdBu_r	

def display_learning_summary():RdGy		 	RdGy_r	

    """RdPu		 	RdPu_r	

    Display comprehensive learning summary about scatter plots.RdYlBu		 	RdYlBu_r	

    """RdYlGn		 	RdYlGn_r	

    summary = """Reds		 	Reds_r	

    📚 SCATTER PLOT LEARNING SUMMARYSet1		 	Set1_r	

    ================================Set2		 	Set2_r	

    Set3		 	Set3_r	

    🎯 What You Learned:Spectral		 	Spectral_r	

    Wistia		 	Wistia_r	

    1. **Basic Scatter Plots**YlGn		 	YlGn_r	

       - plt.scatter(x, y) - Creates basic scatter plotYlGnBu		 	YlGnBu_r	

       - Essential for showing relationships between two variablesYlOrBr		 	YlOrBr_r	

    YlOrRd		 	YlOrRd_r	

    2. **Color Mapping**afmhot		 	afmhot_r	

       - c=colors parameter maps values to colorsautumn		 	autumn_r	

       - cmap parameter chooses color schemebinary		 	binary_r	

       - plt.colorbar() adds color scale legendbone		 	bone_r	

    brg		 	brg_r	

    3. **Variable Sizes**bwr		 	bwr_r	

       - s=sizes parameter controls point sizescividis		 	cividis_r	

       - Represents magnitude of third variablecool		 	cool_r	

       - Useful for bubble chartscoolwarm		 	coolwarm_r	

    copper		 	copper_r	

    4. **Transparency (Alpha)**cubehelix		 	cubehelix_r	

       - alpha parameter controls transparency (0-1)flag		 	flag_r	

       - Helps with overlapping pointsgist_earth		 	gist_earth_r	

       - Improves readability of dense datagist_gray		 	gist_gray_r	

    gist_heat		 	gist_heat_r	

    5. **Advanced Techniques**gist_ncar		 	gist_ncar_r	

       - Combining multiple visual dimensionsgist_rainbow		 	gist_rainbow_r	

       - Professional styling and layoutsgist_stern		 	gist_stern_r	

       - Custom legends and annotationsgist_yarg		 	gist_yarg_r	

    gnuplot		 	gnuplot_r	

    6. **Colormap Options**gnuplot2		 	gnuplot2_r	

       - viridis, plasma, inferno (perceptually uniform)gray		 	gray_r	

       - coolwarm (diverging colors)hot		 	hot_r	

       - nipy_spectral (wide color range)hsv		 	hsv_r	

    inferno		 	inferno_r	

    🛠️ Key Parameters:jet		 	jet_r	

    - x, y: Data coordinatesmagma		 	magma_r	

    - c: Colors (can be array of values)nipy_spectral		 	nipy_spectral_r	

    - s: Sizes (can be array of values)ocean		 	ocean_r	

    - alpha: Transparency (0=transparent, 1=opaque)pink		 	pink_r	

    - cmap: Colormap nameplasma		 	plasma_r	

    - edgecolors: Border colors for pointsprism		 	prism_r	

    - linewidth: Border thicknessrainbow		 	rainbow_r	

    seismic		 	seismic_r	

    🎓 Best Practices:spring		 	spring_r	

    ✅ Use appropriate colormaps for your data typesummer		 	summer_r	

    ✅ Add colorbars when using color mappingtab10		 	tab10_r	

    ✅ Consider transparency for overlapping pointstab20		 	tab20_r	

    ✅ Label axes and add titlestab20b		 	tab20b_r	

    ✅ Use grids for better readabilitytab20c		 	tab20c_r	

    ✅ Choose appropriate point sizes for your data densityterrain		 	terrain_r	

    twilight		 	twilight_r	

    📊 Common Use Cases:twilight_shifted		 	twilight_shifted_r	

    - Scientific data visualizationviridis		 	viridis_r	

    - Correlation analysiswinter		 	winter_r	

    - Bubble charts for business data

    - Geographic data plotting

    - Machine learning result visualization

    """

    print(summary)

Size

if __name__ == "__main__":You can change the size of the dots with the s argument.

    # Run the interactive demonstration

    try:Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

        interactive_demonstration()

        Example

        # Show learning summarySet your own size for the markers:

        show_summary = input("\n📚 Would you like to see the learning summary? (y/n): ").strip().lower()

        if show_summary in ['y', 'yes']:import matplotlib.pyplot as plt

            display_learning_summary()import numpy as np

            

    except KeyboardInterrupt:x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

        print("\n\n👋 Program interrupted by user. Goodbye!")y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

    except Exception as e:sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

        print(f"\n❌ An error occurred: {e}")

        print("Please check your matplotlib installation and try again.")plt.scatter(x, y, s=sizes)

plt.show()
Result:



Alpha
You can adjust the transparency of the dots with the alpha argument.

Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

Example
Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()


