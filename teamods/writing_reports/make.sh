#!/bin/sh
root=../../../decay-book/doc/.src/chapters
script_source=$root/softeng/report_generation
report_source=$root/archive/decay-reports
cp -r ${report_source}/* .
cp -r ${script_source} .
cd report_generation
sh clean.sh
cd ..
rm -rf _minted-report
git add .
# git ignores temp*
git add -f _static/temp*

# update wiki with mediawiki
cp -r _static/report.mwiki ~/vc/hplgit.github.com.wiki/Experiments-with-Schemes-for-Exponential-Decay.mediawiki
cp -r _static/*.png ~/vc/hplgit.github.com.wiki/
