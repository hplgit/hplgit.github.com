#!/bin/sh
# Copy documents from development repo
name=bitgit
wrap=main_${name}
repo=$HOME/vc/teamods/doc/src/$name

rm -rf html *.html *.pdf
cp -r $repo/sphinx-rootdir/_build/html .
cp -r $repo/sphinx-rootdir-extended/_build/html html-githg
cp $repo/$wrap.pdf Langtangen_$name.pdf
cp $repo/${wrap}_4print.pdf Langtangen_${name}_4print.pdf
cp $repo/${wrap}.html $name.html
cp $repo/${wrap}-solarized.html ${name}-solarized.html
git commit -am 'New updates (copies)'
