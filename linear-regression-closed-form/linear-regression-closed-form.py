import numpy as np

def linear_regression_closed_form(X, y):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float).reshape(-1, 1)

    w = np.linalg.pinv(X.T @ X) @ X.T @ y
    return w.flatten().tolist()
