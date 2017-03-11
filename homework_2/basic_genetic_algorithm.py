"""
Implements a simplified version of genetic algorithm
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


def generate_pairs(x, num_of_pairs):
    """
    Returns list which consist of num_of_pairs pairs of X list elements
    """
    pairs = []
    for _ in range(num_of_pairs):
        element = [x[int(f_rand(0, len(x)))], x[int(f_rand(0, len(x)))]]
        pairs.append(element)
    return pairs


def generate_true(p):
    """
    Returns True with probability p, False with probability (1 - p)
    """
    t = np.random.rand()
    if t <= p:
        return True
    return False

num_of_iterations = 10000
NP = 1000
# generate random vectors - input date
X = np.random.rand(NP, 2, 1)
# crossover
prob_cross = 0.5
XX = X
for k in range(num_of_iterations):
    if(k % 10 == 0):
        print("Iteration # ", k)
    pairs = generate_pairs(XX, int(NP / 2))

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
    for _ in range(int(len(XX) / 2)):
        half_list.append(XX[int(f_rand(0, len(XX)))])

    crossed_list += half_list

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
    pairs_selection = generate_pairs(crossed_list, len(crossed_list))

    final_list = []
    for idx, value in enumerate(pairs_selection):
        if f_booth(value[0][0], value[0][1]) < f_booth(value[1][0], value[1][1]):
            final_list.append(value[0])
        else:
            final_list.append(value[1])
    XX = final_list
index_of_optimum = 0
for idx, el in enumerate(final_list):
    if f_booth(el[0], el[1]) < f_booth(final_list[index_of_optimum][0], final_list[index_of_optimum][1]):
        index_of_optimum = idx
# print(final_list)
print(final_list[index_of_optimum])