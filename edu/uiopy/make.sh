#!/bin/sh
dir=~/vc/teamods/doc/src/python/uiopy
cp -r $dir/uiopy.html $dir/._uiopy*.html $dir/uiopy.pdf $dir/uiopy.do.txt $dir/figs $dir/sphinx-* .
rm -rf sphinx-rootdir
