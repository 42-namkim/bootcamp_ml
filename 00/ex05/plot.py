import numpy as np
from matplotlib import pyplot as plt

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        print("Error: x and/or y and/or theta are not numpy.ndarray")
    elif x.ndim != 1 or y.ndim != 1:
        print("Error: x and/or y and/or theta are not 1D array")
    elif x.size != y.size:
        print("Error: x and y have not the same size")
    elif theta.ndim !=2 or theta.size != 2:
        print("Error: theta shape is wrong")
    else:
        plt.plot(x, y, 'k.')
        plt.plot(x, theta[1] * x + theta[0])
        plt.show()