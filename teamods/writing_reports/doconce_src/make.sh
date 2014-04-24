#!/bin/sh
# Simple bash script for compiling report.do.txt to various formats

# Do all compilations in ../tmp scratch directory
cd ..
rm -rf tmp
cp -r doconce_src tmp
cd tmp

# Spell check with custom dictionary .dict4spell.txt
doconce spellcheck -d .dict4spell.txt report.do.txt

# Plain doconce html bloodish
doconce format html report --html_style=bloodish
if [ $? -ne 0 ]; then failures="$failures:doconce-html"; fi
mv -f report.html report_bloodish.html

# Sphinx
doconce sphinx_dir theme=pyramid report
python automake_sphinx.py

# PDF for screen viewing with an alternative look from classic LaTeX
doconce format pdflatex report --latex_font=helvetica --latex_admon=yellowbox '--latex_admon_color=yellow!5' --latex_fancy_header --latex_title_layout=std --latex_section_headings=blue --latex_colored_table_rows=blue
# Substitute abstract envir with quote and \small font
doconce replace 'begin{abstract}' 'begin{quote}\small' report.p.tex
doconce replace 'end{abstract}' 'end{quote}\small' report.p.tex
doconce replace '[compact]{titlesec}' '[]{titlesec}' report.p.tex

rm -f *.aux
pdflatex -shell-escape report
bibtex report
pdflatex -shell-escape report
pdflatex -shell-escape report

# PDF for printing
doconce format pdflatex report --device=paper --latex_font=palatino --latex_title_layout=titlepage --latex_admon=graybox1
doconce ptex2tex report envir=minted

rm -f *.aux
pdflatex -shell-escape report
bibtex report
pdflatex -shell-escape report
pdflatex -shell-escape report
cp report.pdf report_4printing.pdf

# Plain doconce html bloodish with handwriting font Architects+Daughter
doconce format html report --html_style=bloodish --html_body_font=Architects+Daughter --html_heading_font=Architects+Daughter
if [ $? -ne 0 ]; then failures="$failures:doconce-html"; fi
mv -f report.html report_bloodish_Architects_Daughter.html

# Solarized doconce html
doconce format html report --html_style=solarized --html_admon=apricot
if [ $? -ne 0 ]; then failures="$failures:doconce-html-solarized"; exit 1; fi
mv -f report.html report_solarized.html

# blogger.com (Google) blog
cp report.do.txt report2.do.txt
# Remove title, author and date
doconce subst -m '^TITLE:.+$' '' report2.do.txt
doconce subst -m '^AUTHOR:.+$' '' report2.do.txt
doconce subst -m '^DATE:.+$' '' report2.do.txt
# Figures must have URLs to where they are stored on the web
for figname in BE FE CN error; do
  doconce replace "[$figname," "[https://raw.github.com/hplgit/hplgit.github.com/master/teamods/writing_reports/_static/$figname.png," report2.do.txt
done
doconce format html report2
mv -f report2.html report_blogger.html
# Paste report_blogger.html text into a new blog on your Google account

# Wordpress blog
doconce format html report2 --wordpress
mv -f report2.html report_wordpress.html

# IPython notebook
doconce format ipynb report


