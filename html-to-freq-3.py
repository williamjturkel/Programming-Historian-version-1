# html-to-freq-3.py
 
import dh

# create sorted dictionary of word-frequency pairs
url = 'http://www.biographi.ca/EN/ShowBioPrintable.asp?BioId=34298'
text = dh.webPageToText(url)
fullwordlist = dh.stripNonAlphaNum(text)
wordlist = dh.removeStopwords(fullwordlist, dh.stopwords)
dictionary = dh.wordListToFreqDict(wordlist)
sorteddict = dh.sortFreqDict(dictionary)

# compile dictionary into string and wrap with HTML
outstring = ""
for s in sorteddict:
    outstring += str(s)
    outstring += "<br />"
dh.wrapStringInHTML("html-to-freq-3", url, outstring)