import numpy as np
import matplotlib.pyplot as plt

g_r = []
r = []
plt.xlabel('r')
plt.ylabel('g - r')
plt.annotate('Plot by Seungwon Park, Data by SDSS', xy=(0.02, 0.04), xycoords='axes fraction')

def plot_HR(datafilename, clustername, threshold):

	plt.title('H-R diagram of %s' % clustername)
	with open(datafilename, 'r') as f:
		next(f) # skip first line
		for line in f.readlines():
			data = str(line)[:-1].split(', ')
			if(float(data[-3]) < threshold):
				g_r.append(float(data[-4]) - float(data[-3]))
				r.append(float(data[-3]))

		G_R = np.array(g_r)
		R = np.array(r)

		plt.plot(G_R, R, 'ko')
		plotfilename = 'diagrams/%s_%g_%s.pdf' % (clustername, threshold, datafilename[:-4].split('/')[1])
		plt.savefig(plotfilename, format='pdf')
	return plotfilename
