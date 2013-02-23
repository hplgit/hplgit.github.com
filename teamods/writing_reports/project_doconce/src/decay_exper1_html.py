#!/usr/bin/env python
import os, sys, glob
import decay_exper1

decay_exper1.run_experiments()

# Write HTML report
html = open('tmp_report.html', 'w')
html.write('''
<html>
<head></head>
<body bgcolor="white">

<title>Numerical investigations</title>

<center><h1>Experiments with Schemes for Exponential Decay</h1></center>

<center><b>Hans Petter Langtangen</b></center>
<center><b>Simula Research Laboratory</b></center>
<center><b>University of Oslo</b></center>
<center><h4>August 20, 2012</h4></center>

<b>Summary.</b> This report investigates the accuracy of three
finite difference schemes for the ordinary differential equation
u'=-au with the aid of numerical experiments.  Numerical
artifacts are in particular demonstrated.

<h2>Mathematical problem</h2>

We address the initial-value problem u'(t)=-au(t),
for t in (0,T], and with initial condition u(0)=I.
Here, I, a, and T are prescribed parameters,
and u(t) is the unknown function to be estimated.
This mathematical model is relevant for physical
phenomena featuring exponential decay in time.

<h2>Numerical solution method</h2>

We use a mesh in time with equally spaced points.
The theta-rule is used to discretize the differential
equation. This scheme corresponds to

<ul>
  <li> The Forward Euler scheme when theta=0
  <li> The Backward Euler scheme when theta=1
  <li> The Crank-Nicolson scheme when theta=1/2
</ul>

<h2>Implementation</h2>

The numerical method is implemented in a Python function:
<pre>
def solver(I, a, T, dt, theta):
    """Solve u'=-a*u, u(0)=I, for t in (0,T] with steps of dt."""
    N = int(round(T/float(dt)))  # no of intervals
    u = zeros(N+1)
    t = linspace(0, T, N+1)

    u[0] = I
    for n in range(0, N):
        u[n+1] = (1 - (1-theta)*a*dt)/(1 + theta*dt*a)*u[n]
    return u, t
</pre>

<h2>Numerical experiments</h2>

We define a set of numerical experiments where I, a, and
T are fixed, while the time step and theta are varied.
In particular, I=%g, a=%g, dt=%s.

''' % (decay_exper1.I, decay_exper1.a, ', '.join(sys.argv[1:])))

short2long = dict(FE='The Forward Euler method',
                  BE='The Backward Euler method',
                  CN='The Crank-Nicolson method')
for method in 'BE', 'CN', 'FE':
    html.write('\n<h3>%s</h3>\n' % short2long[method])
    html.write('<img src="%s.png" width="800">\n\n' % method)
html.write("""

<h3>Error versus time discretization</h3>

How E varies with the time step, for the three discretization
methods, is shown below.
<p>
<img="error.png", width="400">

</body>
</html>
""")


