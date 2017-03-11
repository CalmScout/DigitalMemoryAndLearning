"""
Implements a simplified version of genetic algorithm iteration
"""
import matplotlib.pyplot as plt
import numpy as np


def f_booth(x, y):
    """
    Booth's function, global minimum f(1, 3) == 0
    -10 <= x,y <=10
    """
    return np.power(x + 2 * y - 7, 2) + np.power(2 * x + y - 5, 2)


def f_rand(a, b):
    """
    Returns uniformly distributed random in range [a, b)
    """
    return a + np.random.rand() * (b - a)


def generate_true(p):
    """
    Returns True with probability p, False with probability (1 - p)
    """
    t = np.random.rand()
    if t <= p:
        return True
    return False

num_of_iterations = 100
NP = 40
# generate random vectors
X = np.random.rand(NP, 2, 1)
# crossover
prob_cross = 0.5
pairs = []
for _ in range(int(NP / 2)):
    el=[]
    el.append(X[int(f_rand(0, len(X)))])
    el.append(X[int(f_rand(0, len(X)))])
    pairs.append(el)
crossed_list = []
for el in pairs:
    # we cross all coordinates, usually not all coordinates are crossed
    crossed_el = []
    for i in range(len(el)):
        if generate_true(prob_cross):
            crossed_el.append(el[0][i])
        else:
            crossed_el.append(el[1][i])
    crossed_el = np.array(crossed_el)
    crossed_list.append(crossed_el)
# contains half of selected parents
half_list = []
for _ in range(int(len(X) / 2)):
    half_list.append(X[int(f_rand(0, len(X)))])

# crossed_list.append(half_list)
# print(len(crossed_list))
for el in half_list:
    crossed_list.append(el)

# for index, value in enumerate(crossed_list):
#     print("{}, {}, {}".format(index, value, value.shape))

# mutation step
# mutation probability in [0.001, 0.5]
prob_mutation = 0.01
epsilon = 0.1
for i, el in enumerate(crossed_list):
    for ii, elel in enumerate(el):
        if generate_true(prob_mutation):
            crossed_list[i][ii] += epsilon

# selection step
# generate NP pairs
pairs_selection = []
for i in range(len(crossed_list)):
    el = []
    el.append(crossed_list[int(f_rand(0, len(crossed_list)))])
    el.append(crossed_list[int(f_rand(0, len(crossed_list)))])
    pairs_selection.append(el)

final_list = []
for idx, value in enumerate(pairs_selection):
    if f_booth(value[0][0], value[0][1]) < f_booth(value[1][0], value[1][1]):
        final_list.append(value[0])
    else:
        final_list.append(value[1])
print(final_list)