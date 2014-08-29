doconce format html index --html_style=bootswatch_readable --html_bootstrap_jumbotron=off --html_bootstrap_navbar=off
# Add more space before list (no sublist looks strange!)
#doconce replace '<ul>' '<p>&nbsp;&nbsp;<p><ul>' index.html
rm -f .*html_file_collection
