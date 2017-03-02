import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

p = np.mat([[0.8, 0.1, 0.1],[0.2, 0.0, 0.8],[0.4, 0.4, 0.2]])

# Verify by simulation recurrent and transient states
x = np.mat([1.0, 0.0, 0.0])

def step(p, state):
    # sum_prob[i] contains sum: p[state, 0] + p[state, 1] + ... + [pstate, i]
    sum_prob = []
    for j in range(p.shape[1]):
        sum = 0
        for k in range(0, j):
            print(k, )
            sum += p[state,k]
        sum_prob.append(sum)
    print(sum_prob)


for el in range(3):
    step(p, el)