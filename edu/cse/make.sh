#!/bin/bash
name=cse

function system {
 "$@"
 if [ $? -ne 0 ]; then echo "abort!"; exit 1; fi
}

# First make handouts of beamer
system doconce format pdflatex $name -DTEXT_HEADING
system doconce ptex2tex $name -DLATEX_HEADING=beamer envir=minted
system doconce slides_beamer $name --beamer_slide_theme=red2 --handout
system pdflatex -shell-escape $name
system pdfnup --nup 2x3 --frame true --delta "1cm 1cm" --scale 0.9 $name.pdf
# Generate real slides
system doconce format pdflatex $name -DTEXT_HEADING
system doconce ptex2tex $name -DLATEX_HEADING=beamer envir=minted
system doconce slides_beamer $name --beamer_slide_theme=red2
system pdflatex -shell-escape $name

doconce format html $name -DNOTES
cp cse.html ${name}_plain.html
doconce subst 'border:.+px' 'border: 5px' ${name}_plain.html
doconce replace 'width: 75%;' 'width: 50%;' ${name}_plain.html
doconce replace 'font-size: 90%;' 'font-size: 100%;' ${name}_plain.html
doconce replace 'border-radius: 4px' 'border-radius: 14px' ${name}_plain.html

system doconce format html $name --pygments_html_style=monokai --keep_pygments_html_bg -DTEXT_HEADING
#system doconce format html $name --pygments_html_style=native
cp $name.html ${name}_reveal.html
system doconce slides_html ${name}_reveal reveal --html_slide_theme=darkgray

system doconce format html $name --pygments_html_style=perldoc --keep_pygments_html_bg
#doconce format html $name --pygments_html_style=native
cp $name.html ${name}_deck.html
system doconce slides_html ${name}_deck deck --html_slide_theme=sandstone.default

scp_rsync_del='rsync -rtDvz -u -e ssh -b --exclude-from=/Users/hpl/1/.rsyncexclude --suffix=.rsync~ --delete --force '
$scp_rsync_del * $fb2:www_docs/tmp/CSE/

