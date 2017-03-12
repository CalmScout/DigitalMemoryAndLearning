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


def generate_pairs(x, num_of_pairs):
    """
    Returns list which consist of num_of_pairs pairs of X list elements
    """
    pairs = []
    for _ in range(num_of_pairs):
        # element = [x[int(f_rand(0, len(x)))], x[int(f_rand(0, len(x)))]]
        element = [x[np.random.randint(0, len(x))], x[np.random.randint(0, len(x))]]
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


def plot_init_and_final_2D_vectors(init_list, final_list):
    """
    Plots two graphs - init vectors and final vectors
    """
    init = np.array(init_list)
    final = np.array(final_list)
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].scatter(init[:, 0], init[:, 1])
    axarr[0].set_title("Initial vectors")
    axarr[1].scatter(final[:, 0], final[:, 1])
    axarr[1].set_title("Final vectors")


num_of_iterations = 1000
NP = 400
# generate random vectors - input date
X = np.random.uniform(low=-10, high=10,size=(NP, 2, 1))
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
        half_list.append(XX[np.random.randint(0, len(XX))])

    crossed_list += half_list

    # mutation step
    # mutation probability in [0.001, 0.5]
    prob_mutation = 0.1
    epsilon = 0.1
    for i, el in enumerate(crossed_list):
        for ii, elel in enumerate(el):
            if generate_true(prob_mutation):
                if generate_true(0.5):
                    crossed_list[i][ii] += epsilon
                else:
                    crossed_list[i][ii] -= epsilon

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
plot_init_and_final_2D_vectors(X, final_list)
plt.show()