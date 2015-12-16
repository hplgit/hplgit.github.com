def Trapezoidal(f, a, b, n):
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(0,n,1):
        s = s + f(a + i*h)
    return h*s

from math import exp  # or from math import *
def g(t):
    return exp(-t**4)

a = -2;  b = 2
n = 1000
result = Trapezoidal(g, a, b, n)
print result
