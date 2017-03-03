import numpy


def f00(x):
    y = numpy.power(x, 4) / 4 + numpy.power(x, 3) / 3 - 5 * numpy.power(x, 2) / 2 + 3 * x - 2
    return y


def f0(x):
    y = numpy.power(x, 3) - 6 * numpy.power(x, 2) + 9 * x + 1
    return y


def f2(x, y):
    z = numpy.power(x, 2) + numpy.power(y, 2)
    return z

