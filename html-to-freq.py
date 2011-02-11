# html-to-freq-2.py

import urllib2
import dh

url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'

response = urllib2.urlopen(url)
html = response.read()
text = dh.stripTags(html).replace('&nbsp;', ' ')
fullwordlist = dh.stripNonAlphaNum(text.lower())
wordlist = dh.removeStopwords(fullwordlist, dh.stopwords)
dictionary = dh.wordListToFreqDict(wordlist)
sorteddict = dh.sortFreqDict(dictionary)
for s in sorteddict: print str(s)