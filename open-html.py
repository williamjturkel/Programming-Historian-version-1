# open-html.py

import urllib2

url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'

response = urllib2.urlopen(url)
html = response.read()

print html[0:300]

print type(html)