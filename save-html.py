# save-html.py

import urllib2

url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'

response = urllib2.urlopen(url)
html = response.read()

f = open('dcb-34298.html', 'w')
f.write(html)
f.close