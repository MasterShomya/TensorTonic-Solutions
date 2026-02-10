import numpy as np
def dice_loss(p, y, eps=1e-8):
    p,y = np.asarray(p).flatten(),np.asarray(y).flatten()
    dice = (2*np.sum(p*y)+eps) / (np.sum(p) + np.sum(y)+eps)
    loss = 1 - dice
    return loss