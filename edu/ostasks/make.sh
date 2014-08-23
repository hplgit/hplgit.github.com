#!/bin/sh
dir=~/vc/primer4/doc/src/chapters/tech
name=ostasks
cp -r $dir/${name}*.html $dir/._${name}*.html .
cp $dir/main_${name}.pdf ${name}.pdf
