maker is a keyword argument marker to empahsize each point with a specified marker


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10.20,30.40,50.60])
ypoints = np.array([20.30,40.50,60.70])

plt.plot(xpoints, ypoints, marker = 'o')
plt.plot(xpoints, ypoints, marker = 'o')
plt.plot(xpoints, ypoints, marker = '*')



Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline