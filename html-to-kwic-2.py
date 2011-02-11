# html-to-kwic-2.py

import dh

# create dictionary of n-grams
n = 7
url = 'file:///C:/Documents%20and%20Settings/HP_Administrator/Desktop/ProgrammingHistorian/dcb-34298.html'
# url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'
text = dh.webPageToText(url)
fullwordlist = ('# ' * (n//2)).split()
fullwordlist += dh.stripNonAlphaNum(text)
fullwordlist += ('# ' * (n//2)).split()
ngrams = dh.getNGrams(fullwordlist, n)
worddict = dh.nGramsToKWICDict(ngrams)

# output KWIC and wrap with HTML
target = 'iroquois'
outstr = '<pre>'
if worddict.has_key(target):
    for k in worddict[target]:
        linkname = dh.prettyPrintKWIC(k)
        keywords = dh.removeStopwords(k, dh.stopwords)
        outstr += dh.keywordListToGoogleSearchLink(keywords, linkname)
        # outstr += '<br />'
else:
    outstr += 'Keyword not found in source'
outstr += '</pre>'
dh.wrapStringInHTML('html-to-kwic-2', url, outstr)