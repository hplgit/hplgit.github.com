#!/bin/sh
dir=~/vc/teamods/doc/src/python/num_prog_guide
names="numerical_programming_guide computing_competence"
for name in $names; do
    cp $dir/$name.html $dir/._${name}*.html $dir/$name.pdf .
done
