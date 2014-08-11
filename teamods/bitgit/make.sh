#!/bin/sh
# Copy documents from development repo
name=bitgit
wrap=main_${name}
repo=$HOME/vc/teamods/doc/src/$name

rm -rf html *.html .*.html *.pdf
cp -r $repo/sphinx-rootdir/_build/html .
cp -r $repo/sphinx-rootdir-extended/_build/html html-githg
cp -r $repo/sphinx-rootdir-github/_build/html html-github
cp $repo/${wrap}*.pdf .
cp $repo/main_github*.pdf .
cp $repo/${wrap}*.html $repo/._${wrap}*.html .
cp $repo/main_github*.html $repo/._main_github*.html .
scitools rename $wrap Langtangen_$name *.pdf *.html .*.html
scitools rename main_github Langtangen_github *.pdf *.html .*.html
scitools replace $wrap Langtangen_$name *.html .*.html
scitools replace main_github Langtangen_github *.html .*.html
rm -f *~ .*~
git add .
git commit -am 'New updates (copies)'
