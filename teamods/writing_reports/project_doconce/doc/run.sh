#!/bin/sh
# Run experiment documented in reports

python decay_exper1_do.py 1.25 0.75 0.5 0.1

# Make reports

# HTML
file=tmp_report
doconce format html report_mathjax.html
mv report_mathjax.html.html report_do.html

# LaTeX
doconce format pdflatex report_mathjax.html
doconce ptex2tex report_mathjax.html envir=minted
pdflatex -shell-escape report_mathjax.html
pdflatex -shell-escape report_mathjax.html
mv report_mathjax.html.pdf report.pdf

# Sphinx
doconce sphinx_dir theme=pyramid report
cp *.png sphinx-rootdir
python automake_sphinx.py

