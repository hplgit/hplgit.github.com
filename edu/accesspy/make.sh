#!/bin/sh
dir=~/vc/primer4/doc/src/chapters/tech
name=accesspy
cp -r $dir/${name}*.html $dir/._${name}*.html $dir/fig-${name} .
cp $dir/main_${name}.pdf ${name}.pdf
rm -rf ${name}_blog*
