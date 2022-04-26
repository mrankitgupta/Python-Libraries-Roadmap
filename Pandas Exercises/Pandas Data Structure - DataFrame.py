#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

# Create an Empty DataFrame
df = pd.DataFrame()
print (df)

# Create a DataFrame from Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)

data = [['Ankit',21],['Bob',24],['Clarke',20]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)

# Create a DataFrame from Dict of ndarrays / Lists
data = {'Name':['Ankit', 'Gupta', 'Steve', 'Ricky'],'Age':[21,22,29,32]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)

# Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)

# Create a DataFrame from Dict of Series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print (df)

# Column Addition
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
# Adding a new column to an existing DataFrame object with column label by passing new series
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)
print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print (df)

# Column Deletion
print ("Deleting the first column using DEL function:")
del df['one']
print ("Deleting another column using POP function:")
df.pop('two')
print (df)

# Row Selection
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print (df.loc['b']) # Row Selection by Label
print (df.iloc(2)) # Row Selection by Integer Location
# Slice Rows
print (df[2:4])

# Deletion of Row & Addition of Rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2) # Add new rows to a DataFrame using the append function
# Drop rows with label 0
df = df.drop(0) # delete or drop rows from a DataFrame
print (df)
