# html-to-freq-4.py

import dh

# create sorted dictionary of word-frequency pairs
url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'
# url = 'file:///C:/Documents%20and%20Settings/HP_Administrator/Desktop/ProgrammingHistorian/dcb-34298.html'
text = dh.webPageToText(url)
fullwordlist = dh.stripNonAlphaNum(text)
wordlist = dh.removeStopwords(fullwordlist, dh.stopwords)
dictionary = dh.wordListToFreqDict(wordlist)
sorteddict = dh.sortFreqDict(dictionary)

# create Google search link
keywords = []
for k in sorteddict[0:5]:
    keywords.append(str(k[1]))
gsearch = dh.keywordListToGoogleSearchLink(keywords, 'Google Search n=5')

# compile dictionary into string and wrap with HTML
outstring = gsearch + "<br /><br />"
for s in sorteddict:
    outstring += str(s)
    outstring += "<br />"
dh.wrapStringInHTML("html-to-freq-4", url, outstring)
