import numpy as np
from collections import Counter
def majority_classifier(y_train, X_test):
    counts = Counter(y_train)
    max_count = max(counts.values())
    for label in y_train:
        if counts[label] == max_count:
            majority = label
            break
    return np.full(len(X_test), majority, dtype=int)
