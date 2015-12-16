import numpy as np

def Trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    return (b-a)/float(n)*(np.sum(f(x)) - 0.5*(f(a) + f(b)))

def _my_special_problem():
    from numpy import exp
    def g(t):
        return exp(-t**4)

    a = -2;  b = 2
    n = 1000
    result = Trapezoidal(g, a, b, n)
    print result

if __name__ == '__main__':
    _my_special_problem()
