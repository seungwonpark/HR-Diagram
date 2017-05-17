from crawler import crawl_url

ra_0 = 114.543
dec_0 = 21.641
ra_1 = 114.665
dec_1 = 21.526

#interval = 0.001
interval = 0.02
threshold = 18 # if object is darker than threshold, then skip.

ra_0, ra_1 = sorted([ra_0, ra_1])
dec_0, dec_1 = sorted([dec_0, dec_1])

ra_length = int((ra_1 - ra_0) // interval)
dec_length = int((dec_1 - dec_0) // interval)

filename = 'result/%g-%g-%g-%g-%g.csv' % (ra_0, ra_1, dec_0, dec_1, interval)

f = open(filename, 'w')
f.write('ObjectNo, ra, dec, type, u, g, r, i, z\n')

ObjectList = []

for ra_i in range(ra_length):
	for dec_i in range(dec_length):
		ra = ra_0 + interval * ra_i
		dec = dec_0 + interval * dec_i
		print(ra, dec)

		data = crawl_url(ra, dec, 0.5)
		if(data == 0):
			continue
		else:
			if(float(data[-3]) < threshold and data[3] == 'STAR'):
				if(data[0] not in ObjectList): # to avoid duplication
					ObjectList.append(data[0])
					f.write(", ".join(data) + "\n")
