import numpy as np
from collections import Counter
def entropy_node(y):
    if len(y)==0:
        return 0.0
    counts=Counter(y)
    total = len(y)
    entropy=0.0
    for i in counts.values():
        p = i/total
        if p>0:
            entropy-=(p*np.log2(p))
    return float(max(entropy, 0.0))
