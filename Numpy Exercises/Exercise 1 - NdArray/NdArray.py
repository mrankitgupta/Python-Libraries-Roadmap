import numpy as np

a = np.arange(10,20)
print(a)

a=np.full((1,2),10)
print(a)

a = np.array([(1,2,3),(4,5,6)])
print(a)

import numpy as np
a = np.array([1,2,3])
print (a)

# more than one dimensions
import numpy as np
a = np.array([[1, 2], [3, 4]])
print (a)

# minimum dimensions
import numpy as np
a = np.array([1, 2, 3,4,5], ndmin = 2)
print (a)

# dtype parameter
import numpy as np
a = np.array([1, 2, 3], dtype = complex)
print (a)
