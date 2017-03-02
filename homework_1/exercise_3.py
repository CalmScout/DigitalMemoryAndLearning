import numpy as np
from scipy import linalg

p = np.mat([[0.8, 0.1, 0.1],[0.2, 0.0, 0.8],[0.4, 0.4, 0.2]])

# Verify by simulation recurrent and transient states
x = np.mat([1.0, 0.0, 0.0])
print(x * p)