"""
Example for illustrating how Sphinx can be used to create
API documentation for Python modules.

This module is minimalistic - se module :mod:`quadratic` for a
better examples on how to write doc strings.
"""

__all__ = ['root', 'Linear', 'Line']

def root(a, b):
    """Return the root ``x`` of the equation ``a*x + b``."""
    return -b/float(a)

class Linear:
    """
    Class for representing linear functions :math:`ax^2+b`.

    >>> line = Linear(a=1, b=-2)
    >>> line.value(4)
    2.0
    >>> line.root()
    2.0
    >>> print line
    1.0*x - 2.0
    """
    def __init__(self, a, b):
        """
        `a` and `b` are coefficients in the linear
        function :math:`ax^2+b`.
        """
        self.a, self.b = float(a), float(b)

    def root(self):
        """Return the root of the linear function."""
        return - self.b/self.a

    def value(self, x):
        """Return value of linear function at `x`."""
        return self.a*x + self.b

    def __call__(self, x):
        """Return value of linear function at `x`."""
        return self.value(x)

    def __str__(self):
        import quadratic
        return '%s*x %s %s' % (self.a, quadratic._sign(self.b), abs(self.b))

class Line:
    """
    Compute the straight line that goes through two points p1 and p2.

    Example:

    >>> line = Line((1,0), (-4,1))
    >>> print line
    -0.2*x + 0.2
    >>> line.value(1)
    0.0
    >>> line.value(-4)
    1.0
    """
    def __init__(self, p1, p2):
        """`p1` and `p2` are two points (2-tuple/list)."""
        x0, y0 = p1
        x1, y1 = p2
        # be careful with potential integer division:
        a = float(y1-y0)/(x1-x0)
        b = y0 - a*x0
        self.line = Linear(a, b)

    def value(self, x):
        """Return the value of the line at `x`."""
        return self.line.value(x)

    def __str__(self):
        return str(self.line)

if __name__ == '__main__':
    line = Line((0,-1), (2,4))
    print line.a, line.b
    print line.value(0.5), line.value(0), line.value(1)

