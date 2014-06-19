#!/bin/sh
dir=~/vc/primer4/doc/src/chapters/tech
cp -r $dir/accesspy*.html $dir/._accesspy*.html $dir/fig-accesspy .
rm -rf accesspy_blog*
