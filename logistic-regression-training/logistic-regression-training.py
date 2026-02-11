import numpy as np

def _sigmoid(z):
    return np.where(z >= 0,
                    1/(1+np.exp(-z)),
                    np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):

    x = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    n, d = x.shape
    w = np.zeros(d)
    b = 0.0

    for _ in range(steps):
        z = x @ w + b
        p = _sigmoid(z)
        eps = 1e-9
        loss = -np.mean(y*np.log(p+eps) + (1-y)*np.log(1-p+eps))
        grad_w = (x.T @ (p - y)) / n
        grad_b = np.mean(p - y)
        w -= lr * grad_w
        b -= lr * grad_b

    return w, b
