import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    x = comb(n, k)
    pmf = x * (p ** k) * ((1 -p) ** (n -k))

    i = np.arange(k + 1)
    y = comb(n,i)
    cdf = np.sum(y * (p ** i) * ((1 - p) ** (n - i)))

    return float(pmf), float(cdf)