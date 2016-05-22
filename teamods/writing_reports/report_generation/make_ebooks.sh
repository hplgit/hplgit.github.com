#!/bin/bash
# Run make_reports.sh first to make reports, then run this script as a
# post process for making ebook formats (ePub, Mobi).


rm -rf ebooks
mkdir ebooks
cd ebooks
cp ../reports/_static/report_4printing.pdf report.pdf
cp -r ../reports/_static/sphinx-uio .
cd sphinx-uio
mv -f index.html report.html
cp ../../report.json .
doconce replace '"source" : "._report*.html"' '"source" : "index.html"' report.json
python3 ~/vc/ebookmaker/ebookmaker.py report.json
# produces report.epub
mv -f report.epub report_sphinx.epub
cd ..

# Test calibre on PDF (does not work well)
ebook-convert report.pdf report_calibre.mobi
ebook-convert report.pdf report_calibre.epub
