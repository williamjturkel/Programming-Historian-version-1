# html-to-tag-cloud.py

import dh

# create sorted dictionary of word-frequency pairs
# url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'
url = 'file:///C:/Documents%20and%20Settings/HP_Administrator/Desktop/ProgrammingHistorian/dcb-34298.html'
text = dh.webPageToText(url)
fullwordlist = dh.stripNonAlphaNum(text)
wordlist = dh.removeStopwords(fullwordlist, dh.stopwords)
dictionary = dh.wordListToFreqDict(wordlist)
sorteddict = dh.sortFreqDict(dictionary)

# create tag cloud and open in Firefox
cloudsize = 100
maxfreq = sorteddict[0][0]
minfreq = sorteddict[cloudsize][0]
freqrange = maxfreq - minfreq
outstring = ''
resorteddict = dh.reSortFreqDictAlpha(sorteddict[:cloudsize])
for k in resorteddict:
    kfreq = k[0]
    klabel = k[1]
    scalingfactor = (kfreq - minfreq) / float(freqrange)
    outstring += ' ' + dh.scaledFontHeatmapSpan(klabel, scalingfactor) + ' '
dh.wrapStringInHTML("html-to-tag-cloud", url, dh.defaultCSSDiv(outstring))
    