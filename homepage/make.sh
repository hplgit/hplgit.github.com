#!/bin/sh
files="index bio research education software contact books book_comparison"
for file in $files; do
doconce format html $file --html_style=solarized --html_template=template_solarized_box_yellow.html
done
