from Trapezoidal import Trapezoidal
from Trapezoidal_vec import Trapezoidal as Trapezoidal_vec

def linear():
    """Test linear integrand: exact result for any n."""

    def f(x):
        return 8*x + 6

    def F(x):
        """Anti-derivative of f(x)."""
        return 4*x**2 + 6*x

    a = 2
    b = 6
    exact = F(b) - F(a)
    numerical = Trapezoidal(f, a, b, n=4)
    error = exact - numerical
    print '%.16f' % error

# Call linear:
#linear()

def test_linear():
    """Test linear integrand: exact result for any n."""

    def f(x):
        return 8*x + 6

    def F(x):
        """Anti-derivative of f(x)."""
        return 4*x**2 + 6*x

    a = 2
    b = 6
    expected = F(b) - F(a)
    tol = 1E-14
    computed = Trapezoidal(f, a, b, n=4)
    error = abs(expected - computed)
    msg = 'Trapezoidal: expected=%g, computed=%g, error=%g' % \
          (expected, computed, error)
    assert error < tol, msg

def test_linear_symbolic():
    """Test linear integrand: exact result for any n."""
    import sympy as sym
    # Define a linear expression and integrate it
    x = sym.symbols('x')
    f = 8*x + 6                 # Integrand for this test
    F = sym.integrate(f, x)
    # Verify symbolic computation: F'(x) == f(x)
    assert sym.diff(F, x) == f
    # Transform expressions f and F to Python functions of x
    f = sym.lambdify([x], f, modules='numpy')
    F = sym.lambdify([x], F, modules='numpy')

    # Run one test with fixed a, b, n, for scalar and
    # vectorized implementation
    a = 2
    b = 6
    expected = F(b) - F(a)
    tol = 1E-14
    for func in Trapezoidal, Trapezoidal_vec:
        computed = func(f, a, b, n=4)
        error = abs(expected - computed)
        msg = 'expected=%g, computed=%g, error=%g' % \
              (expected, computed, error)
        assert error < tol, msg

def test_linear_symbolic_large_limits():
    """Test linear integrand: exact result for any n, large limits."""
    import sympy as sym
    # Define a linear expression and integrate it
    x = sym.symbols('x')
    f = 8*x + 6                 # Integrand for this test
    F = sym.integrate(f, x)
    # Verify symbolic computation: F'(x) == f(x)
    assert sym.diff(F, x) == f
    # Transform expressions f and F to Python functions of x
    f = sym.lambdify([x], f, modules='numpy')
    F = sym.lambdify([x], F, modules='numpy')

    # Run one test with fixed a, b, n.
    a = 2E+8
    b = 6E+9
    expected = F(b) - F(a)
    tol = 1E-14
    for func in Trapezoidal, Trapezoidal_vec:
        print func.__name__
        computed = func(f, a, b, n=4)
        error = abs(expected - computed)/abs(expected)
        msg = 'expected=%g, computed=%g, error=%g' % \
              (expected, computed, error)
        assert error < tol, msg

def test_convergence_rate():
    import sympy as sym
    # Construct test problem
    x = sym.symbols('x')
    F = sym.exp(-x)*sym.sin(2*x)  # Anti-derivative
    f = sym.diff(F, x)            # Integrand for this test
    # Turn to Python functions
    f = sym.lambdify([x], f, modules='numpy')
    F = sym.lambdify([x], F, modules='numpy')

    a = 0.1
    b = 0.9
    expected = F(b) - F(a)
    # Run experiments (double n in each experiment)
    n = 1
    errors = []
    for k in range(28):
        n *= 2
        computed = Trapezoidal(f, a, b, n)
        error = abs(expected - computed)
        errors.append((n, error))
        print k, n, error
    # Compute empirical convergence rates
    from math import log as ln
    estimator = lambda E1, E2, n1, n2: ln(E1/E2)/ln(float(n1)/n2)
    r = []
    for i in range(len(errors)-1):
        n1, E1 = errors[i]
        n2, E2 = errors[i+1]
        r.append(estimator(E1, E2, n1, n2))
    expected = -2
    computed = r[-1]  # The "most" asymptotic value
    error = abs(expected - computed)
    tol = 1E-3
    msg = 'Convergence rates: %s' % r
    print errors
    assert error < tol, msg
    print r

if __name__ == '__main__':
    test_linear()
    test_linear_symbolic()
    test_linear_symbolic_large_limits()
    test_convergence_rate()
