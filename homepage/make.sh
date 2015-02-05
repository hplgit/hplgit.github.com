#!/bin/sh
files="index bio research education software contact books"
for file in $files; do
doconce format html $file --html_style=solarized --html_template=template_solarized_box_yellow.html
done
