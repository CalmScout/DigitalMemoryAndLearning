import numpy as np
import inspect


def f00(x):
    """
    x in [-4, 3]
    """
    y = np.power(x, 4) / 4 + np.power(x, 3) / 3 - 5 * np.power(x, 2) / 2 + 3 * x - 2
    return y


def f0(x):
    """
    x in [-0.5, 4.5]
    """
    y = np.power(x, 3) - 6 * np.power(x, 2) + 9 * x + 1
    return y


def f1(x1, x2, x3):
    """
    -5.12 <= x1, x2, x3 <= 5.12
    """
    return np.power(x1, 2) + np.power(x2, 2) + np.power(x3, 2)


def f2(x1, x2):
    """
    -2.048 <= x1, x2 <= 2.048
    """
    return 100 * np.power(np.power(x1, 2) - x2, 2) + np.power(1 - x1, 2)


def f3(x1, x2, x3, x4, x5):
    """
    -5.12 <= x1, x2, x3, x4, x5 <= 5.12
    """
    return np.floor(x1) + np.floor(x2) + np.floor(x3) + np.floor(x4) + np.floor(x5)


def f4(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    """
    -5.12 <= x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 <= 5.12
    """
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)

    def get_new_random(hist_list):
        """
        Generate new random in [0, 1) if it is not in hist_list and add it to hist_list
        """
        el = np.random.rand()
        if el not in hist_list:
            hist_list.append(el)
            return el
        while el in hist_list:
            el = np.random.rand()
        hist_list.append(el)
        return el

    randoms = []
    result = 0.0
    for arg in args:
        result += np.power(values[arg], 4) + get_new_random(randoms)
    print(len(randoms))
    return result


def f5(x1, x2):
    """
    -65.536 <= x1, x2 <= 65.536
    """
    a11 = -16 * (np.mod(16, 5) - 2)
    a12 = -16 * (np.mod(16, 5) - 2)
    a21 = 32
    a22 = 32
    z = 1. / (0.002 + 51. / (2 + np.power((x1 - a11), 6) + np.power((x1 - a12), 6))
              + 51. / (3 + np.power((x2 - a21), 6) + np.power((x2 - a22), 6)))
    return z