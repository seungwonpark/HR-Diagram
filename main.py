import os
if not os.path.exists('data/'):
	os.makedirs('data/')
if not os.path.exists('diagrams/'):
	os.makedirs('diagrams/')

from explorer import grid_search
from plotter import plot_HR

import configparser
config = configparser.ConfigParser()
config.read('ClusterInfo.ini')

clustername = str(config['name']['clustername'])
ra_0 = float(config['start']['ra'])
dec_0 = float(config['start']['dec'])
ra_1 = float(config['end']['ra'])
dec_1 = float(config['end']['dec'])
interval = float(config['config']['interval'])
threshold = float(config['config']['threshold'])


print('Collecting star information...')
datafilename = grid_search(ra_0, ra_1, dec_0, dec_1, interval)

print('Plotting H-R diagram...')
plotfilename = plot_HR(datafilename, clustername,threshold)
print('Plot saved to %s' % (plotfilename))
