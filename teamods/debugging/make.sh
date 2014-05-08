#!/bin/sh
# Copy documents from development repo
name=debug
wrap=main_${name}
repo=$HOME/vc/primer4/doc/src/chapters/debug

rm -rf html *.html *.pdf
#cp -r $repo/sphinx-rootdir/_build/html .
#cp -r $repo/sphinx-rootdir-extended/_build/html html-githg
cp $repo/$wrap.pdf $name.pdf
#cp $repo/${wrap}_4print.pdf ${name}_4print.pdf
cp $repo/${name}.html $repo/._${name}*.html .
#cp $repo/${wrap}-solarized.html ${name}-solarized.html
git add .
git commit -am 'New updates (copies)'
