import numpy as np
import matplotlib.pyplot as plt

filename = 'result/114.543-114.665-21.526-21.641-0.02.csv'
clustername = 'NGC2420'
g_r = []
r = []

plt.xlabel('r')
plt.ylabel('g - r')
plt.title('H-R diagram of %s' % clustername)
plt.annotate('Plot by Seungwon Park, Data by SDSS', xy=(0.02, 0.04), xycoords='axes fraction')

with open(filename, 'r') as f:
	next(f) # skip first line
	for line in f.readlines():
		data = str(line)[:-1].split(', ')
		g_r.append(float(data[-4]) - float(data[-3]))
		r.append(float(data[-3]))

	G_R = np.array(g_r)
	R = np.array(r)

	plt.plot(G_R, R, 'ko')
	plt.show()
