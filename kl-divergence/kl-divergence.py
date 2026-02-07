import numpy as np

def kl_divergence(p, q, eps=1e-12):
    kl=0
    for i in range(len(p)):
        if p[i]==0:
            continue
        kl+=p[i]*np.log(p[i]/(q[i]+eps))
    return kl