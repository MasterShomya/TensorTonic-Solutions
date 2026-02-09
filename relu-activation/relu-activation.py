import numpy as np

def relu(x):
    x = np.array(x)
    if x.shape == ():
        x = x.reshape(-1)
    return np.maximum(0,x)