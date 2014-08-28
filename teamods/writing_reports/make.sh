#!/bin/sh
source=~/vc/deqbook/doc/src/chapters/archive/decay-reports
cp -r $source/* $source/.publish*.bib .
git add .
# git ignores temp*
git add -f _static/temp*

# update wiki with mediawiki
cp -r $source/_static/report.mwiki ~/vc/hplgit.github.com.wiki/Experiments-with-Schemes-for-Exponential-Decay.mediawiki
cp -r $source/_static/*.png ~/vc/hplgit.github.com.wiki/
