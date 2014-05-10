#!/bin/sh
# Copy documents from development repo
name=bitgit
wrap=main_${name}
repo=$HOME/vc/teamods/doc/src/$name

rm -rf html *.html .*.html *.pdf
cp -r $repo/sphinx-rootdir/_build/html .
cp -r $repo/sphinx-rootdir-extended/_build/html html-githg
cp $repo/${wrap}*.pdf .
cp $repo/${wrap}*.html $repoo/._${wrap}*.html .
scitools rename $wrap Langtangen_$name *.pdf *.html .*.html
git add .
git commit -am 'New updates (copies)'
