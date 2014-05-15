from pylab import *

# make a square figure and axes
figure(1, figsize=(6,6))

# The slices will be ordered and plotted counter-clockwise.
labels = 'Problem formulation', 'Solution', 'Interpretation'
fracs = [15, 80, 5]
#explode=(0, 0.05, 0)
explode=(0, 0, 0)

pie(fracs, explode=explode, labels=labels,
                autopct='%d%%', shadow=False, startangle=90)
title('Classic teaching')
savefig('classic_teaching.png')
savefig('classic_teaching.pdf')

# make a square figure and axes
figure(2, figsize=(6,6))

labels = 'Problem formulation', 'Solution', 'Interpretation', 'Extra'
fracs = [25, 20, 20, 35]
explode=(0, 0, 0, 0.1)

pie(fracs, explode=explode, labels=labels,
                autopct='%d%%', shadow=False, startangle=80)
title('Computerized solution procedure')
savefig('computerized_teaching.png')
savefig('computerized_teaching.pdf')

show()
