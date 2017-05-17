from crawler import crawl_url

def grid_search(ra_0, ra_1, dec_0, dec_1, interval):
	ra_0, ra_1 = sorted([ra_0, ra_1])
	dec_0, dec_1 = sorted([dec_0, dec_1])

	ra_length = int((ra_1 - ra_0) // interval)
	dec_length = int((dec_1 - dec_0) // interval)

	datafilename = 'data/%g-%g-%g-%g-%g.csv' % (ra_0, ra_1, dec_0, dec_1, interval)

	f = open(datafilename, 'w')
	f.write('ObjectNo, ra, dec, type, u, g, r, i, z\n')

	ObjectList = []
	num = ra_length * dec_length

	print('Started crawling %d spots...' % (num))
	for ra_i in range(ra_length):
		for dec_i in range(dec_length):
			ra = ra_0 + interval * ra_i
			dec = dec_0 + interval * dec_i
			data = crawl_url(ra, dec, 0.5)
			if(data == 0):
				continue
			else:
				if(data[3] == 'STAR'):
					if(data[0] not in ObjectList): # to avoid duplication
						ObjectList.append(data[0])
						f.write(", ".join(data) + "\n")

			x = 1 + dec_i + ra_i * dec_length
			if(x % 10 == 0):
				print('Crawled %d out of %d spots' % (x, num))

	print('Done!')

	return datafilename
