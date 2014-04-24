#!/bin/sh
# Run experiment documented in reports

python decay_exper1_do.py 1.25 0.75 0.5 0.1

# ----- Make reports -----

# Make publish database for bibliography (from BibTeX file refs.bib)
publish import refs

# HTML
file=tmp_report
doconce format html template_vagrant.html
mv -f template_vagrant.html.html report_do.html

# LaTeX
doconce format pdflatex template_vagrant.html
doconce ptex2tex template_vagrant.html envir=minted
pdflatex -shell-escape template_vagrant.html
pdflatex -shell-escape template_vagrant.html
mv -f template_vagrant.html.pdf report.pdf

# Sphinx
doconce sphinx_dir theme=pyramid report
cp *.png sphinx-rootdir
python automake_sphinx.py

