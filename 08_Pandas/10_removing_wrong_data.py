or small data sets you might be able to replace the wrong data one by one, but not for big data sets.

To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

Example
Loop through all values in the "Duration" column.

If the value is higher than 120, set it to 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


print(df.to_string())



Removing Rows
Another way of handling wrong data is to remove the rows that contains wrong data.

This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

Example
Delete rows where "Duration" is higher than 120:

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)



    