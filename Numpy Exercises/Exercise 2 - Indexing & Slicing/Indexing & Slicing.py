import numpy as np
a = np.arange(10)
s = slice(2,7,2)
print (a[s])

import numpy as np
a = np.arange(10)
b = a[2:7:2]
print (b)

# slice single item
import numpy as np
a = np.arange(10)
b = a[5]
print (b)

# slice items starting from index
import numpy as np
a = np.arange(10)
print (a[2:])

# slice items between indexes
import numpy as np
a = np.arange(10)
print (a[2:5])

import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a)
# slice items starting from index
print ('Now we will slice the array from the index a[1:]')
print (a[1:])

# array to begin with
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print ('Our array is:')
print (a)
# this returns array of items in the second column
print ('\n The items in the second column are:')
print (a[...,1])
# Now we will slice all items from the second row
print ('\n The items in the second row are:')
print (a[1,...])
# Now we will slice all items from column 1 onwards
print ('\n The items column 1 onwards are:')
print (a[...,1:])