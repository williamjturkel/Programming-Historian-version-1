# html-to-list-2.py

import urllib2
import dh

url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'

response = urllib2.urlopen(url)
html = response.read()
text = dh.stripTags(html).replace('&nbsp;', ' ')
wordlist = dh.stripNonAlphaNum(text.lower())
print wordlist[0:500]