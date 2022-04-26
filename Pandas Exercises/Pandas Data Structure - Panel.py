import pandas as pd
import numpy as np

# Create Panel from 3D ndarray
# creating an empty panel
data = np.random.rand(2,4,5)
p = pd.Panel (data)
print (p)