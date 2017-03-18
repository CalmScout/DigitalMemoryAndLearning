"""
Stochastic methods implementation: simulated annealing algorithm
"""
import numpy as np


def simulated_annealing(f, t_init, t_fin, n_iter, domain, h=(lambda t: 0.9 * t)):
    """
    Optimization algorithm.
    :param f: cost function
    :param t_init: initial temperature
    :param t_fin: final temperature
    :param n_iter: number of iterations per stage
    :param h: temperature function
    :param domain: list, contains boundaries for each variable
    :return: x_opt minimizing f
    """
    # generate random x in [domain[0], domain[1])
    x = np.random.rand() * (domain[1] - domain[0]) + domain[0]
    x_opt = x
    t = t_init
    k = 0


    def get_neighbour(x, eps=(domain[1] - domain[0])/2.0):
        x_min = x - eps if x - eps > domain[0] else domain[0]
        x_max = x + eps if x + eps < domain[1] else domain[1]
        return np.random.rand() * (x_max - x_min) + x_min

    while t > t_fin:
        while k < n_iter:
            y = get_neighbour(x)
            delta_f = f(y) - f(x)
            if delta_f < 0:
                x = y
                if f(x) < f(x_opt):
                    x_opt = x
            else:
                p = np.random.rand()
                if p < np.exp(-1.0 * delta_f / t):
                    x = y
            k = k + 1
        t = h(t)
    return x_opt