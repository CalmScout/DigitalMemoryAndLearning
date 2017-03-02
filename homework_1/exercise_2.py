import numpy as np
from scipy import linalg

p = np.matrix([[0.5, 0.25, 0.0, 0.25, 0.0, 0.0, 0.0],
              [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5],
              [0.0, 0.0, 1.0/8.0, 0.0, 7.0/8.0, 0.0, 0.0],
              [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.75],
              [0.0, 1.0/9.0, 7.0/9.0, 0.0, 0.0, 1.0/9.0, 0.0],
              [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]])

def transition_probability(p_matrix, i, j, n):
    temp_p_matrix = p_matrix
    for el in range(0,n - 1):
        temp_p_matrix *= p_matrix
    return temp_p_matrix[i - 1, j - 1]

# Calculate P(X_2 = 6| X_0 = 3)
print("P(X_2 = 6| X_0 = 3) ==", "{:6.3f}".format(transition_probability(p, 3, 6, 2)))

# Calculate P(x_2 = 4| x_0 = 2)
print("P(x_2 = 4| x_0 = 2) ==", "{:6.3f}".format(transition_probability(p, 2, 4, 2)))
