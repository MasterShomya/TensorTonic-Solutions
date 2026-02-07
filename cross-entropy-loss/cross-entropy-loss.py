import numpy as np

def cross_entropy_loss(y_true, y_pred):
    probs=[]
    for i in range(len(y_pred)):
        probs.append(y_pred[i][y_true[i]])
    ce = -np.mean(np.log(probs))
    return ce