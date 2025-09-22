Start Angle
As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.

The startangle parameter is defined with an angle in degrees, default angle is 0:

Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

The explode parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed:


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 


1. Data values
y = np.array([35, 25, 25, 15])


np.array(...) creates a NumPy array.

These numbers are the sizes of each slice in the pie chart.

So:

Apples → 35

Bananas → 25

Cherries → 25

Dates → 15

👉 The pie chart will divide the circle according to these values.

2. Labels
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]


These are the names of each slice.

When the pie is drawn, each slice will have the corresponding label.

3. Explode
myexplode = [0.2, 0, 0, 0]


explode makes slices “pop out” of the pie.

Each number represents how far a slice should move outward.

0.2 → Apples slice will move outward a little.

0, 0, 0 → Bananas, Cherries, Dates stay in place.

4. Pie chart
plt.pie(y, labels = mylabels, explode = myexplode)


y → sizes of slices.

labels=mylabels → adds labels to each slice.

explode=myexplode → moves out the first slice (Apples).

5. Show
plt.show()


Displays the pie chart with:

Apples (largest slice, pulled out)

Bananas

Cherries

Dates



Matplotlib Pie Charts
Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:

ExampleGet your own Python Server
A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 
Result:


As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).

By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:



Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:

The value divided by the sum of all values: x/sum(x)

REMOVE ADS

Labels
Add labels to the pie chart with the labels parameter.

The labels parameter must be an array with one label for each wedge:

Example
A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 
Result:


Start Angle
As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.

The startangle parameter is defined with an angle in degrees, default angle is 0:



Example
Start the first wedge at 90 degrees:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 
Result:


Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

The explode parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed:

Example
Pull the "Apples" wedge 0.2 from the center of the pie:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 
Result:


Shadow
Add a shadow to the pie chart by setting the shadows parameter to True:

Example
Add a shadow:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 
Result:


Colors
You can set the color of each wedge with the colors parameter.

The colors parameter, if specified, must be an array with one value for each wedge:

Example
Specify a new color for each wedge:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 
Result:


You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:

'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White

Legend
To add a list of explanation for each wedge, use the legend() function:

Example
Add a legend:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 
Result:


Legend With Header
To add a header to the legend, add the title parameter to the legend function.

Example
Add a legend with a header:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 