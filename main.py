import os
if not os.path.exists('data/'):
	os.makedirs('data/')
if not os.path.exists('diagrams/'):
	os.makedirs('diagrams/')

from explorer import grid_search
from plotter import plot_HR


ra_0 = 114.543
dec_0 = 21.641
ra_1 = 114.665
dec_1 = 21.526
interval = 0.02

clustername = 'NGC2420'

print('Collecting star information...')
datafilename = grid_search(ra_0, ra_1, dec_0, dec_1, interval)

print('Plotting H-R diagram...')
plotfilename = plot_HR(datafilename, clustername)
print('Plot saved to %s' % (plotfilename))
