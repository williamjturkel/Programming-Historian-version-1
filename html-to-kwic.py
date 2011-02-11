# html-to-kwic.py

import dh

# create dictionary of n-grams
n = 7

# NB Local copy; clean this up!
url = 'file:///C:/Documents%20and%20Settings/HP_Administrator/Desktop/ProgrammingHistorian/dcb-34298.html'

# url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'
text = dh.webPageToText(url)
fullwordlist = ('# ' * (n//2)).split()
fullwordlist += dh.stripNonAlphaNum(text)
fullwordlist += ('# ' * (n//2)).split()
ngrams = dh.getNGrams(fullwordlist, n)
worddict = dh.nGramsToKWICDict(ngrams)

# output KWIC and wrap with HTML
target = 'dictionary'
outstr = '<pre>'
if worddict.has_key(target):
    for k in worddict[target]:
        outstr += dh.prettyPrintKWIC(k)
        outstr += '<br />'
else:
    outstr += 'Keyword not found in source'
outstr += '</pre>'
dh.wrapStringInHTML('html-to-kwic', url, outstr)