Let's try to convert all cells in the 'Date' column into dates.

Pandas has a to_datetime() method for this:

ExampleGet your own Python Server
Convert to date:

import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())


Replacing Values
One way to fix wrong values is to replace them with something else.

In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

ExampleGet your own Python Server
Set "Duration" = 45 in row 7:

df.loc[7, 'Duration'] = 45
