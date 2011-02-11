# html-to-tag-cloud-kwic.py

import dh

# create sorted dictionary of word-frequency pairs
# url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'
url = 'file:///C:/Documents%20and%20Settings/HP_Administrator/Desktop/ProgrammingHistorian/dcb-34298.html'
text = dh.webPageToText(url)
fullwordlist = dh.stripNonAlphaNum(text)
wordlist = dh.removeStopwords(fullwordlist, dh.stopwords)
dictionary = dh.wordListToFreqDict(wordlist)
sorteddict = dh.sortFreqDict(dictionary)

# create dictionary of n-grams
n = 7
paddinglist = ('# ' * (n//2))
fullwordlist[:0] = paddinglist
fullwordlist.extend(paddinglist)
ngrams = dh.getNGrams(fullwordlist, n)
worddict = dh.nGramsToKWICDict(ngrams)

# create tag cloud
cloudsize = 40
maxfreq = sorteddict[0][0]
minfreq = sorteddict[cloudsize][0]
freqrange = maxfreq - minfreq
tempstring = ''
resorteddict = dh.reSortFreqDictAlpha(sorteddict[:cloudsize])
for k in resorteddict:
    kfreq = k[0]
    klabel = dh.undecoratedHyperlink('#'+k[1], k[1])    
    scalingfactor = (kfreq - minfreq) / float(freqrange)
    tempstring += dh.scaledFontSizeSpan(klabel, scalingfactor)
outstring = dh.defaultCSSDiv(tempstring) + '<br />'

# create KWIC listings for each item
for k in resorteddict:
    klabel = k[1]
    tempstring = ''
    tempstring += '<a name=\"%s\">%s</a> ' % (klabel, klabel)
    tempstring += dh.undecoratedHyperlink('#', '[back]')
    outstring += dh.defaultCSSDiv(tempstring, opt='font-size : 24px;')
    outstring += '<p><pre>'
    for t in worddict[klabel]:
        outstring += dh.prettyPrintKWIC(t)
        outstring += '<br />'
    outstring += '</pre></p>'

# open in Firefox
dh.wrapStringInHTML("html-to-tag-cloud-kwic", url, outstring)
    
