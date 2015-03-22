#!/bin/sh
script_source=~/vc/deqbook/doc/src/chapters/softeng1/report_generation
report_source=~/vc/deqbook/doc/src/chapters/archive/decay-reports
cp -r ${report_source}/* .
cp -r ${script_source} .
git add .
# git ignores temp*
git add -f _static/temp*

# update wiki with mediawiki
cp -r $source/_static/report.mwiki ~/vc/hplgit.github.com.wiki/Experiments-with-Schemes-for-Exponential-Decay.mediawiki
cp -r $source/_static/*.png ~/vc/hplgit.github.com.wiki/
