import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    if reduction=="sum":
        return float(np.sum(np.maximum(0, margin-(y_true*y_score))))
    if reduction=="mean":
        return float(np.mean(np.maximum(0, margin-(y_true*y_score))))