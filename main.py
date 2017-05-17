import os
if not os.path.exists('data/'):
	os.makedirs('data/')
if not os.path.exists('diagrams/'):
	os.makedirs('diagrams/')

from explorer import grid_search
from plotter import plot_HR

ra_0 = 132.975
dec_0 = 11.739
ra_1 = 132.775
dec_1 = 11.905
interval = 0.005
threshold = 17

clustername = 'M67'

print('Collecting star information...')
datafilename = grid_search(ra_0, ra_1, dec_0, dec_1, interval)

print('Plotting H-R diagram...')
plotfilename = plot_HR(datafilename, clustername,threshold)
print('Plot saved to %s' % (plotfilename))
