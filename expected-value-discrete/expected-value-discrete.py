import numpy as np

def expected_value_discrete(x, p):
    x = np.asarray(x)
    p = np.asarray(p)

    if x.shape != p.shape:
        raise ValueError("shapes of x and p must match")

    if not np.allclose(np.sum(p), 1.0, atol= 1e-6):
        raise ValueError("probabilities must sum to 1")

    return float(np.sum(x * p))

    