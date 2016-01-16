def Trapezoidal(f, a, b, n):
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    return h*s

def _my_special_problem():
    from math import exp
    def g(t):
        return exp(-t**4)

    a = -2;  b = 2
    n = 1000
    result = Trapezoidal(g, a, b, n)
    print result

if __name__ == '__main__':
    _my_special_problem()
