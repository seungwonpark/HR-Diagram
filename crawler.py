import urllib.request
import re

baseurl = 'http://skyserver.sdss.org/dr7/sp/tools/chart/shownearest.asp'
# '?ra=114.59053567107003&dec=21.56293906666667&scale=0.39612&opt=&radius=0.2'

def coordinates_str(ra, dec, scale):
	return '?ra=%s&dec=%s&scale=%s' % (str(ra), str(dec), str(scale))

def crawl_url(ra, dec, scale):
	url = baseurl + coordinates_str(ra, dec, scale)
	f = urllib.request.urlopen(url)
	html = f.read().decode('utf-8')

	try:
		objectNo = re.findall(r"javascript:explore\('(.*)'\)", html)[0]
		m = re.findall(r"<td align='right' class='c'>(.*)<\/td>", html)
		return [objectNo] + m
	except:
		return 0
