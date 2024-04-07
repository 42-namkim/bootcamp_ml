import numpy as np


def mse_elem(y, y_hat):
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    elif y.shape != y_hat.shape or y.size == 0 or y_hat.size == 0:
        return None
    else:
        return (y_hat - y) ** 2

def mse_(y, y_hat):
    """
    Description:
    Calculate the MSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    elif y.shape != y_hat.shape or y.size == 0 or y_hat.size == 0:
        return None
    else:
        return sum(mse_elem(y, y_hat)) / y.size

def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        rmse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    elif y.shape != y_hat.shape or y.size == 0 or y_hat.size == 0:
        return None
    else:
        return np.sqrt(mse_(y, y_hat))

def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        mae: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    elif y.shape != y_hat.shape or y.size == 0 or y_hat.size == 0:
        return None
    else:
        return sum(abs(y_hat - y)) / y.size

def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
        y: has to be a numpy.array, a vector of dimension m * 1.
        y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
        r2score: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    elif y.shape != y_hat.shape or y.size == 0 or y_hat.size == 0:
        return None
    else:
        return 1 - (sum((y_hat - y) ** 2) / sum((y - y.mean()) ** 2))