name=mn_strategy
doconce format html $name
doconce replace '<title>Forskning _OG_ undervisning</title>' '<title>Forskning OG undervisning</title>' $name.html
doconce slides_html $name.html reveal --html_slide_theme=beige # --html_footer_logo=uio_symbol
