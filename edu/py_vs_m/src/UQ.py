"""
Integrate cos(t) from a to 2, where a is an uncertain
parameter, normally distributed around 1 with std.dev. 0.2.
"""
from Trapezoidal_vec import Trapezoidal
import numpy as np
N = 100000       # Monte Carlo samples
a = np.random.normal(loc=-2, scale=0.2, size=N)  # N samples of a
I = np.zeros(N)  # Responses (integrals)
for i in range(N):
    I[i] = Trapezoidal(np.cos, a[i], 2, n=1000)
print 'Integral of cos(t) from t=-2 to t=2:', np.sin(2) - np.sin(-2)
print 'Mean value of uncertain integral:', np.mean(I)
print 'Standard deviation of uncertain integral:', np.std(I)
