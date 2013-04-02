#!/bin/sh
# Copy documents from development repo
name=bitgit
wrap=main_${name}
repo=$HOME/vc/teamods/doc/src/$name

rm -rf html *.html *.pdf
cp -r $repo/sphinx-rootdir/_build/html .
cp $repo/$wrap.pdf Langtangen_$name.pdf
cp $repo/$wrap.html $name.html
git commit -am 'New updates (copies)'
