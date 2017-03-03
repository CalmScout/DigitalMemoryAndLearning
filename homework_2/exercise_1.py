"""
Gradient descent algorithm implementation.
"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from homework_2.cost import f0
from homework_2.cost import f00

alpha = 0.001

def grad(func, x):
    delta = 0.001
    return (func(x + delta) - func(x)) / delta

def gradient_descent(func, learning_rate, eps, init_value, boundaries):


# x = Symbol('x')
# y = x ** 2 + 1
# y_prime = y.diff(x)
# print(y)
# print(y_prime)