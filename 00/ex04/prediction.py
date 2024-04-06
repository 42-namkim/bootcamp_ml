import numpy as np

def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * n.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """

    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        print("Error: x and/or theta are not numpy.ndarray")
        return None
    if theta.shape != (2, 1):
        print("Error: theta dimensions are not appropriate")
        return None
    if x.ndim == 1:
        x = x.reshape((-1, 1))
    if x.ndim == 2 and x.shape[1] == 1:
        x = np.hstack((np.ones((x.shape[0], 1)), x))
        return (np.dot(x, theta))
    else:
        print("Error: x dimensions are not appropriate")
        return None
    # res = [float(x[i] * theta[1] + theta[0]) for i in range(x.shape[0])]
    # return np.array(res)