name=mn_strategy
doconce format html $name
doconce replace '<title>Forskning _OG_ utdanning</title>' '<title>Forskning OG utdanning</title>' $name.html
doconce slides_html $name.html reveal --html_slide_theme=simple #beige # --html_footer_logo=uio_symbol
