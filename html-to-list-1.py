# html-to-list-1.py

import urllib2
import dh

url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'

response = urllib2.urlopen(url)
html = response.read()
text = dh.stripTags(html)
wordlist = text.split()
print wordlist[0:120]
