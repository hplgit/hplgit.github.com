#!/bin/sh
#source=~/vc/deqbook/doc/src/decay/src-decay/experiments/archived-reports/
source=~/vc/deqbook/doc/src/archive/decay-reports
cp -r $source/* $source/.publish*.bib .

# update wiki with mediawiki
cp -r $source/_static/report.mwiki ~/vc/hplgit.github.com.wiki/Experiments-with-Schemes-for-Exponential-Decay.mediawiki
cp -r $source/_static/*.png ~/vc/hplgit.github.com.wiki/