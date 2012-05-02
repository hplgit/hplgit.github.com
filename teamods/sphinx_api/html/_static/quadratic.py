"""
This is an example on how to document Python modules using doc
strings and the sphinx tool. The doc strings can make use of
the reStructuredText format, see
`<http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_.
It is recommended to document Python modules according to
the `rules <https://github.com/numpy/numpy/blob/master/doc/example.py>`_
of the ``numpy`` package. See also
`A Guide to NumPy/SciPy Documentation <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`_.

"""
__all__ = ['roots', 'Quadratic', 'Cubic']

from numpy.lib.scimath import sqrt  # handles real and complex args

def roots(a, b, c, verbose=False):
    """
    Return the two roots in the quadratic equation::

      a*x**2 + b*x + c = 0

    or written with math typesetting

    .. math:: ax^2 + bx + c = 0

    The returned roots are real or complex numbers,
    depending on the values of the arguments `a`, `b`,
    and `c`.

    Parameters
    ----------
    a: int, real, complex
       coefficient of the quadratic term
    b: int, real, complex
       coefficient of the linear term
    c: int, real, complex
       coefficient of the constant term
    verbose: bool, optional
       prints the quantity ``b**2 - 4*a*c`` and if the
       roots are real or complex

    Returns
    -------
    root1, root2: real, complex
        the roots of the quadratic polynomial.

    Raises
    ------
    ValueError:
        when `a` is zero

    See Also
    --------
    :class:`Quadratic`: which is a class for quadratic polynomials
        that also has a :func:`Quadratic.roots` method for computing
        the roots of a quadratic polynomial. There is also a class
        :class:`linear.Linear` in the module :mod:`linear`
        (i.e., :class:`linear.Linear`).

    Notes
    -----
    The algorithm is a straightforward implementation of
    a very well known formula [1]_.

    References
    ----------
    .. [1] Any textbook on mathematics or
           `Wikipedia <http://en.wikipedia.org/wiki/Quadratic_equation>`_.

    Examples
    --------
    >>> roots(-1, 2, 10)
    (-5.3166247903553998, 1.3166247903553998)
    >>> roots(-1, 2, -10)
    ((-2-3j), (-2+3j))

    Alternatively, we can in a doc string list the arguments and
    return values in a table

    ==========   =============   ================================
    Parameter    Type            Description
    ==========   =============   ================================
    a            float/complex   coefficient for quadratic term
    b            float/complex   coefficient for linear term
    c            float/complex   coefficient for constant term
    r1, r2       float/complex   return: the two roots of
                                 the quadratic polynomial
    ==========   =============   ================================
    """
    if abs(a) < 1E-14:
        raise ValueError('a=%g is too close to zero' % a)

    q = b**2 - 4*a*c
    if verbose:
        print 'q=%g: %s roots' % (q, 'real' if q>0 else 'complex')

    root1 = -b + sqrt(q)/float(2*a)
    root2 = -b - sqrt(q)/float(2*a)
    return root1, root2

class Quadratic:
    """
    Representation of a quadratic polynomial:

    .. math::

       ax^2 + bx + c

    Example:

    >>> q = Quadratic(a=2, b=4, c=-16)
    >>> print q
    2*x**2 + 4*x - 16
    >>> r1, r2 = q.roots()
    >>> r1
    2.0
    >>> r2
    -4.0
    >>> q(r1), q(r2)  # check
    (0.0, 0.0)
    >>> repr(q)
    'Quadratic(a=2, b=4, c=-16)'
    """

    def __init__(self, a, b, c):
        """
        The arguments `a`, `b`, and `c` are coefficients in
        the quadratic polynomial::

          a*x**2 + b*x + c

        or

        .. math::

           ax^2 + bx + c

        ==========   =============   ================================
        Argument     Type            Description
        ==========   =============   ================================
        a            float/complex   coefficient for quadratic term
        b            float/complex   coefficient for linear term
        c            float/complex   coefficient for constant term
        ==========   =============   ================================

        Raises
        ------
        ValueError:
            When `a` is too close to zero.
        """
        self.a, self.b, self.c = a, b, c
        if abs(a) < 1E-14:
            raise ValueError('a=%g is too close to zero' % a)

    def __call__(self, x):
        return self.value(x)

    def value(self, x):
        """
        Return the value of the quadratic polynomial for `x`.

        Example:

        >>> q = Quadratic(a=2, b=4, c=-16)
        >>> print q
        2*x**2 + 4*x - 16
        >>> q(1)
        -10
        >>> q(-2.5)
        -13.5
        """
        return self.a*x**2 + self.b*x + self.c

    def roots(self):
        """
        Return the two roots of the quadratic polynomial.
        The roots are real or complex, depending on the
        coefficients in the polynomial.

        Let us define a quadratic polynomial:

        >>> q = Quadratic(a=2, b=4, c=-16)
        >>> print q
        2*x**2 + 4*x - 16

        The roots are then found by

        >>> r1, r2 = q.roots()
        >>> r1
        2.0
        >>> r2
        -4.0
        """
        a, b, c = self.a, self.b, self.c  # short names
        q = b**2 - 4*a*c
        root1 = (-b + sqrt(q))/float(2*a)
        root2 = (-b - sqrt(q))/float(2*a)
        return root1, root2


    def __str__(self):
        # no doc
        return '%s*x**2 %s %s*x %s %s' % \
               (self.a, _sign(self.b), abs(self.b),
                _sign(self.c), abs(self.c))

    def __repr__(self):
        return 'Quadratic(a=%s, b=%s, c=%s)' % \
               (self.a, self.b, self.c)

def _sign(v):
    """Return '+' if `v` >= 0, otherwise '-'."""
    return '+' if v >= 0 else '-'

class Cubic(Quadratic):
    """Evaluation of a cubic polynomial :math:`ax^3 + bx^2 + cx + d`."""
    def __init__(self, a, b, c, d):
        self.cubic = self.a
        Quadratic.__init__(self, b, c, d)

    def value(self, x):
        return Quadratic.value(self, x) + self.cubic*x**3

    def roots(self):
        raise NotImplementedError('roots for cubic polynomial not impl.')

    def __str__(self):
        return '%s*x**3 +' % (self.cubic) + Quadratic.__str__(self)
