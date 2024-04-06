import numpy as np

def simple_predict(x, theta):
    
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.ndim != 1 or theta.ndim != 1 or theta.shape[0] != 2 or len(x) == 0:
        return None
    res = [float(x[i] * theta[1] + theta[0]) for i in range(x.shape[0])]
    return np.array(res)