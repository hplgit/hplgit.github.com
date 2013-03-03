#!/bin/sh
# Run experiment documented in reports

python decay_exper1_do.py 1.25 0.75 0.5 0.1

# Make reports

# HTML
file=tmp_report
doconce format html report_md.html
mv report_md.html.html report_do.html

# LaTeX
doconce format pdflatex report_md.html
doconce ptex2tex report_md.html envir=minted
pdflatex -shell-escape report_md.html
pdflatex -shell-escape report_md.html
mv report_md.html.pdf report.pdf

# Sphinx
doconce sphinx_dir theme=pyramid report
cp *.png sphinx-rootdir
python automake_sphinx.py

