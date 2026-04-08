import numpy as np

def bernoulli_pmf_and_moments(x, p):
    x = np.asarray(x)
    pmf = np.where(x == 1, p , 1.0 - p)

    if pmf.ndim == 0:
        pmf = float(pmf)
    mean = p
    var = p * (1 - p)

    return pmf, mean, var