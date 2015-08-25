#!/bin/sh
name=programmering
doconce format pdflatex $name --latex_code_style=lst-yellow2
pdflatex $name
pdflatex $name

doconce format ipynb $name
