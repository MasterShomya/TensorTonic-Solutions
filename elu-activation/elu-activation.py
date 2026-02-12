import numpy as np
def elu(x, alpha):
    x = np.asarray(x)
    return list(np.where(x>0, x, alpha*(np.exp(x)-1)))