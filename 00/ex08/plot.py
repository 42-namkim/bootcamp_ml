import numpy as np
import matplotlib.pyplot as plt
import os, sys
path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path)
from ex07.vec_loss import loss_

def plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        print("Error: x and/or y and/or theta are not numpy.ndarray")
    elif x.ndim != 1 or y.ndim != 1:
        print("Error: x and/or y and/or theta are not 1D array")
    elif x.size != y.size:
        print("Error: x and y have not the same size")
    elif theta.size != 2:
        print("Error: theta shape is wrong")
    else:
        y_hat = np.array([theta[0] + theta[1] * x_i for x_i in x])
        plt.plot(x, y, 'b.')
        plt.plot(x, theta[1] * x + theta[0], '#FF7F50')
        for x_i, y_i, yh_i in zip(x, y, y_hat):
            plt.plot([x_i, x_i], [y_i, yh_i], 'r--')
        cost = loss_(y, y_hat) * 2  # why...?
        plt.title(f"Cost: {cost:.6f}")
        plt.show()