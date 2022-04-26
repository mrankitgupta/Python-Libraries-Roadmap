from matplotlib import pyplot as plt
# Importing Numpy Library
import numpy as np

plt.style.use('fivethirtyeight')
mu = 50
sigma = 7
x = np.random.normal(mu, sigma, size=200)
fig, ax = plt.subplots()
ax.hist(x, 20)
ax.set_title('Historgram')
ax.set_xlabel('bin range')
ax.set_ylabel('frequency')
fig.tight_layout()
plt.show()