import numpy as np

def swish(x):
    x = np.asarray(x)
    return (1/(1+np.exp(-x)))*x