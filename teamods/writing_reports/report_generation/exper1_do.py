#!/usr/bin/env python
import os, sys, glob
import exper1

I = 1; a = 2; T = 5
exper1.run_experiments(I=I, a=a, T=T)

# Write Doconce report
do = open('tmp_report.do.txt', 'w')
title = 'Experiments with Schemes for Exponential Decay'
author1 = 'Hans Petter Langtangen {copyright|CC BY} Email:hpl@simula.no at '\
          'Center for Biomedical Computing, Simula Research Laboratory & '\
          'Department of Informatics, University of Oslo.'
date = 'today'

dt_values_str = ', '.join(sys.argv[1:])  # needed in report

# Remember to use raw string because of latex commands for math
do.write(r"""
TITLE: %(title)s
AUTHOR: %(author1)s
DATE: %(date)s

__Summary.__
This report investigates the accuracy of three finite difference
schemes for the ordinary differential equation $u'=-au$ with the
aid of numerical experiments. Numerical artifacts are in particular
demonstrated.

## Include table of contents (latex and html; sphinx always has a toc).
## (Lines starting with ## are not propagated to the output file,
## otherwise comments lines starting with # are visible in the
## output file.)

TOC: on


======= Mathematical problem =======
label{math:problem}

## Purpose: section with multi-line equation.
## idx{keyword} adds keyword to the index
## (to be place before the actual paragraph).

idx{model problem} idx{exponential decay}

We address the initial-value problem

!bt
\begin{align}
u'(t) &= -au(t), \quad t \in (0,T], label{ode}\\
u(0)  &= I,                         label{initial:value}
\end{align}
!et
where $a$, $I$, and $T$ are prescribed parameters, and $u(t)$ is
the unknown function to be estimated. This mathematical model
is relevant for physical phenomena featuring exponential decay
in time, e.g., vertical pressure variation in the atmosphere,
cooling of an object, and radioactive decay.

======= Numerical solution method =======
label{numerical:problem}

## Purpose: section with single-line equation, equation reference,
## a bullet list, and links to URLs ("link text": "url").

idx{mesh in time} idx{$\theta$-rule} idx{numerical scheme}
idx{finite difference scheme}

We introduce a mesh in time with points $0 = t_0 < t_1 \cdots < t_{N_t}=T$.
For simplicity, we assume constant spacing $\Delta t$ between the
mesh points: $\Delta t = t_{n}-t_{n-1}$, $n=1,\ldots,N_t$. Let
$u^n$ be the numerical approximation to the exact solution at $t_n$.

The $\theta$-rule cite{Iserles_2009}
is used to solve (ref{ode}) numerically:

!bt
\[
u^{n+1} = \frac{1 - (1-\theta) a\Delta t}{1 + \theta a\Delta t}u^n,
\]
!et
for $n=0,1,\ldots,N_t-1$. This scheme corresponds to

  * The "Forward Euler":
    "http://en.wikipedia.org/wiki/Forward_Euler_method"
    scheme when $\theta=0$
  * The "Backward Euler":
    "http://en.wikipedia.org/wiki/Backward_Euler_method"
    scheme when $\theta=1$
  * The "Crank-Nicolson":
    "http://en.wikipedia.org/wiki/Crank-Nicolson"
    scheme when $\theta=1/2$


======= Implementation =======

## Purpose: section with computer code taken from a part of
## a file. The fromto: f@t syntax copies from the regular
## expression f up to the line, but not including, the regular
## expression t.

!bc pyhid
from numpy import zeros, linspace
!ec

The numerical method is implemented in a Python function
cite{Langtangen_2014} `solver` (found in the "`model.py`":
"http://bit.ly/29ayDx3" Python module file):

@@@CODE ../model.py  fromto: def solver@def u_exact


======= Numerical experiments =======

## Purpose: section with figures.

idx{numerical experiments}

A set of numerical experiments has been carried out,
where $I$, $a$, and $T$ are fixed, while $\Delta t$ and
$\theta$ are varied. In particular, $I=%(I)g$, $a=%(a)g$,
$\Delta t = %(dt_values_str)s$.
Figure ref{fig:BE} contains four plots, corresponding to
four decreasing $\Delta t$ values. The red dashed line
represent the numerical solution computed by the Backward
Euler scheme, while the blue line is the exact solution.
The corresponding results for the Crank-Nicolson and
Forward Euler methods appear in Figures ref{fig:CN}
and ref{fig:FE}.

""" % vars())

short2long = dict(FE='Forward Euler method',
                  BE='Backward Euler method',
                  CN='Crank-Nicolson method')
methods = 'BE', 'CN', 'FE'
for method in methods:
    do.write("""

idx{%s}

FIGURE: [%s, width=800] The %s for decreasing time step values. label{fig:%s}

""" % (short2long[method], method, short2long[method], method))

# Remember raw string for latex math with backslashes
do.write(r"""

======= Error vs $\Delta t$ =======

idx{error vs time step}

How the error

!bt
\[ E^n = \left(\int_0^T (Ie^{-at} - u^n)^2dt\right)^{\frac{1}{2}}\]
!et
varies with $\Delta t$ for the three numerical methods
is shown in Figure ref{fig:error}.

## Here is an admonition box for warnings

!bwarning Observe:
The data points for the three largest $\Delta t$ values in the
Forward Euler method are not relevant as the solution behaves
non-physically.
!ewarning

FIGURE: [error, width=400] Variation of the error with the time step. label{fig:error}

## A corresponding table

The $E$ numbers corresponding to Figure ref{fig:error}
are given in the table below.

|------c--------------c--------------c--------------c-------|
| $\Delta t$   | $\theta=0$   | $\theta=0.5$ | $\theta=1$   |
|------r--------------r--------------r--------------r-------|
| 1.25         | 7.4630       | 0.2161       | 0.2440       |
| 0.75         | 0.6632       | 0.0744       | 0.1875       |
| 0.50         | 0.2797       | 0.0315       | 0.1397       |
| 0.10         | 0.0377       | 0.0012       | 0.0335       |
|-----------------------------------------------------------|

## Here is an admonition box for summaries

!bsummary
 o $\theta =1$: $E\sim \Delta t$ (first-order convergence).
 o $\theta =0.5$: $E\sim \Delta t^2$ (second-order convergence).
 o $\theta =1$ is always stable and gives qualitatively corrects results.
 o $\theta =0.5$ never blows up, but may give oscillating solutions
   if $\Delta t$ is not sufficiently small.
 o $\theta =0$ suffers from fast-growing solution if $\Delta t$ is
   not small enough, but even below this limit one can have oscillating
   solutions (unless $\Delta t$ is sufficiently small).
!esummary

======= Bibliography =======

## Publish (https://bitbucket.org/logg/publish is used to
## handle references. The line below specifies the name of
## the Publish database file (see the doconce manual for details).

BIBFILE: .publish_references.pub
""")

# Good habits when writing for latex, sphinx and mathjax-html
# at once:
#
# Minimize math in captions as the caption becomes the figure
# name in sphinx, when referring to figures, and any math
# is deleted in the name.
#
# Use \[, equation or align enviroments in latex math.
# Sphinx cannot handle labels in align environments.
#
# Figures float around in latex, but are placed at where
# they are defined in sphinx and html. Figures without captions
# are placed inline in latex and may be convenient.
#
# Remember raw strings for any text with latex math with
# backslashes.
